from Ecommerce.dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from Ecommerce.myexceptions.CustomerNotFoundException import CustomerNotFoundException
from Ecommerce.myexceptions.ProductNotFoundException import ProductNotFoundException
from Ecommerce.myexceptions.OrderNotFoundException import OrderNotFoundException

def main():
    repo = OrderProcessorRepositoryImpl()

    while True:
        print("\n========== ECOMMERCE MENU ==========")
        print("1. Create Customer")
        print("2. Add Product")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Place Order")
        print("6. View Orders")
        print("7. Remove Product from Cart")
        print("8. Delete Product")
        print("9. Delete Customer")
        print("10. Exit")
        print("====================================")

        choice = input("Enter your choice (1-10): ")

        try:
            if choice == '1':
                name = input("Enter customer name: ")
                email = input("Enter customer email: ")
                password = input("Enter password: ")
                repo.createCustomer(name, email, password)

            elif choice == '2':
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                description = input("Enter product description: ")
                stock = int(input("Enter stock quantity: "))
                repo.addProduct(name, price, description, stock)

            elif choice == '3':
                cust_id = int(input("Enter customer ID: "))
                prod_id = int(input("Enter product ID: "))
                quantity = int(input("Enter quantity: "))
                repo.addToCart(cust_id, prod_id, quantity)

            elif choice == '4':
                cust_id = int(input("Enter customer ID: "))
                repo.viewCart(cust_id)

            elif choice == '5':
                cust_id = int(input("Enter customer ID: "))
                address = input("Enter shipping address: ")
                repo.placeOrder(cust_id, address)

            elif choice == '6':
                cust_id = int(input("Enter customer ID: "))
                repo.viewCustomerOrders(cust_id)

            elif choice == '7':
                cust_id = int(input("Enter customer ID: "))
                prod_id = int(input("Enter product ID to remove: "))
                repo.removeFromCart(cust_id, prod_id)

            elif choice == '8':
                prod_id = int(input("Enter product ID to delete: "))
                repo.deleteProduct(prod_id)

            elif choice == '9':
                cust_id = int(input("Enter customer ID to delete: "))
                repo.deleteCustomer(cust_id)

            elif choice == '10':
                print("Exiting application. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 10.")

        except CustomerNotFoundException as e:
            print(f"Error: {e}")
        except ProductNotFoundException as e:
            print(f"Error: {e}")
        except OrderNotFoundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
