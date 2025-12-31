from classes.Product import Product
from classes.Order import Order
from products.Clothing import Clothing
from products.Electronics import Electronics
from products.Food import Food
import datetime



class Inventory:
    """Main inventory management system class"""
    def __init__(self):
        self._products = {}
        self._suppliers = []
        self._orders = []
    
    @property
    def products(self):
        return self._products.copy()

    @staticmethod
    def calculate_inventory_value(products):
        return sum(product.calculate_value_of_stock() for product in products)

    @classmethod
    def create_sample_inventory(cls):
        """Class method to create a sample inventory with different product types"""
        inventory = cls()

        e = Electronics("ayfon", 15, 1, 12)
        c = Clothing("Gore", 8, 3,"XL","Cotton","Please send cargo to this address ...")
        f = Food("Kiwi", 4, 150, datetime.date.today() - datetime.timedelta(days=30))
        f2 = Food("Apple", 1, 100, datetime.date.today() + datetime.timedelta(days=30))
        
        inventory.add_product(e)
        inventory.add_product(c)
        inventory.add_product(f)
        inventory.add_product(f2)

        return inventory

    #BASIC FUNCTIONS

    def add_product(self, product:Product):
        if product in self._products.values():
            self._products[product.id].quantity += product.quantity
        else:
            self._products[product.id] = product

    def update_product(self, product:Product, name:str, price:float, quantity:int):
        product.name = name
        product.price = price
        product.quantity = quantity

        return product

    def remove_product(self, product:Product):
        if product.id in self._products:
            self._products.pop(product.id)
        else:
            return f"There is no product that has id:{product.id}"

    def list_product(self):
        list_text = ""
        for key, value in self._products.items():
            list_text += str(value) + "\n"
        return list_text

    def get_product_count(self):
        return len(self._products)

    #FILTERS

    def find_product_by_id(self, product_id:Product.id):
        if product_id in self._products:
            return self._products[product_id]
        else:
            return f"There is no product that has id: {product_id}"

    def find_product_by_name(self, name:str):
        if name or len(name) > 0:
            for product in self._products.values():
                if name.lower() == product.name.lower():
                    return product 

    def find_product_by_type(self, type:str):
        list = []
        for product in self._products.values():
            if product.get_product_type() == type:
                list.append(product)
        return list

    def find_product_by_price(self, start:int, end:int):
        list = []
        for product in self._products.values():
            if start <= product.price <= end:
                list.append(product)
        return list

    def find_product_by_quantity(self, start:int, end:int):
        list = []
        for product in self._products.values():
            if start <= product.quantity <= end:
                list.append(product)
        return list

    def find_product_by_date(self, start: datetime, end: datetime):
        result = []
        for product in self._products.values():
            if start <= product._creation_date <= end:
                result.append(product)
        return result



    def get_low_stock_products(self, num:int):
        return [product for product in self._products.values()
                if product.quantity < num]

    def generate_inventory_report(self):
        """
        Generate an inventory report
        """
        report = "=== INVENTORY REPORT ===\n"
        report += f"Total Products: {len(self._products)}\n"
        report += f"Total Value Of Inventory {Inventory.calculate_inventory_value(self._products.values())}\n\n"

        #add product_groups

        #low stock alert
        low_stock = self.get_low_stock_products(5)
        if low_stock:
            report += "=== LOW STOCK ALERT ===\n"
            for stock in low_stock:
                report += str(stock) + "\n"

        return report

    def add_supplier(self, supplier):
        self._suppliers.append(supplier)

    def create_order(self, order_type = "Purchase"):
        order = Order(order_type)
        self._orders.append(order)
        return order

    def textify(self,list):
        txt = "Here are the products:\n"
        for i in list:
            txt += str(i) + "\n"
        return txt

    def get_expired_products(self):
        """    
        def get_expired_products(self):
            expired = []
            for product in self._products.values():
                if isinstance(product, Perishable) and product.is_expired():
                    expired.append(product)
            return expired
        """
        list = []
        for p in self._products.values():
            if p.get_product_type() == "Food" and p.is_expired():
                list.append(p)
        return self.textify(list)
    
