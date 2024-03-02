import CellPhoneClass as c

def main():
    
    #create class object
    cellphone = c.Cellphone()
    
    #input manufacturer
    manufacturer =  input('Please input manufacturer name: ')
    cellphone.set_manufact(manufacturer)
    
    #input model
    model = input('Please enter model: ')
    cellphone.set_model(model)
    
    #input price
    price = input('Please enter retail price: ')
    cellphone.set_retail(price)
    
    print(f'Manufacturer: {cellphone.get_manufact()}')
    print(f'Model: {cellphone.get_model()}')
    print('Retail Price: $', format(cellphone.get_retail_price(), ',.2f'),sep='')
    
main()