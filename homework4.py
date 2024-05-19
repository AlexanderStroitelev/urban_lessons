immutable_var = (1,2,3, ['fbc', 3, True],'string')
print(immutable_var)
immutable_var[1] = 'banana'
print(immutable_var) # !!!Ошибка - мы пытаемся изменить неизменяемое
                     # значение в кортеже - 2 на 'banana'

# чтобы увидет решение по изменяемым спискам - задокументируй данные до этого блока

mutable_list = ['banana', True, 5, 7, 'my_cat']
mutable_list[1] = False
print(mutable_list)
