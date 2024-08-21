# product.py

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id  # Unique ID for the product
        self.name = name  # Name of the product
        self.price = price  # Price of the product
        self.status = 'Active'  # Status of the product (Active/Suspended)

    def create_product(self):
        print(f"Product {self.name} with ID {self.product_id} has been created.")

    def update_product(self, name=None, price=None):
        if name:
            self.name = name
        if price:
            self.price = price
        print(f"Product {self.product_id} has been updated.")

    def remove_product(self):
        self.status = 'Suspended'
        print(f"Product {self.name} has been suspended.")
