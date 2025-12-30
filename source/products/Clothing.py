from classes.Product import Product

class Clothing(Product):
    materials = ["cotton", "silk", "leather", "linen", "wool", "hemp"]
    clothing_sizes = ["XS", "S", "M", "L", "XL", "XXL"]
    def __init__(self, name:str, price:float, quantity:int, size:str, material:str, additional_info:str=""):
        super().__init__(name, price, quantity,)
        self._size = size
        self._material = material
        self._info = additional_info

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size_of_clothing:str):
        if not size_of_clothing or size_of_clothing not in Clothing.clothing_sizes:
            raise ValueError(f"Please choose from {Clothing.clothing_sizes}")
        self._size = size_of_clothing

    @property
    def info(self):
        return f"Name: {self.name} \nAdditional Info: {self._info}"
    
    @property
    def material(self):
        return self._material
    @material.setter
    def material(self, material_type:str):
        if not material_type or material_type not in Clothing.materials:
            raise ValueError(f"Please choose from {Clothing.materials}")
        self._material = material_type

    def get_product_type(self):
        return "Clothing"

    def __repr__(self):
        return f"{super().__repr__()}, Size: {self._size}, Material: {self._material}"


