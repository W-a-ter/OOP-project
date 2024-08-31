from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """базовый абстрактный класс """

    @abstractmethod
    def __add__(self, other):
        pass
