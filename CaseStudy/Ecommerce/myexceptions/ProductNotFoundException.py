class ProductNotFoundException(Exception):
    def __init__(self, message="Product not found."):
        super().__init__(message)
