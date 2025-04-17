class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer not found."):
        super().__init__(message)
