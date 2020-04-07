from __future__ import annotations
from abc import ABC, abstractmethod
from car.Car import Car
from motorcycle.Motorcycle import Motorcycle


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self) -> Motorcycle:
        pass
