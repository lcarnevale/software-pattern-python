from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def useful_function_a(self) -> str:
        pass
