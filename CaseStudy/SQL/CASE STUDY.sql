CREATE DATABASE EcommerceDB;
GO
USE EcommerceDB;
GO

CREATE TABLE customers (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) UNIQUE NOT NULL,
    password NVARCHAR(255) NOT NULL
);


CREATE TABLE products (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description NVARCHAR(MAX),
    stockQuantity INT NOT NULL
);
SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'products';
EXEC sp_columns 'products';


CREATE TABLE cart (
    cart_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

CREATE TABLE orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT,
    order_date DATETIME DEFAULT GETDATE(),
    total_price DECIMAL(10,2) NOT NULL,
    shipping_address NVARCHAR(MAX) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE order_items (
    order_item_id INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

INSERT INTO customers (name, email, password) VALUES 
('Alice Johnson', 'alice@example.com', 'password123'),
('Bob Smith', 'bob@example.com', 'password456'),
('Charlie Brown', 'charlie@example.com', 'password789'),
('Diana Prince', 'diana@example.com', 'password321'),
('Ethan Hunt', 'ethan@example.com', 'password654');
GO --batch seperation

INSERT INTO products (name, price, description, stockQuantity) VALUES 
('Laptop', 800.00, 'High performance laptop', 10),
('Smartphone', 500.00, 'Latest model smartphone', 15),
('Headphones', 100.00, 'Noise-canceling headphones', 30),
('Smartwatch', 250.00, 'Water-resistant smartwatch', 20),
('Gaming Mouse', 50.00, 'Ergonomic gaming mouse', 40);
GO

IF OBJECT_ID('CreateCustomer', 'P') IS NOT NULL DROP PROCEDURE CreateCustomer;
GO 
--Checks if an object named 'CreateCustomer' exists in the database
-- NOT NULL- Condition is true if the object exists
--DROP PROCEDURE Removes the stored procedure from the database

IF OBJECT_ID('AddProduct', 'P') IS NOT NULL DROP PROCEDURE AddProduct;
GO

IF OBJECT_ID('DeleteProduct', 'P') IS NOT NULL DROP PROCEDURE DeleteProduct;
GO

IF OBJECT_ID('DeleteCustomer', 'P') IS NOT NULL DROP PROCEDURE DeleteCustomer;
GO

IF OBJECT_ID('AddToCart', 'P') IS NOT NULL DROP PROCEDURE AddToCart;
GO

IF OBJECT_ID('RemoveFromCart', 'P') IS NOT NULL DROP PROCEDURE RemoveFromCart;
GO

IF OBJECT_ID('PlaceOrder', 'P') IS NOT NULL DROP PROCEDURE PlaceOrder;
GO

CREATE PROCEDURE CreateCustomer @name NVARCHAR(100), @email NVARCHAR(100), @password NVARCHAR(255) --Creates a new stored procedure named "CreateCustomer"
AS
BEGIN
    INSERT INTO customers (name, email, password) VALUES (@name, @email, @password); 
END
GO

CREATE PROCEDURE AddProduct @pname NVARCHAR(100), @pprice DECIMAL(10,2), @pdesc NVARCHAR(MAX), @pstock INT
AS
BEGIN
    INSERT INTO products (name, price, description, stockQuantity) VALUES (@pname, @pprice, @pdesc, @pstock);
END
GO

CREATE PROCEDURE DeleteProduct @productId INT
AS
BEGIN
    DELETE FROM products WHERE product_id = @productId; --safely removes a product from your database by its ID
END
GO

CREATE PROCEDURE DeleteCustomer @customerId INT
AS
BEGIN
    DELETE FROM customers WHERE customer_id = @customerId;
END
GO
/*Remove the customer's shopping cart items */

CREATE PROCEDURE AddToCart @customerId INT, @productId INT, @quantity INT
AS
BEGIN
    INSERT INTO cart (customer_id, product_id, quantity) VALUES (@customerId, @productId, @quantity);
END
GO
/*Centralizes cart addition logic */

CREATE PROCEDURE RemoveFromCart @customerId INT, @productId INT
AS
BEGIN
    DELETE FROM cart WHERE customer_id = @customerId AND product_id = @productId;
END
GO 
--removes only the specified product from the specified customer's cart
--WHERE clause with both conditions ensures no accidental mass deletions

--PLACE ORDER
CREATE PROCEDURE PlaceOrder @cust_id INT, @ship_addr NVARCHAR(MAX) --@cust_id: The customer ID placing the order, @ship_addr: The shipping address for the order
AS
BEGIN
    DECLARE @total DECIMAL(10,2);
    SELECT @total = SUM(p.price * c.quantity) FROM cart c  --(COST OF THE PRODUCT)
    JOIN products p ON c.product_id = p.product_id -- inner join customer productID and Product ProductId
    WHERE c.customer_id = @cust_id; 

    INSERT INTO orders (customer_id, total_price, shipping_address) 
    VALUES (@cust_id, @total, @ship_addr);
    
    DECLARE @order_id INT;
    SET @order_id = SCOPE_IDENTITY(); --auto generates new orderID

    INSERT INTO order_items (order_id, product_id, quantity)
    SELECT @order_id, c.product_id, c.quantity FROM cart c WHERE c.customer_id = @cust_id; --transfer the cart to order items

    DELETE FROM cart WHERE customer_id = @cust_id; --clears the customer's cart
END
GO 
--VIEW CART
CREATE PROCEDURE ViewCart @customerId INT
AS
BEGIN
SELECT p.product_id, p.name, p.price, c.quantity 
FROM cart c
JOIN products p ON c.product_id= p.product_id WHERE c.customer_id = @customerId; -- combines two table cart and products
END
GO 

--VIEW CUSTOMER ORDERS
CREATE PROCEDURE ViewCustomerOrders @customerId INT
AS
BEGIN
SELECT o.order_id, o.order_date, o.total_price, o.shipping_address, p.name AS product_name, 
oi.quantity
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id --combines orders and order items
JOIN products p ON oi.product_id = p.product_id WHERE o.customer_id = @customerId;
END
GO

select*from customers;
select*from products;
select*from Cart;
select*from orders;
