class Product:

    def __init__(self, name, description, price, quantity):
        """ инициализация объектов"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """метод, возвращающий строковое значение обьекта"""
        return f'{self.name}, {self.__price} руб., Остаток: {self.quantity} шт.'

    def __add__(self, other):
        result = self.quantity * self.price
        result_ = other.quantity * other.price
        return result + result_

    @classmethod
    def new_product(cls, params_product: dict):
        return cls(
            name=params_product["name"],
            description=params_product["description"],
            price=params_product["price"],
            quantity=params_product["quantity"]
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, prices):
        if prices < self.__price:
            print(f"Вы точно хотите понизить цену с "
                  f"{self.__price} до {prices}? y/n\n")
            user = input()
            if user == "y":
                if prices <= 0:
                    print("Цена не должна быть нулевая или отрицательная")
                    return
                self.__price = prices
            return
