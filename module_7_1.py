class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

    def exists(self, file_name = 'products.txt'):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    if line.strip().split(',')[0] == self.name:
                        return True
        except FileNotFoundError:
            return False
        return False


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''

    def add(self, *products):
        for product in products:
            if not product.exists():
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
            else:
                print(f"Продукт {product.name} уже есть в магазине")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')  # это не будет добавлено, потому что продукт с именем "Potato" уже существует

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
