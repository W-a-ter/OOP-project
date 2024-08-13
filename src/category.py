class Category:
    counter_products = 0
    counter_category = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        self.counter_products += len(products)
        self.counter_category += 1

    def __str__(self):
        return f'{self.name}, количество продуктов {self.counter_products} шт.'

    def add_product(self, new_products):
        """метод, добавления продукта в категорию"""
        self.__products.append(new_products)
        self.counter_products += 1

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
