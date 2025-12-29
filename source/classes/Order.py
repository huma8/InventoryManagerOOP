import datetime
from classes.Product import Product

class Order:
    _order_id_counter = 1
    def __init__(self, order_type:str="Purchase"):
        self._order_id = Order._order_id_counter
        self._order_type = order_type #purchase or sale
        self._items = []
        self._date = datetime.datetime.now()
        self._total_amount = 0
        Order._order_id_counter += 1
    
    @property
    def order_id(self):
        return self._order_id

    @property
    def order_type(self):
        return self._order_type
    @order_type.setter
    def order_type(self, value:str="Sale"):
        if value and (value == "Sale" or value == "Purchase"):
            self._order_type = value
        else:
            raise ValueError("Choose either \"Sale\" or \"Purchase\"")
    
    @property
    def order_items(self):
        return self._items
    
    @property
    def order_date(self):
        return self._date
    
    @property
    def order_amount(self):
        return self._total_amount

    def add_item(self, product:Product, quantity):
        if quantity < 0:
            raise ValueError("Quantity must be above 0")
        if self._order_type == "Sale" and product.quantity < quantity:
            raise ValueError(f"There is not enough product. Stock: {product.quantity}")

        for i, (pro, qua) in enumerate(self._items):
            if product.id == pro.id:
                self._items[i] = (pro, quantity + qua)
                self._calculate_total()
                return
        
        self._items.append((product, quantity))
        self._calculate_total()

    def remove_item(self, product:Product):
        self._items = [(p,q) for p, q in self._items if p.id != product.id]
        self._calculate_total()

    def _calculate_total(self):
        self._total_amount = sum(product.price*quantity for product, quantity in self._items)

    def execute_order(self):
        for product, quantity in self._items:
            if self._order_type == "Purchase":
                product.add_stock(quantity)
            elif self._order_type == "Sale":
                if not product.remove_stock(quantity):
                    raise ValueError(f"Insufficient stock for: {product.name}")
    
    def __repr__(self):
        return f"Order(Id: {self._order_id}, Type: {self._order_type}, Items: {len(self._items)}, Total: {self._total_amount}, Date: {self._date}"
    
