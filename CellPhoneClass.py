class CellPhone:
    def __init__(self, manu):
        self.__manufact = manu

    def __init__(self, mod):
        self.__model = mod

    def __init__(self, rprice):
        self.__retail_price = rprice

    ###############################################

    def set_manufact(self, str):
        return self.__manufact

    def set_model(self, str):
        return self.__model

    def set_retail_price(self, amount):
        return self.__retail_price

    ###############################################

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
