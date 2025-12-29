from classes.Product import Product
class Supplier:
    """Supplier class for managing product suppliers"""

    def __init__(self, name:str, contact_info:str):
        self._name = name
        self._contact = contact_info
        self._products = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value:str):
        if value and 0 < len(value.strip()) <= 25:
            self._name = value
        else:
            raise ValueError(f"The value range isnt between 0-25")
    
    @property
    def contact_info(self):
        return self._contact
    @contact_info.setter
    def contact_info(self, value:str):
        if value:
            self._contact = value
        else:
            raise ValueError("Check the contact_info value!!!")
    
    def add_product(self, *products:Product):
        if products:
            for product in products:
                self._products.append(product)

    def remove_product(self, product:Product):
        if product and product in self._products:
            self._products.remove(product)

    def get_supplied_products(self):
        return self._products
    
    def __repr__(self):
        return f"Supplier(Name: {self._name}, Contact info: {self._contact}, Product count: {len(self._products)})"
    