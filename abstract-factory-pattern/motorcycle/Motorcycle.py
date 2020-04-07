from abc import ABC, abstractmethod


class Motorcycle(ABC):

    @abstractmethod
    def useful_function_b(self) -> str:
        pass
