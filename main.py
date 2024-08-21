# main.py

from policyholder import Policyholder
from product import Product
from payment import Payment

# Create products
product1 = Product("P001", "Health Insurance", 1000)
product1.create_product()

# Create policyholders
ph1 = Policyholder("Jasmine", "PH001")
ph2 = Policyholder("Samuel", "PH002")

# Register policyholders
ph1.register()
ph2.register()

# Suspend and reactivate a policyholder
ph1.suspend()
ph1.reactivate()

# Add products to policyholders
ph1.add_product(product1)

# Process payments
payment1 = Payment("PMT001", "PH001", 1000, "2024-09-01")
payment1.process_payment()

# Display policyholder details
print(f"Policyholder {ph1.name}: {ph1.status}, Products: {[p.name for p in ph1.products]}")
print(f"Policyholder {ph2.name}: {ph2.status}, Products: {[p.name for p in ph2.products]}")
