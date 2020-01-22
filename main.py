from bike import Bicycle
from car import Car

def main():
    bike1 = Bicycle("black", "BMX", "Garth", 2, "Michelin", 8)
    bike1.pedal()
    print(bike1.vehicle.wheels.size)
    print(bike1.get_color())
    car1 = Car("red", "Ford Pinto", "Wayne", 4, "Michelin", 20)
    print(car1.vehicle.color)
    print(car1.get_model())
    print(car1.vehicle.wheels.size)
    car1.brake()
    
if __name__== "__main__":
    main()

