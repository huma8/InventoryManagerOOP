from classes.Product import Product
import datetime

class Food(Product):
    def __init__(self, name:str, price:float, quantity:int, expiry_date:datetime.date, additional_info:str=""):
        super().__init__(name, price, quantity)
        self._expiry_date = expiry_date
        self._info = additional_info

    @property
    def expiry_date(self):
        return self._expiry_date
    
    @expiry_date.setter
    def expiry_date(self, value:datetime.date):
        if value < datetime.date.today():
            raise ValueError("Expiry date cannot be in the past")
        self._expiry_date = value

    @property
    def info(self):
        return f"Name: {self.name} \nAdditional Info: {self._info}"

    def is_expired(self):
        return self._expiry_date < datetime.date.today()
    
    def get_product_type(self):
        return "Food"
    
    def __repr__(self):
        return f"{super().__repr__()} Expiry date: {self.expiry_date}"
    
    