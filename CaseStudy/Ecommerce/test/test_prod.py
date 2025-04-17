import unittest
from unittest.mock import patch, MagicMock
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from myexceptions.CustomerNotFoundException import CustomerNotFoundException
from myexceptions.ProductNotFoundException import ProductNotFoundException
from myexceptions.OrderNotFoundException import OrderNotFoundException


class TestOrderProcessorRepositoryImpl(unittest.TestCase):

    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl._execute_procedure')
    def test_create_product_success(self, mock_execute):
        mock_execute.return_value = None  # Simulate successful DB operation
        repo = OrderProcessorRepositoryImpl()
        product_name = "Laptop"
        price = 1200.00
        description = "High-end laptop"
        stock_quantity = 10
        repo.addProduct(product_name, price, description, stock_quantity)
        mock_execute.assert_called_with("AddProduct", [product_name, price, description, stock_quantity])

    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl._execute_procedure')
    def test_add_to_cart_success(self, mock_execute):
        mock_execute.return_value = None  # Simulate successful DB operation
        repo = OrderProcessorRepositoryImpl()
        customer_id = 1
        product_id = 101
        quantity = 2
        repo.addToCart(customer_id, product_id, quantity)
        mock_execute.assert_called_with("AddToCart", [customer_id, product_id, quantity])

    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl._execute_procedure')
    def test_place_order_success(self, mock_execute):
        mock_execute.return_value = None  # Simulate successful DB operation
        repo = OrderProcessorRepositoryImpl()
        customer_id = 1
        shipping_address = "123 Street, City, Country"
        repo.placeOrder(customer_id, shipping_address)
        mock_execute.assert_called_with("PlaceOrder", [customer_id, shipping_address])

    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl._execute_procedure')
    def test_customer_not_found_exception(self, mock_execute):
        # Simulate the database query that would raise the CustomerNotFoundException
        mock_execute.side_effect = CustomerNotFoundException("Customer not found")

        repo = OrderProcessorRepositoryImpl()

        # Verify that the exception is raised when trying to fetch customer orders for a non-existing customer
        with self.assertRaises(CustomerNotFoundException):
            repo.viewCustomerOrders(999)  # Simulating non-existing customer ID

    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl._execute_procedure')
    def test_product_not_found_exception(self, mock_execute):
        # Simulate the database query that would raise the ProductNotFoundException
        mock_execute.side_effect = ProductNotFoundException("Product not found")

        repo = OrderProcessorRepositoryImpl()

        # Provide the missing quantity argument
        with self.assertRaises(ProductNotFoundException):
            repo.addToCart(1, 999, 1)  # Simulating non-existing product ID with quantity 1


# Simulating non-existing product ID

if __name__ == '__main__':
    unittest.main()
