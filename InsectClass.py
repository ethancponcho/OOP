import random

class Insect:
    
    def __init__(self,w,l,n):
        self.wings = w
        self.legs = l
        self.flight = 0
        self.name = n
        
    def fly(self): #mutator method/set method
        self.flight = random.randint(1, 10)
        
    def get_flight_miles(self): #accessor method
        return self.flight 
    
    def get_name(self):
        return self.name