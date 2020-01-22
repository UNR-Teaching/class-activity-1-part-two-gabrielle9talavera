from vehicle import Vehicle

class Bicycle(Vehicle):

    color = ""
    model = ""
    owner = ""

    def __init__(self, c, m, o, n, b, s):
        self.vehicle = Vehicle(c, m, o, n, b, s)

    def get_color(self):
        return self.vehicle.color

    def get_model(self):
        return self.vehicle.model

    def get_owner(self):
        return self.vehicle.owner

    def set_color(self, x):
        self.vehicle.color = x

    def set_model(self, x):
        self.vehicle.model = x

    def set_owner(self, x):
        self.vehicle.owner = x  

    def pedal(self):
        print("Pedaling Bicycle")

    def brake(self):
        print("Bike Braking")

    def ring(self):
        print("Bike Bell Ringing")

