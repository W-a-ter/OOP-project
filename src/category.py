from src.product import Product


class Category:
    counter_products = 0
    counter_category = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        self.counter_products += len(products)
        self.counter_category += 1

    def result(self):
        try:
            result_ = sum([product.price for product in self.__products])
            total_quantity = sum([product.quantity
                                  for product in self.__products])
            total = result_/total_quantity
            return total
        except ZeroDivisionError:
            return '0'

    def __str__(self):
        return (f'{self.name}, количество продуктов: '
                f'{sum([product.quantity for product in self.__products])}'
                f' шт.')

    def add_product(self, new_products):
        """метод, добавления продукта в категорию"""
        if isinstance(new_products, Product):
            self.__products.append(new_products)
            self.counter_products += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += (f"{product.name}, "
                            f"{product.price} руб. Остаток: "
                            f"{product.quantity} шт.\n")
        return product_str

    @property
    def list_products(self):
        return self.__products
