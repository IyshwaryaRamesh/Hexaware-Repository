class Cart:
    def __init__(self, cart_id=None, customer_id=None, product_id=None, quantity=None):
        self.__cart_id = cart_id
        self.__customer_id = customer_id
        self.__product_id = product_id
        self.__quantity = quantity

    def get_cart_id(self):
        return self.__cart_id

    def set_cart_id(self, cart_id):
        self.__cart_id = cart_id

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity
