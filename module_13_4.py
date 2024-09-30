from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN = ''

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью. Напиши 'Calories' для начала.")

@dp.message_handler(Text(equals='Calories', ignore_case=True))
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число для возраста.")
        return

    await state.update_data(age=age)
    await message.answer("Введите свой рост (в сантиметрах):")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        growth = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число для роста.")
        return

    await state.update_data(growth=growth)
    await message.answer("Введите свой вес (в килограммах):")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    try:
        weight = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число для веса.")
        return

    await state.update_data(weight=weight)

    data = await state.get_data()
    age = data.get('age')
    growth = data.get('growth')
    weight = data.get('weight')
    bmr = 10 * weight + 6.25 * growth - 5 * age +5
    await message.answer(f"Ваша норма калорий: {bmr:.2f} ккал в день.")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
