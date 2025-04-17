class Product:
    def __init__(self, product_id=None, name=None, price=None, description=None, stock_quantity=None):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__description = description
        self.__stock_quantity = stock_quantity

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_stock_quantity(self):
        return self.__stock_quantity

    def set_stock_quantity(self, stock_quantity):
        self.__stock_quantity = stock_quantity
