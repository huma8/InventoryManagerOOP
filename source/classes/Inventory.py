from classes.Product import Product
class Inventory:
    """Main inventory management system class"""
    def __init__(self):
        self._products = {}
    
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

        p = Product("ayfon", 15, 1)
        p.name = "samsunG"
        p.price = 5
        p.quantity = 2.1

        t = Product("Gore", 8, 3)

        inventory.add_product(p)
        inventory.add_product(t)
        return inventory

    def add_product(self, product:Product):
        if product.id in self._products:
            self._products[product.id].quantity += product.quantity
        x = self.find_product_by_name(product.name)
        if x:
            self._products[x[0].id].quantity += product.quantity
        else:
            self._products[product.id] = product

    def remove_product(self, product:Product):
        if product.id in self._products:
            self._products.pop(product.id)
        else:
            return f"There is no product that has id:{product.id}"

    def get_product(self, product_id:Product.id):
        if product_id in self._products:
            return self._products[product_id]
        else:
            return f"There is no product that has id: {product_id}"

    def list_product(self):
        list_text = ""
        for key, value in self._products.items():
            list_text += str(value) + "\n"
        return list_text

    def find_product_by_name(self, name:str):
        if name or len(name) > 0:
            return [product for product in self._products.values()
                    if name.lower() in product.name.lower()]

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

    def add_supplier(args):
        pass

    def create_order(args):
        pass

    def get_expired_products(args):
        pass
