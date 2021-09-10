class Product():
    __hats = []
    __tshirts = []
    __hoodies = []
    __pants = []
    __shoes = []


class Hats(object):
    __id = 0
    price = 0
    __name = 0

    def __init__(self, id, name, price):
        self.__id = id
        self.price = price
        self.__name = name
