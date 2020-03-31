__author__ = "Lorenzo Carnevale"
__license__ = "MIT"
__email__ = "lorenzocarnevale@gmail.com"


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('The SingletonPattern is instanced')
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def useIt():
        print(".. and use it!")


if __name__ == '__main__':
    iterations = range(0, 5)
    for iteration in iterations:
        singleton = Singleton()
        singleton.useIt()
