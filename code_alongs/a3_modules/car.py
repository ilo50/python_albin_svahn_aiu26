from engine import Engine
from tire import Tire

class Car:
    print("car class")

    def __init__(self):
        self.tire = Tire()
        self.engine = Engine()

c = Car()
print(c.engine, c.tire)