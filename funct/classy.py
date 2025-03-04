class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info (self):
            print(f"car:{self.brand} {self.model}")

car = Car("Toyota","Camry")
car.display_info()