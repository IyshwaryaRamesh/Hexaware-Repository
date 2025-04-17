import pyodbc
from util.DBConnUtil import DBConnUtil
from myexceptions.CustomerNotFoundException import CustomerNotFoundException
from myexceptions.ProductNotFoundException import ProductNotFoundException
from myexceptions.OrderNotFoundException import OrderNotFoundException

class OrderProcessorRepositoryImpl:

    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def _execute_procedure(self, procedure_name, params):
        cursor = self.conn.cursor()
        cursor.execute(f"EXEC {procedure_name} {', '.join(['?' for _ in params])}", *params)
        self.conn.commit()

    def createCustomer(self, name, email, password):
        self._execute_procedure("CreateCustomer", [name, email, password])

    def addProduct(self, name, price, description, stock_quantity):
        self._execute_procedure("AddProduct", [name, price, description, stock_quantity])

    def addToCart(self, customer_id, product_id, quantity):
        self._execute_procedure("AddToCart", [customer_id, product_id, quantity])

    def viewCart(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute("EXEC ViewCart ?", customer_id)
        result = cursor.fetchall()
        if result:
            for row in result:
                print(f"Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Quantity: {row[3]}")
        else:
            print("Your cart is empty.")

    def placeOrder(self, customer_id, shipping_address):
        self._execute_procedure("PlaceOrder", [customer_id, shipping_address])

    def viewCustomerOrders(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute("EXEC ViewCustomerOrders ?", customer_id)
        result = cursor.fetchall()
        if not result:
            raise CustomerNotFoundException(f"Customer with ID {customer_id} not found.")
        # Otherwise, return or print the result
        for row in result:
            print(f"Order ID: {row[0]}, Date: {row[1]}, Total Price: {row[2]}, Shipping Address: {row[3]}")

        else:
            print("No orders found for this customer.")

    def removeFromCart(self, customer_id, product_id):
        self._execute_procedure("RemoveFromCart", [customer_id, product_id])

    def deleteProduct(self, product_id):
        self._execute_procedure("DeleteProduct", [product_id])

    def deleteCustomer(self, customer_id):
        self._execute_procedure("DeleteCustomer", [customer_id])

