from classes.Product import Product
from classes.Order import Order
from classes.Supplier import Supplier
from classes.Audit import AuditLog

from products.Clothing import Clothing
from products.Electronics import Electronics
from products.Food import Food
import json
import datetime



class Inventory:
    """Main inventory management system class"""
    with open("source/products/product_stock_threshold.json", "r", encoding="utf-8") as f:
        stock_threshold = json.load(f)
    def __init__(self):
        self._products = {}
        self._suppliers = []
        self._orders = []
        self._logs = []
    
    @property
    def products(self):
        return self._products.copy()

    @property
    def logs(self):
        txt=""
        for i in self._logs:
            txt += i + "\n"
        return txt + "\n\n"

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

    #APPLIER FUNCTIONS

#####
    def adjust_inventory(self, product_id, adjustment_amount, reason=""):
        """
        Adjust inventory for a specific product
        :param product_id: ID of the product to adjust
        :param adjustment_amount: Amount to adjust (positive for additions, negative for reductions)
        :param reason: Reason for the adjustment
        :return: Boolean indicating success
        """
        if product_id in self._products:
            old_quantity = self._products[product_id].quantity
            self._products[product_id].quantity += adjustment_amount
            # Prevent negative quantities
            if self._products[product_id].quantity < 0:
                self._products[product_id].quantity = 0
            self._logs.append(f"Inventory adjusted for product {product_id}: {old_quantity} -> {self._products[product_id].quantity} ({reason})")
            return True
        return False
    
    def correct_inventory(self, product_id, new_quantity, reason=""):
        """
        Correct inventory to a specific quantity
        :param product_id: ID of the product to correct
        :param new_quantity: New quantity to set
        :param reason: Reason for the correction
        :return: Boolean indicating success
        """
        if product_id in self._products and new_quantity >= 0:
            old_quantity = self._products[product_id].quantity
            self._products[product_id].quantity = new_quantity
            self._logs.append(f"Inventory corrected for product {product_id}: {old_quantity} -> {new_quantity} ({reason})")
            return True
        return False
#####

    def add_product(self, product:Product):
        if product in self._products.values():
            self._products[product.id].quantity += product.quantity
        else:
            self._products[product.id] = product
        
        self._logs.append(f"{AuditLog(product, "ADD", product.quantity)}")
        
    def update_product(self, product:Product, name:str, price:float, quantity:int):
        product.name = name
        product.price = price
        product.quantity = quantity

        self._logs.append(f"{AuditLog(product, "UPDATE", product.quantity)}")
        return product

    def remove_product(self, product:Product):
        if product.id in self._products:
            self._products.pop(product.id)
            self._logs.append(f"{AuditLog(product, "REMOVE", product.quantity)}")
        else:
            return f"There is no product that has id:{product.id}"

    def add_supplier(self, supplier:Supplier):
        self._suppliers.append(supplier)
        self._logs.append(f"{AuditLog(supplier, "SUPPLIER", 1)}")
        return None

    def create_order(self, order_type = "Purchase"):
        order = Order(order_type)
        self._orders.append(order)
        self._logs.append(f"{AuditLog(order_type, "ORDER", 1)}")

        return order

    
    #SUPPLIERS
    def find_supplier_by_name(self, name):
        """Find a supplier by name"""
        for supplier in self._suppliers:
            if supplier.name.lower() == name.lower():
                return supplier
        return None
    
    def find_suppliers_by_product_type(self, product_type:str):
        """Find suppliers that supply a specific product type"""
        matching_suppliers = []
        for supplier in self._suppliers:
            for product in supplier.get_supplied_products():
                if product.get_product_type() == product_type:
                    matching_suppliers.append(supplier)
                    break  # Don't add the same supplier multiple times
        return matching_suppliers
    
    def get_all_suppliers(self):
        """Return a list of all suppliers"""
        return self._suppliers

    def place_order_with_supplier(self, supplier:Supplier, products_quantities:dict):
        """
        Place an order with a supplier for specific products
        
        :param supplier: Supplier object to place order with
        :param products_quantities: Dictionary of product_id to quantity
        :return: Order object
        """
        order = self.create_order("Purchase")
        for product_id, quantity in products_quantities.items():
            product = self.find_product_by_id(product_id)
            if product:
                order.add_item(product, quantity)
        # Add the order to supplier's history
        supplier._add_order_to_history({
            'order': order,
            'date': datetime.datetime.now(),
            'status': 'pending'
        })
        return order

    def track_supplier_delivery(self, supplier:Supplier, order:Order, delivery_date:datetime.datetime=None):
        """
        Track delivery from a supplier
        :param supplier: Supplier object
        :param order: Order object that was delivered
        :param delivery_date: Date of delivery (defaults to now)
        :return: Boolean indicating success
        """
        if delivery_date is None:
            delivery_date = datetime.datetime.now()

        # Update order status in supplier's history
        for order_record in supplier._order_history:
            if order_record['order'].order_id == order.order_id:
                order_record['delivery_date'] = delivery_date
                order_record['status'] = 'delivered'
                # Record delivery time
                order_placed = order_record['date']
                delivery_time = (delivery_date - order_placed).days
                supplier.add_delivery_record(delivery_time)
                return True
        return False

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

    #REPORTS

    def list_product(self):
        list_text = ""
        for key, value in self._products.items():
            list_text += str(value) + "\n"
        return list_text

    def product_count(self):
        return len(self._products)

    def low_stock_products(self):
        return [product for product in self._products.values()
                if product.quantity < Inventory.stock_threshold["Products"][product.get_product_type()]]

    def product_groups(self):
        product_groups = {}
        for product in self._products.values():
            type = product.get_product_type()
            if type not in product_groups:
                product_groups[type] = []
            product_groups[type].append(product)
        
        return product_groups

    def generate_inventory_report(self):
        """
        Generate an inventory report
        """
        report = "=== INVENTORY REPORT ===\n"
        report += f"Total Products: {self.product_count()}\n"
        report += f"Total Value Of Inventory {Inventory.calculate_inventory_value(self._products.values())}\n\n"

        #ADD product_groups
        report += f"=== PRODUCTS BY GROUP ===\n"
        product_groups = self.product_groups()

        for type, prdct in product_groups.items():
            report += f"{type}:\n"
            for p in prdct:
                report += " - " + str(p) + "\n"
        report += "\n"

        #low stock alert
        low_stock = self.low_stock_products()
        if low_stock:
            report += "=== LOW STOCK ALERT ===\n"
            for stock in low_stock:
                report += str(stock) + "\n"

        return report

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

    def transaction_history(self):
        txt = ""
        for i in self._logs:
            txt += i + "\n"
        return txt
