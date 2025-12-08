class vehicle:
    def __init__(self,wheel,fuel_type,speed,price):
        self.wheel=wheel
        self.fuel_type=fuel_type
        self.speed=speed
        self.price=price 

    def show_details(self):
        print(f"total wheels:{self.wheel} ") 
        print(f"fuel_type:{self.fuel_type} ")  
        print(f"total speed:{self.speed} ")  
        print(f"total price:{self.price} ") 

    def accelerate (self,increase):
        self.speed+=increase         
    
class car(vehicle):
    def __init__(self):
        super().__init__(wheel=4, fuel_type="petrol", speed=78, price=100000)
     
my_car=car()        

my_car.show_details()



