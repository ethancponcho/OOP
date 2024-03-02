import CarClass as c

def main():
    
    car_1 = c.Car("Honda", "Civic")
    
    i = 0
    while i in range(0, 5):
        car_1.accelerate()
        print("Current Speed:", car_1.get_speed())
        i += 1
    
    i = 0
    while i in range(0, 5):
        car_1.brake()
        print("Current Speed:", car_1.get_speed())
        i += 1
        
main()