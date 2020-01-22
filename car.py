from vehicle import Vehicle

class Car(Vehicle):
    color = ""
    model = ""
    owner = ""

    def __init__(self, c, m, o, n, b, s):
        self.vehicle = Vehicle(c, m, o, n, b, s)

    def get_color(self):
        return self.vehicle.color

    def get_model(self):
        return self.vehicle.model

    def get_owner(self, x):
        return self.vehicle.owner

    def set_color(self, x):
        self.vehicle.color = x

    def set_model(self, x):
        self.vehicle.model = x

    def set_owner(self, x):
        self.vehicle.owner = x  

    def start(self):
        print("Starting Car")

    def brake(self):
        print("Car Braking")

    def honk(self):
        print("Car Honking")


def main():
    car1 = Car("red", "Ford Pinto", "Wayne", 4, "Michelin", 20)
    print(car1.vehicle.color)
    print(car1.vehicle.wheels.size)
    car1.brake()
    
if __name__== "__main__":
    main()
