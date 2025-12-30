from classes.Product import Product
from classes.Inventory import Inventory
from classes.Supplier import Supplier
from classes.Order import Order
from products.Electronics import Electronics
from products.Clothing import Clothing
from products.Food import Food

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

#-----------------------------------------------------------------

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

inventory = Inventory.create_sample_inventory()
p = Product("samsunG", 5.0, 1)
inventory.add_product(p)
inventory.add_product(p)
print(inventory.generate_inventory_report())

#-----------------------------------------------------------------

s = Supplier("HighLevel","highlevel@everest.com")
t = Product("Gore", 8, 1)
s.add_product(p,t)
s.remove_product(p)
print(s.get_supplied_products())

#-----------------------------------------------------------------

o = Order()
o.order_type = "Sale"
p = Product("Gore", 2.5, 4)
o.add_item(p, 4)
print(p)
print(o.order_amount)
o.execute_order()
print(p)
print(o.order_amount)

#-----------------------------------------------------------------

e = Electronics("ELGI", 15.24, 5, warranty_months=5, additional_info="Ayım andı dı watı pliz help mi")
print(e.info)

c = Clothing("Poncuk", 10.75, 4, "XL", "Cotton", additional_info="Please send cargo to this address ...")
print(c.info)


"""


