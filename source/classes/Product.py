"""Product class module."""
import datetime

class Product():
    """Base class for all products in the inventory system"""

    _id_counter:int = 0

    def __init__(self, name:str, price:float, quantity=1):
        self.__id = Product._id_counter
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__created_at = datetime.datetime.now()
        Product._id_counter += 1
    
    #PROPERTY_GETTERS
    @property
    def id(self):
        return self.__id  
    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def quantity(self):
        return self.__quantity
    @property
    def created_at(self):
        return self.__created_at
    
    #PROPERTY_SETTERS
    @name.setter
    def name(self, value:str):
        if not value or len(value.strip()) == 0:
            raise ValueError("Please define a value for name")
        self.__name = value

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be a negative number")
        if type(value != float):
            value = float(value)
        self.__price = value

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be a negative number")
        if type(value != int):
            value = int(value)
        self.__quantity = value

    def add_stock(self, value:int):
        if value < 0:
            raise ValueError("Cannot add a negative number")
        self.__quantity += value

    def remove_stock(self, value:int):
        if value < 0:
            raise ValueError("Cannot remove a negative number")
        if self.__quantity >= value:
            self.__quantity -= value
            return True
        return False    

    def calculate_value_of_stock(self):
        return f"Total value of stock is : {self.__quantity * self.__price}"

    def __repr__(self):
        return f"{self.__class__.__name__}(Product id: {self.__id}, name: {self.__name}, price: {self.__price}, quantity: {self.__quantity} \nCreated at {self.__created_at})"
