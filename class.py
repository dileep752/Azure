#class Car:
   # def __init__(self, name, model, year):
    #3 self.name = name
      #  self.model = model
     #   self.year = year
    #    self.speed = 0

   # def accelerate(self,amount):
     #   self.speed += amount
    #    return f"accelerate... new speed: '{self.speed}'km/hr."

   # def brake(self, amount):
    #    self.speed += amount
   #     return f"accelerate.. new speed : '{self.speed - amount}'."
    
  #  def display_info(self):
 #       return f"{self.name},{self.model},{self.year}."
    
#Bmw_instance = Car("Bmw","XL7","2025")
#print(Bmw_instance.display_info())
#print(Bmw_instance.accelerate(100))
#print(Bmw_instance.brake(90))

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self,amount):
        self.speed += amount
        return f"Accelerating... new speed: {self.speed}km/hr"
    def brake(self,amount):
        self.speed = max(0, self.speed - amount)
        return f"Braking... new speed: {self.speed}km/hr"

    def display_info(self):
        return f"{self.brand},{self.model},{self.year}"

Bmw_instance = Car("Bmw", "XL7","2025")

print(Bmw_instance.display_info())
print(Bmw_instance.accelerate(100))
print(Bmw_instance.brake(90))