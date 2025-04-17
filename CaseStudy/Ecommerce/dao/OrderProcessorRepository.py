from abc import ABC, abstractmethod

class OrderProcessorRepository(ABC):

    @abstractmethod
    def create_customer(self, customer): pass

    @abstractmethod
    def create_product(self, product): pass

    @abstractmethod
    def add_to_cart(self, cart): pass

    @abstractmethod
    def place_order(self, order): pass

    @abstractmethod
    def get_customer_by_id(self, customer_id): pass

    @abstractmethod
    def get_product_by_id(self, product_id): pass
