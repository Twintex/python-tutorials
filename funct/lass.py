# class Car:

#  #def __init__(self, brand, model, year):
#   self.brand = brand
#   self.model = model
#   self.year = year
# my_car = Car("Toyata", "corolla", 2016)
# #print(my_car.model)

class car:
    wheels = 4 #class varibles
    def __init__(self,brand):
     self.brand = brand #instance varible
     car_1 = car("Tayota")
     car_2 = car ("Honda")
     print(car_1.brand, car_1.wheels)