class PrintMixin:
    def __init__(self):
        super().__init__()
        print(repr(self))

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'({self.name}, {self.description}, '
                f'{self.price}, {self.quantity})')
