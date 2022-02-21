class CellPhone:

    ## only way to create instance is init method
    def __init__(self, manufacta, modelb, pricec):
        self.__manufact = manufacta
        self.__model = modelb
        self.__retail_price = pricec

    ###############################################
    ## the set manufact method aqccepts an argument for the phone's manufacturet
    def set_manufact(self, man):
        self.__manufact = man

    def set_model(self, mod):
        self.__model = mod

    def set_retail_price(self, price):
        self.__price

    ###############################################

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
