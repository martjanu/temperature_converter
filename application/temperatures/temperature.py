from abc import  ABC, abstractmethod

class Temperature(ABC):
    @abstractmethod
    def convert_to_calvin(self, amount):
        pass

    @abstractmethod
    def convert_from_calvin(self, amount):
        pass