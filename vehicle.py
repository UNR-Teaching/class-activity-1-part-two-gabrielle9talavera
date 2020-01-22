from abc import ABCMeta, abstractmethod

class Vehicle:
    __metaclass__ = ABCMeta 
    color = ""
    model = ""
    owner = ""

    def __init__(self, c, m, o, n, b, s):
        self.color = c
        self.model = m
        self.owner = o
        self.wheels = Wheels(n,b,s)

    def get_color(self):
        return self.color

    def get_model(self):
        return self.model

    def get_owner(self, x):
        return self.owner

    def set_color(self, x):
        self.color = x

    def set_model(self, x):
        self.model = x

    def set_owner(self, x):
        self.owner = x

    def brake(self):
        print("Braking")

class Wheels(Vehicle):
	number = 0
	brand = ""
	size = 0

	def __init__(self, n, b, s):
		self.number = n
		self.brand = b
		self.size = s
