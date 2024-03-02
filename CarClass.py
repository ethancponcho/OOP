class Car:
    
    def __init__(self,make,model):
        self.make = make
        self.model = model
        self.speed = 0
        
    def brake(self):
        self.speed -= 5
        
    def accelerate(self):
        self.speed += 5
    
    def get_speed(self):
        return self.speed