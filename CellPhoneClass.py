class Cellphone:
    
    def __innit__(self,m,n,p):
        self.__manufact = m
        self.__model = n
        self.__price = p

    def set_manufact(self,manufacturer):
        self.__manufact = manufacturer
    def set_model(self,model):
        self.__model = model
    def set_retail(self,price):
        self.__price = int(price)
    def get_manufact(self):
        return self.__manufact
    def get_model(self):
        return self.__model
    def get_retail_price(self):
        return  self.__price
            
            
        
        