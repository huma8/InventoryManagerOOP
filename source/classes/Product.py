"""Product class module."""
import datetime

class Product():
    """Base class for all products in the inventory system"""

    _id_counter:int = 1

    def __init__(self, name:str, price:float, quantity=1):
        self._id = Product._id_counter
        self._name = name
        self._price = price
        self._quantity = quantity
        self._created_at = datetime.datetime.now()
        Product._id_counter += 1
    
    #PROPERTY_GETTERS
    @property
    def id(self):
        return self._id  
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    @property
    def quantity(self):
        return self._quantity
    @property
    def created_at(self):
        return self._created_at
    
    #PROPERTY_SETTERS
    @name.setter
    def name(self, value:str):
        if not value or len(value.strip()) == 0:
            raise ValueError("Please define a value for name")
        self._name = value

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be a negative number")
        if type(value != float):
            value = float(value)
        self._price = value

    @quantity.setter
    def quantity(self, value:int):
        if value < 0:
            raise ValueError("Quantity cannot be a negative number")
        self._quantity = value

    def add_stock(self, value:int):
        if value < 0:
            raise ValueError("Cannot add a negative number")
        self._quantity += value

    def remove_stock(self, value:int):
        if value < 0:
            raise ValueError("Cannot remove a negative number")
        if self._quantity >= value:
            self._quantity -= value
            return True
        return False    

    def calculate_value_of_stock(self):
        return self._quantity * self._price
    
    def get_product_type(args):
        """Get Product Type By Children"""
        raise NotImplementedError("Make sure children of product class has get_product_type function")

    def __repr__(self):
        return f"{self.__class__.__name__}(Product id: {self._id}, Name: {self._name}, Price: {self._price}, Quantity: {self._quantity}, Created at {self._created_at})"
