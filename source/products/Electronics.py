from classes.Product import Product

class Electronics(Product):
    def __init__(self, name:str, price:float, quantity:int, warranty_months:int, additional_info:str=""):
        super().__init__(name, price, quantity)
        self._warranty_months = warranty_months
        self._info = additional_info
    
    @property
    def warranty_months(self):
        return self._warranty_months

    @warranty_months.setter
    def warranty_months(self, value):
        if value < 0:
            raise ValueError("Warranty Months Value must be above zero")
        self._warranty_months = value

    @property
    def info(self):
        return f"Name: {self.name} \nAdditional Info: {self._info}"

    def get_product_type(self):
        return "Electronics"
    
    def __repr__(self):
        return f"{super().__repr__()}, Warranty: {self._warranty_months} months"

