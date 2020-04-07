from VehicleFactory import VehicleFactory
from car.CarImpl import CarImpl
from motorcycle.MotorcycleImpl import MotorcycleImpl


class VehicleFactoryImpl(VehicleFactory):

    def create_car(self) -> CarImpl:
        return CarImpl()

    def create_motorcycle(self) -> MotorcycleImpl:
        return MotorcycleImpl()
