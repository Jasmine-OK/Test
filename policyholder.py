# policyholder.py

class Policyholder:
    def __init__(self, name, policy_id):
        self.name = name  # Name of the policyholder
        self.policy_id = policy_id  # Unique ID for the policyholder
        self.status = 'Active'  # Status of the policyholder (Active/Suspended)
        self.products = []  # List to store the products associated with the policyholder

    def register(self):
        print(f"Policyholder {self.name} with ID {self.policy_id} has been registered.")

    def suspend(self):
        self.status = 'Suspended'
        print(f"Policyholder {self.name} has been suspended.")

    def reactivate(self):
        if self.status == 'Suspended':
            self.status = 'Active'
            print(f"Policyholder {self.name} has been reactivated.")
        else:
            print(f"Policyholder {self.name} is already active.")

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added to {self.name}'s account.")
