from classes.Product import Product
class Supplier:
    """Supplier class for managing product suppliers"""
    _supplier_count = 0
    def __init__(self, name:str, contact_info:str):
        self._name = name
        self._contact = contact_info
        self._products = []
        self._delivery_times = []  # List of delivery time in days
        self._quality_ratings = []  # List of quality ratings (1-5)
        self._order_history = []   # List of order information
        Supplier._supplier_count += 1

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

    #DELIVERY TRACKERS
    def add_delivery_record(self, days_to_deliver):
        """Add a delivery time record"""
        if days_to_deliver > 0:
            self._delivery_times.append(days_to_deliver)

    def _get_avg_delivery_time(self):
        """Calculate average delivery time"""
        if self._delivery_times:
            return sum(self._delivery_times) / len(self._delivery_times)
        return 0
    
    def add_quality_rating(self, rating):
        """Add a quality rating (1-5)"""
        if 1 <= rating <= 5:
            self._quality_ratings.append(rating)

    def _get_avg_quality_rating(self):
        """Calculate average quality rating"""
        if self._quality_ratings:
            return sum(self._quality_ratings) / len(self._quality_ratings)
        return 0
    
    def _add_order_to_history(self, order_info):
        """Add order information to history"""
        self._order_history.append(order_info)

    def __repr__(self):
        return f"Supplier(Name: {self._name}, Contact info: {self._contact}, Product count: {len(self._products)})"
    