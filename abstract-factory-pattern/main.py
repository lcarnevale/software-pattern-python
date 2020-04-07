from VehicleFactory import VehicleFactory
from VehicleFactoryImpl import VehicleFactoryImpl


def client_code(vehicle_factory: VehicleFactory) -> None:
    car = vehicle_factory.create_car()
    print("%s" % (car.useful_function_a()))

    motorcycle = vehicle_factory.create_motorcycle()
    print("%s" % (motorcycle.useful_function_b()))


if __name__ == "__main__":
    client_code(VehicleFactoryImpl())
