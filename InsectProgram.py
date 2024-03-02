import InsectClass as i

def main():
    mosquito = i.Insect(2,4,"Mosquito")
    housefly = i.Insect(2,4,"Housefly")
    
    mosquito.fly()
    housefly.fly()
    
    print(f"{mosquito.get_name()} Miles: {mosquito.get_flight_miles()}")
    
    print(f"{housefly.get_name()} Miles: {housefly.get_flight_miles()}")
    
main()