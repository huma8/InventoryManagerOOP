from classes.Product import Product
from classes.Inventory import Inventory
from classes.Supplier import Supplier


"""
p = Product("ayfon", 15, 1)
p.name = "samsunG"
p.price = 5
p.quantity = 2.1

t = Product("Gore", 8, 3)

print(p.name)
print(p.price)
print(p.quantity)
print(p.calculate_value_of_stock())

i = Inventory()
i.add_product(p)
i.add_product(p)
i.add_product(t)
i.remove_product(p)
print(i.get_product(1))
print(i.list_product())
print(i.find_product_by_name("samsung"))
print(f"Total Value Of Inventory is {Inventory.calculate_inventory_value(i._products.values())}")
print(f"Products that has stock below 5 : {i.get_low_stock_products(5)}")

print(i.generate_inventory_report())
"""

inventory = Inventory.create_sample_inventory()
p = Product("samsunG", 5.0, 1)
inventory.add_product(p)
inventory.add_product(p)
print(inventory.generate_inventory_report())

s = Supplier("HighLevel","highlevel@everest.com")
t = Product("Gore", 8, 1)
s.add_product(p,t)
s.remove_product(p)
print(s.get_supplied_products())
