from classes.Product import Product


p = Product("ayfon", 15, 1)
p.name = "samsunG"
p.price = 5
p.quantity = 6.9
print(p.name)
print(p.price)
print(p.quantity)
print(p.calculate_value_of_stock())