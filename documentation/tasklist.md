# Detailed Implementation Tasklist for OOP Inventory Management System

## 1. Create base Product class in source/classes/Product.py with encapsulation, private attributes, and property getters/setters
- [x] Create the Product class with private attributes: `_id`, `_name`, `_price`, `_quantity`, `_created_at`
- [x] Implement constructor that initializes private attributes with validation
- [x] Add class attribute `_id_counter` to track product IDs
- [x] Create property getters for all attributes (id, name, price, quantity, created_at)
- [x] Create property setters for name, price, and quantity with validation
- [x] Add validation: name cannot be empty, price and quantity cannot be negative
- [x] Implement `add_stock()` method with validation
- [x] Implement `remove_stock()` method with validation and return boolean
- [x] Implement `calculate_value_of_stock()` method to calculate total value (price * quantity)
- [x] Add `__repr__()` method for string representation
- [x] Fix type conversion logic in setters (e.g., `if type(value) != float:` instead of `if type(value != float):`)
- [x] Fix get_product_type method in Product base class to include 'self' parameter 

## 2. Create base Inventory class in source/classes/Inventory.py with product storage and management methods
- [x] Create Inventory class with private attribute `_products` as a dictionary
- [x] Implement constructor to initialize empty product dictionary
- [x] Create `add_product()` method to add products to inventory
- [x] Create `remove_product()` method to remove products by ID
- [x] Create `get_product()` method to retrieve products by ID
- [x] Create `list_product()` method to return all products (note: method name is list_product, not list_products)
- [x] Add validation to prevent duplicate product IDs
- [x] Implement basic inventory management methods
- [x] Fix logic in add_product method to properly handle ID vs name matching
- [x] Implement `find_product_by_name()` method for searching products
- [x] Create `update_product()` method to modify existing products
- [x] Add `get_product_count()` method to return total number of products
- [x] Implement `get_total_value()` method to calculate inventory value
- [x] Create `get_low_stock_products()` method to identify products with low stock
- [x] Add filtering methods to get products by type, price range, quantity range, or creation date (find_product_by_type, find_product_by_price, find_product_by_quantity, find_product_by_date methods implemented)
- [x] Add inventory history/transaction tracking
- [x] Implement stock level monitoring with configurable thresholds
- [x] Create methods to track product movement (additions, removals)
- [x] Add inventory audit functionality
- [x] Implement inventory reports (by type, value, stock levels) - IMPLEMENTED but not properly marked as done (generate_inventory_report method exists)
- [x] Add methods to handle inventory adjustments and corrections
- [x] Add supplier management methods - add_supplier method implemented
- [x] Implement methods to manage multiple suppliers - suppliers stored in _suppliers list
- [x] Create functionality to associate products with suppliers - implemented through add_supplier method
- [x] Add supplier performance tracking (delivery times, quality, etc.)
- [x] Implement supplier search and filtering methods
- [x] Add methods to track supplier orders and deliveries
- [x] Create supplier contact management features - contact info is stored and managed through properties in Supplier class

## 3. Create base Supplier class in source/classes/Supplier.py with supplier information and product association
- [x] Create Supplier class with private attributes: `_name`, `_contact_info`, `_supplied_products`
- [x] Implement constructor to initialize supplier information
- [x] Create property getters and setters for name and contact_info
- [x] Implement `add_product()` method to associate products with supplier
- [x] Implement `remove_product()` method to disassociate products
- [x] Create `get_supplied_products()` method to return associated products
- [ ] Add validation to prevent duplicate product associations (modify add_product method to check if product is not already in self._products list before adding)
  Step-by-step:
  1. Open source/classes/Supplier.py
  2. Locate the add_product method
  3. Modify the method to check if the product is already in the list before adding:
     ```
     def add_product(self, *products:Product):
         if products:
             for product in products:
                 if product not in self._products:
                     self._products.append(product)
                 else:
                     print(f"Product {product.name} is already associated with this supplier")
     ```
  4. Save the file
- [ ] Add class method to create supplier from data
  Step-by-step:
  1. Open source/classes/Supplier.py
  2. Add the following class method after the constructor:
     ```
     @classmethod
     def from_dict(cls, data):
         """
         Create a Supplier instance from a dictionary
         :param data: Dictionary containing supplier information
         :return: Supplier instance
         """
         return cls(
             name=data.get('name', ''),
             contact_info=data.get('contact_info', '')
         )
     ```
  3. Save the file
- [ ] Add comprehensive docstrings to all methods (add docstrings to all methods in Product, Inventory, Supplier, Order, Electronics, Clothing, and Food classes)
  Step-by-step:
  1. Open source/classes/Product.py
  2. Add docstrings to all methods including __init__, property getters, setters, add_stock, remove_stock, calculate_value_of_stock, get_product_type, and __repr__
  3. Open source/classes/Inventory.py
  4. Add docstrings to all methods including __init__, property getters, add_product, remove_product, find_product_by_id, find_product_by_name, find_product_by_type, find_product_by_price, find_product_by_quantity, find_product_by_date, list_product, product_count, low_stock_products, product_groups, generate_inventory_report, textify, get_expired_products, transaction_history, and create_sample_inventory
  5. Open source/classes/Supplier.py
  6. Add docstrings to all methods including __init__, property getters, setters, add_product, remove_product, get_supplied_products, and __repr__
  7. Open source/classes/Order.py
  8. Add docstrings to all methods including __init__, property getters, add_item, remove_item, _calculate_total, execute_order, and __repr__
  9. Open source/products/Electronics.py
  10. Add docstrings to all methods including __init__, property getters, setters, get_product_type, and __repr__
  11. Open source/products/Clothing.py
  12. Add docstrings to all methods including __init__, property getters, setters, get_product_type, and __repr__
  13. Open source/products/Food.py
  14. Add docstrings to all methods including __init__, property getters, setters, is_expired, get_product_type, and __repr__

## 4. Create base Order class in source/classes/Order.py with order processing functionality
- [x] Create Order class with private attributes: `_order_id`, `_order_type`, `_items`, `_date`, `_total_amount`
- [x] Implement constructor with order type parameter ("Purchase" or "Sale")
- [x] Create class attribute `_order_id_counter` to track order IDs
- [x] Create property getters for order attributes (order_id, order_type, order_items, order_date, order_amount) - IMPLEMENTED but not properly marked as done
- [x] Implement `add_item()` method to add products to order with validation
- [x] Implement `remove_item()` method to remove products from order
- [x] Create `_calculate_total()` private method to update order total
- [x] Implement `execute_order()` method to process the order and update inventory - IMPLEMENTED but not properly marked as done
- [x] Add validation to ensure sufficient stock for sales orders
- [ ] Enhance Order class with more detailed order information
  Step-by-step:
  1. Open source/classes/Order.py
  2. Add new private attributes to store more detailed order information in the __init__ method:
     ```
     self._customer_name = ""  # Name of the customer for sales orders
     self._customer_contact = ""  # Contact information for the customer
     self._shipping_address = ""  # Shipping address for the order
     self._notes = ""  # Additional notes about the order
     self._status = "pending"  # Status of the order (pending, processed, cancelled, delivered)
     ```
  3. Add property getters and setters for these new attributes:
     ```
     @property
     def customer_name(self):
         return self._customer_name
     @customer_name.setter
     def customer_name(self, value):
         self._customer_name = value

     @property
     def customer_contact(self):
         return self._customer_contact
     @customer_contact.setter
     def customer_contact(self, value):
         self._customer_contact = value

     @property
     def shipping_address(self):
         return self._shipping_address
     @shipping_address.setter
     def shipping_address(self, value):
         self._shipping_address = value

     @property
     def notes(self):
         return self._notes
     @notes.setter
     def notes(self, value):
         self._notes = value

     @property
     def status(self):
         return self._status
     @status.setter
     def status(self, value):
         if value in ["pending", "processed", "cancelled", "delivered"]:
             self._status = value
         else:
             raise ValueError("Status must be one of: pending, processed, cancelled, delivered")
     ```
  4. Update the __repr__ method to include the new information
  5. Save the file
- [ ] Implement order status tracking (pending, processed, cancelled)
  Step-by-step:
  1. Open source/classes/Order.py
  2. The status property has already been added in the previous task, so ensure it's properly implemented
  3. Add methods to change order status:
     ```
     def mark_as_processed(self):
         """Mark the order as processed"""
         self._status = "processed"

     def mark_as_cancelled(self):
         """Mark the order as cancelled"""
         self._status = "cancelled"

     def mark_as_delivered(self):
         """Mark the order as delivered"""
         self._status = "delivered"

     def is_pending(self):
         """Check if order is still pending"""
         return self._status == "pending"

     def is_processed(self):
         """Check if order has been processed"""
         return self._status == "processed"

     def is_cancelled(self):
         """Check if order has been cancelled"""
         return self._status == "cancelled"

     def is_delivered(self):
         """Check if order has been delivered"""
         return self._status == "delivered"
     ```
  4. Update the execute_order method to automatically set status to "processed" when executed
  5. Save the file
- [ ] Create methods to handle partial order fulfillment
  Step-by-step:
  1. Open source/classes/Order.py
  2. Add a method to check if partial fulfillment is needed:
     ```
     def can_partial_fulfill(self):
         """Check if the order can only be partially fulfilled due to insufficient stock"""
         for product, requested_quantity in self._items:
             if product.quantity < requested_quantity:
                 return True
         return False
     ```
  3. Add a method to fulfill what is available:
     ```
     def partial_fulfill(self):
         """Execute the order for available quantities only"""
         fulfilled_items = []
         for product, requested_quantity in self._items:
             if self._order_type == "Purchase":
                 product.add_stock(requested_quantity)
                 fulfilled_items.append((product, requested_quantity))
             elif self._order_type == "Sale":
                 available_quantity = min(product.quantity, requested_quantity)
                 if product.remove_stock(available_quantity):
                     fulfilled_items.append((product, available_quantity))
                 else:
                     # If we can't remove stock, add what we have to fulfilled items
                     fulfilled_items.append((product, 0))
         # Update the order items to reflect what was actually fulfilled
         self._items = fulfilled_items
         self._status = "processed"
         return fulfilled_items
     ```
  4. Add a method to get fulfillment status:
     ```
     def get_fulfillment_status(self):
         """Get the fulfillment status of the order"""
         if self._status == "cancelled":
             return "cancelled"
         elif self.can_partial_fulfill():
             return "partial"
         else:
             return "full"
     ```
  5. Save the file
- [ ] Add order history and tracking functionality
  Step-by-step:
  1. Open source/classes/Inventory.py
  2. Add a private attribute to store order history in the __init__ method:
     ```
     self._order_history = []
     ```
  3. Add a method to add an order to history:
     ```
     def add_order_to_history(self, order):
         """Add an order to the history"""
         self._order_history.append({
             'order': order,
             'timestamp': datetime.datetime.now(),
             'executed': False
         })
     ```
  4. Add a method to mark an order as executed in history:
     ```
     def mark_order_executed(self, order_id):
         """Mark an order as executed in the history"""
         for record in self._order_history:
             if record['order'].order_id == order_id:
                 record['executed'] = True
                 record['execution_time'] = datetime.datetime.now()
                 return True
         return False
     ```
  5. Add a method to get order history:
     ```
     def get_order_history(self):
         """Get the order history"""
         return self._order_history
     ```
  6. Modify the execute_order method in the Order class to add tracking functionality
  7. Save the file
- [ ] Implement order validation and approval workflows
  Step-by-step:
  1. Open source/classes/Order.py
  2. Add a private attribute to track approval status in the __init__ method:
     ```
     self._approved = False  # Whether the order has been approved
     self._approver = None   # Who approved the order
     self._approval_date = None  # When the order was approved
     ```
  3. Add property getters for approval status:
     ```
     @property
     def approved(self):
         return self._approved
     ```
  4. Add a method to approve the order:
     ```
     def approve(self, approver_name):
         """Approve the order"""
         self._approved = True
         self._approver = approver_name
         self._approval_date = datetime.datetime.now()
         return True
     ```
  5. Add a method to validate the order before approval:
     ```
     def validate_order(self):
         """Validate the order before approval"""
         # Check that all items have valid quantities
         for product, quantity in self._items:
             if quantity <= 0:
                 return False
             # For sales orders, check if sufficient stock is available
             if self._order_type == "Sale" and product.quantity < quantity:
                 return False
         return True
     ```
  6. Modify the execute_order method to check if the order is approved before executing:
     ```
     def execute_order(self):
         # Only execute if the order is approved
         if not self._approved:
             raise Exception("Order must be approved before execution")
         for product, quantity in self._items:
             if self._order_type == "Purchase":
                 product.add_stock(quantity)
             elif self._order_type == "Sale":
                 if not product.remove_stock(quantity):
                     raise ValueError(f"Insufficient stock for: {product.name}")
         # Update status to processed
         self._status = "processed"
     ```
  7. Save the file
- [ ] Add methods to generate purchase orders for low-stock items
  Step-by-step:
  1. Open source/classes/Inventory.py
  2. Add a method to generate purchase orders for low-stock items:
     ```
     def generate_purchase_orders_for_low_stock(self, supplier=None, reorder_amounts=None):
         """
         Generate purchase orders for products that are below their minimum threshold
         :param supplier: Optional supplier to send the order to
         :param reorder_amounts: Optional dict specifying how much to reorder for each product
         :return: List of purchase orders
         """
         low_stock_products = self.low_stock_products()
         purchase_orders = []

         for product in low_stock_products:
             # Determine how much to order
             threshold = Inventory.stock_threshold["Products"][product.get_product_type()]
             current_quantity = product.quantity
             reorder_amount = threshold - current_quantity

             # If custom reorder amounts are provided, use those instead
             if reorder_amounts and product.id in reorder_amounts:
                 reorder_amount = reorder_amounts[product.id]

             # Create a purchase order
             order = self.create_order("Purchase")
             order.add_item(product, reorder_amount)

             # If a supplier is specified, associate the order with the supplier
             if supplier:
                 # This would require a method to link orders to suppliers
                 pass

             purchase_orders.append(order)

         return purchase_orders
     ```
  3. Add a method to automatically process these orders:
     ```
     def process_low_stock_orders(self, supplier=None, reorder_amounts=None):
         """
         Automatically create and approve purchase orders for low-stock items
         :param supplier: Optional supplier to send the order to
         :param reorder_amounts: Optional dict specifying how much to reorder for each product
         :return: List of processed orders
         """
         orders = self.generate_purchase_orders_for_low_stock(supplier, reorder_amounts)
         for order in orders:
             # Automatically approve the order
             order.approve("System")
         return orders
     ```
  4. Save the file
- [ ] Add class method to create order from data
  Step-by-step:
  1. Open source/classes/Order.py
  2. Add a class method to create an order from a dictionary:
     ```
     @classmethod
     def from_dict(cls, data, inventory):
         """
         Create an Order instance from a dictionary
         :param data: Dictionary containing order information
         :param inventory: Inventory instance to get products from
         :return: Order instance
         """
         order = cls(data.get('order_type', 'Purchase'))
         items_data = data.get('items', [])
         for item_data in items_data:
             product_id = item_data['product_id']
             quantity = item_data['quantity']
             product = inventory.find_product_by_id(product_id)
             if product:
                 order.add_item(product, quantity)
         return order
     ```
  3. Save the file
- [ ] Add comprehensive docstrings to all methods

## 5. Implement Electronics class in source/products/Electronics.py inheriting from Product with warranty attribute
- [x] Import Product class from classes.Product
- [x] Create Electronics class inheriting from Product
- [x] Implement constructor that calls super().__init__() and adds `_warranty_months` attribute
- [x] Create property getter and setter for warranty_months with validation (non-negative)
- [x] Override `get_product_type()` method to return "Electronics" (FIX: add 'self' parameter) - IMPLEMENTED but not properly marked as done
- [x] Override `__repr__()` method to include warranty information
- [ ] Add any electronics-specific methods if needed
  Step-by-step:
  1. Open source/products/Electronics.py
  2. Consider adding methods that are specific to electronic products:
     ```
     def is_under_warranty(self):
         """Check if the electronic product is still under warranty"""
         # Assuming the product was purchased at the time of creation
         # and the warranty is in months
         import datetime
         purchase_date = self._creation_date
         warranty_end_date = purchase_date + datetime.timedelta(days=self._warranty_months * 30)
         return datetime.date.today() <= warranty_end_date.date()

     def get_warranty_expiration_date(self):
         """Get the warranty expiration date"""
         import datetime
         purchase_date = self._creation_date.date()
         warranty_end_date = purchase_date + datetime.timedelta(days=self._warranty_months * 30)
         return warranty_end_date
     ```
  3. Add any other relevant methods for electronics
  4. Save the file
- [ ] Add comprehensive docstrings to all methods

## 6. Implement Clothing class in source/products/Clothing.py inheriting from Product with size and material attributes
- [x] Import Product class from classes.Product
- [x] Create Clothing class inheriting from Product
- [x] Implement constructor that calls super().__init__() and adds `_size` and `_material` attributes
- [x] Create property getters and setters for size and material with validation
- [x] For size, validate against standard sizes: ["XS", "S", "M", "L", "XL", "XXL"]
- [x] Override `get_product_type()` method to return "Clothing" (FIX: add 'self' parameter) - IMPLEMENTED but not properly marked as done
- [x] Override `__repr__()` method to include size and material information
- [ ] Add any clothing-specific methods if needed
  Step-by-step:
  1. Open source/products/Clothing.py
  2. Consider adding methods that are specific to clothing products:
     ```
     def is_size_available(self, size):
         """Check if a specific size is available in stock"""
         return size in Clothing.clothing_sizes and self._size == size and self._quantity > 0

     def get_material_care_instructions(self):
         """Get care instructions based on the material"""
         care_instructions = {
             "cotton": "Machine wash cold, tumble dry low",
             "silk": "Dry clean only",
             "leather": "Professional leather cleaning recommended",
             "linen": "Machine wash cold, line dry",
             "wool": "Hand wash cold or dry clean",
             "hemp": "Machine wash cold, tumble dry low"
         }
         return care_instructions.get(self._material.lower(), "Check care label")
     ```
  3. Add any other relevant methods for clothing
  4. Save the file
- [ ] Add comprehensive docstrings to all methods

## 7. Implement Food class in source/products/Food.py inheriting from Product with expiry date functionality
- [x] Import Product class from classes.Product and datetime module
- [x] Create Food class inheriting from Product
- [x] Implement constructor that calls super().__init__() and adds `_expiry_date` attribute
- [x] Create property getter and setter for expiry_date with validation (not in the past)
- [x] Implement `is_expired()` method to check if product is expired
- [x] Override `get_product_type()` method to return "Food" (FIX: add 'self' parameter) - IMPLEMENTED but not properly marked as done
- [x] Override `__repr__()` method to include expiry date information
- [ ] Add any food-specific methods if needed
  Step-by-step:
  1. Open source/products/Food.py
  2. Consider adding methods that are specific to food products:
     ```
     def days_until_expiry(self):
         """Get the number of days until the food expires"""
         import datetime
         today = datetime.date.today()
         days = (self._expiry_date - today).days
         return days

     def is_safe_to_consume(self):
         """Check if the food is safe to consume (not expired and not close to expiry)"""
         days_to_expiry = self.days_until_expiry()
         # Consider food unsafe if it expires in 2 days or less
         return days_to_expiry > 2
     ```
  3. Add any other relevant methods for food products
  4. Save the file
- [ ] Add comprehensive docstrings to all methods

## 8. Add abstract base class functionality to Product class with abstract methods
- [ ] Import ABC and abstractmethod from abc module (add `from abc import ABC, abstractmethod` to Product.py)
  Step-by-step:
  1. Open source/classes/Product.py
  2. Add `from abc import ABC, abstractmethod` at the top of the file after the existing import
  3. Save the file

- [ ] Make Product class inherit from ABC (change `class Product():` to `class Product(ABC):`)
  Step-by-step:
  1. Open source/classes/Product.py
  2. Locate the class definition `class Product():`
  3. Change it to `class Product(ABC):`
  4. Save the file

- [ ] Create abstract method `get_product_type()` that must be implemented by subclasses (add `@abstractmethod` decorator to the method after first fixing the method signature to include `self` parameter)
  Step-by-step:
  1. First ensure the get_product_type method has the correct signature: `def get_product_type(self):`
  2. Add the `@abstractmethod` decorator just before the method definition
  3. The method should look like:
     ```
     @abstractmethod
     def get_product_type(self):
         """Get the product type - must be implemented by subclasses"""
         pass
     ```

- [ ] Ensure all product subclasses (Electronics, Clothing, Food) implement the abstract method correctly (with 'self' parameter)
  Step-by-step:
  1. Open source/products/Electronics.py and verify get_product_type method has 'self' parameter
  2. Open source/products/Clothing.py and verify get_product_type method has 'self' parameter
  3. Open source/products/Food.py and verify get_product_type method has 'self' parameter
  4. All should have signature `def get_product_type(self):`

- [ ] Test that the abstract base class functionality works correctly
  Step-by-step:
  1. Create a test script to verify that you can't instantiate the Product class directly
  2. Verify that subclasses like Electronics, Clothing, and Food can still be instantiated
  3. Test that removing get_product_type from a subclass causes an error

## 9. Add class methods and static methods to all classes for data management
- [ ] In Product class: Add class method `from_dict()` to create product from dictionary
  Step-by-step:
  1. Open source/classes/Product.py
  2. Add a new class method after the constructor:
     ```
     @classmethod
     def from_dict(cls, data):
         """
         Create a Product instance from a dictionary
         :param data: Dictionary containing product information
         :return: Product instance
         """
         return cls(
             name=data.get('name', ''),
             price=data.get('price', 0.0),
             quantity=data.get('quantity', 1)
         )
     ```

- [ ] In Product class: Add static method to validate product data
  Step-by-step:
  1. Open source/classes/Product.py
  2. Add a new static method:
     ```
     @staticmethod
     def validate_product_data(name, price, quantity):
         """
         Validate product data before creation
         :param name: Product name
         :param price: Product price
         :param quantity: Product quantity
         :return: Boolean indicating if data is valid
         """
         if not name or len(name.strip()) == 0:
             return False
         if price < 0:
             return False
         if quantity < 0:
             return False
         return True
     ```

- [ ] In Inventory class: Add class method `load_from_csv()` to load inventory from CSV
  Step-by-step:
  1. Open source/classes/Inventory.py
  2. Add a new class method:
     ```
     @classmethod
     def load_from_csv(cls, csv_file_path):
         """
         Load inventory from a CSV file
         :param csv_file_path: Path to the CSV file
         :return: Inventory instance with products loaded from CSV
         """
         import csv
         inventory = cls()
         with open(csv_file_path, 'r', newline='') as csvfile:
             reader = csv.DictReader(csvfile)
             for row in reader:
                 # Determine product type and create appropriate product
                 product_type = row.get('type', 'Product')
                 name = row['name']
                 price = float(row['price'])
                 quantity = int(row['quantity'])

                 if product_type == 'Electronics':
                     warranty = int(row.get('warranty_months', 0))
                     product = Electronics(name, price, quantity, warranty)
                 elif product_type == 'Clothing':
                     size = row.get('size', '')
                     material = row.get('material', '')
                     product = Clothing(name, price, quantity, size, material)
                 elif product_type == 'Food':
                     expiry = datetime.datetime.strptime(row.get('expiry_date', ''), '%Y-%m-%d').date()
                     product = Food(name, price, quantity, expiry)
                 else:
                     # Create base Product for unknown types
                     from .Product import Product
                     product = Product(name, price, quantity)

                 inventory.add_product(product)
         return inventory
     ```

- [ ] In Inventory class: Add static method to calculate total inventory value
  Step-by-step:
  1. Open source/classes/Inventory.py
  2. Locate the existing calculate_inventory_value static method (it already exists)
  3. No changes needed as this method already exists

- [ ] In Supplier class: Add class method to create supplier from data
  Step-by-step:
  1. Open source/classes/Supplier.py
  2. Add a new class method:
     ```
     @classmethod
     def from_dict(cls, data):
         """
         Create a Supplier instance from a dictionary
         :param data: Dictionary containing supplier information
         :return: Supplier instance
         """
         return cls(
             name=data.get('name', ''),
             contact_info=data.get('contact_info', '')
         )
     ```

- [ ] In Order class: Add class method to create order from data
  Step-by-step:
  1. Open source/classes/Order.py
  2. Add a new class method:
     ```
     @classmethod
     def from_dict(cls, data, inventory):
         """
         Create an Order instance from a dictionary
         :param data: Dictionary containing order information
         :param inventory: Inventory instance to get products from
         :return: Order instance
         """
         order = cls(data.get('order_type', 'Purchase'))
         items_data = data.get('items', [])
         for item_data in items_data:
             product_id = item_data['product_id']
             quantity = item_data['quantity']
             product = inventory.find_product_by_id(product_id)
             if product:
                 order.add_item(product, quantity)
         return order
     ```

- [ ] Add appropriate static methods for data validation and processing across all classes
  Step-by-step:
  1. Add static methods to validate data in each class where appropriate
  2. For example, in Electronics, Clothing, and Food classes, add validation methods for their specific attributes

- [ ] Add class method `create_sample_inventory()` to Inventory class (already implemented but can be enhanced)
  Step-by-step:
  1. The method already exists in source/classes/Inventory.py
  2. Consider enhancing it to accept parameters for customization

## 10. Implement comprehensive error handling and validation in all classes
- [ ] Create custom exception classes for inventory management in a new file source/classes/exceptions.py:
  Step-by-step:
  1. Create a new file: source/classes/exceptions.py
  2. Add the following exception classes:
     ```
     class InsufficientStockError(Exception):
         """Raised when there is not enough stock for a requested operation"""
         pass

     class InvalidProductError(Exception):
         """Raised when a product is invalid or has invalid attributes"""
         pass

     class InvalidSupplierError(Exception):
         """Raised when a supplier is invalid or has invalid attributes"""
         pass

     class InvalidOrderError(Exception):
         """Raised when an order is invalid or has invalid attributes"""
         pass

     class ExpiredProductError(Exception):
         """Raised when an operation is attempted on an expired product"""
         pass
     ```

- [ ] Add try/except blocks where appropriate
  Step-by-step:
  1. In the Order.execute_order method, add try/except blocks around product stock operations
  2. In the Inventory.add_product method, add validation with appropriate exceptions
  3. In the Product class setters, replace ValueError with custom exceptions where appropriate

- [ ] Implement input validation in all setters and methods
  Step-by-step:
  1. Review all setter methods in Product, Inventory, Supplier, and Order classes
  2. Add validation checks with appropriate custom exceptions
  3. Ensure all methods validate their inputs before processing

- [ ] Add validation for product creation (name, price, quantity)
  Step-by-step:
  1. In the Product.__init__ method, add validation using the validate_product_data static method
  2. Raise appropriate custom exceptions if validation fails

- [ ] Add validation for order processing (sufficient stock for sales)
  Step-by-step:
  1. In the Order.add_item method, add validation to ensure sufficient stock for sales orders
  2. Raise InsufficientStockError if there's not enough stock
  3. In the Order.execute_order method, add validation to prevent removing more stock than available

- [ ] Add validation for supplier product associations
  Step-by-step:
  1. In the Supplier.add_product method, add validation to ensure the product is valid
  2. Raise InvalidProductError if the product is invalid

- [ ] Implement proper error messages for all validation failures
  Step-by-step:
  1. Update all exception raising code to include descriptive error messages
  2. Make error messages informative and actionable

- [ ] Add logging functionality to track operations
  Step-by-step:
  1. Add import logging at the top of each class file
  2. Create a logger instance in each class
  3. Add logging calls for important operations like adding products, executing orders, etc.

## 11. Create product management functionality in Inventory class (already partially listed in task #2)
- [x] Implement `find_product_by_name()` method for searching products (method already exists in Inventory class)
- [x] Create `update_product()` method to modify existing products (method already exists in Inventory class)
- [x] Add `get_product_count()` method to return total number of products (method exists as product_count in Inventory class)
- [x] Implement `get_total_value()` method to calculate inventory value (method exists as static method calculate_inventory_value in Inventory class)
- [x] Create `get_low_stock_products()` method to identify products with low stock (method exists as low_stock_products in Inventory class)
- [x] Add filtering methods to get products by type or other criteria (methods like find_product_by_type, find_product_by_price, etc. already exist in Inventory class)

## 12. Implement inventory tracking and management features (already partially listed in task #2)
- [ ] Add inventory history/transaction tracking
- [ ] Implement stock level monitoring with configurable thresholds
- [ ] Create methods to track product movement (additions, removals)
- [ ] Add inventory audit functionality
- [ ] Implement inventory reports (by type, value, stock levels)
- [ ] Add methods to handle inventory adjustments and corrections

## 13. Build supplier and vendor management system (already partially listed in task #2)
- [ ] Implement methods to manage multiple suppliers
- [ ] Create functionality to associate products with suppliers
- [ ] Add supplier performance tracking (delivery times, quality, etc.)
- [ ] Implement supplier search and filtering methods
- [ ] Add methods to track supplier orders and deliveries
- [ ] Create supplier contact management features

## 14. Develop sales and purchase order processing (already partially listed in task #4)
- [ ] Enhance Order class with more detailed order information
- [ ] Implement order status tracking (pending, processed, cancelled)
- [ ] Create methods to handle partial order fulfillment
- [ ] Add order history and tracking functionality
- [ ] Implement order validation and approval workflows
- [ ] Add methods to generate purchase orders for low-stock items

## 15. Add reporting and analytics features to Inventory class
- [x] Create `generate_inventory_report()` method with formatted output (already implemented)
- [ ] Implement sales/purchase analytics and reporting
  Step-by-step:
  1. Open source/classes/Inventory.py
  2. Add methods to analyze sales and purchase data:
     ```
     def get_sales_report(self, start_date=None, end_date=None):
         """
         Generate a sales report for a given period
         :param start_date: Start date for the report (optional)
         :param end_date: End date for the report (optional)
         :return: Dictionary with sales information
         """
         # This would require tracking sales transactions
         # For now, we'll return a basic report based on current inventory changes
         sales_data = {}
         for product in self._products.values():
             # Calculate sales based on quantity difference from initial stock
             # This is a simplified approach - in a real system, you'd track actual sales
             pass
         return sales_data

     def get_purchase_report(self, start_date=None, end_date=None):
         """
         Generate a purchase report for a given period
         :param start_date: Start date for the report (optional)
         :param end_date: End date for the report (optional)
         :return: Dictionary with purchase information
         """
         # Similar to sales report but for purchases
         purchase_data = {}
         return purchase_data

     def get_top_moving_products(self, limit=5):
         """
         Get the top moving products based on sales velocity
         :param limit: Number of products to return
         :return: List of top moving products
         """
         # This would require tracking sales history
         # For now, return products with highest quantity sold
         pass
     ```
  3. Add methods to calculate various analytics:
     ```
     def calculate_sales_velocity(self, product_id, days=30):
         """
         Calculate the sales velocity for a product (items sold per day)
         :param product_id: ID of the product
         :param days: Number of days to calculate velocity for
         :return: Sales velocity (items per day)
         """
         # This would require historical sales data
         pass
     ```
  4. Save the file
- [ ] Add inventory turnover rate calculations
  Step-by-step:
  1. Open source/classes/Inventory.py
  2. Add a method to calculate inventory turnover rate:
     ```
     def calculate_inventory_turnover_rate(self, product_id=None, period_days=365):
         """
         Calculate the inventory turnover rate for a product or entire inventory
         :param product_id: ID of the product (if None, calculates for entire inventory)
         :param period_days: Number of days for the calculation period (default 365 for annual)
         :return: Turnover rate as a float
         """
         import datetime
         # Calculate the cost of goods sold (COGS) for the period
         # For simplicity, we'll use average inventory value
         if product_id:
             product = self._products.get(product_id)
             if not product:
                 return 0
             # Calculate average inventory for the product
             avg_inventory = product.quantity  # Simplified - would need historical data for real calculation
             # Calculate COGS for the product (would need sales data)
             # turnover_rate = COGS / avg_inventory
             # For now, return a placeholder calculation
             return 0
         else:
             # Calculate for entire inventory
             total_avg_inventory = sum(p.quantity * p.price for p in self._products.values())
             if total_avg_inventory == 0:
                 return 0
             # Calculate total COGS (would need sales data)
             # For now, return a placeholder
             return 0
     ```
  3. Add a method to get turnover analysis:
     ```
     def get_inventory_turnover_analysis(self):
         """
         Get a complete inventory turnover analysis
         :return: Dictionary with turnover analysis
         """
         analysis = {}
         for product_id, product in self._products.items():
             analysis[product_id] = {
                 'product_name': product.name,
                 'turnover_rate': self.calculate_inventory_turnover_rate(product_id),
                 'quantity': product.quantity
             }
         return analysis
     ```
  4. Save the file
- [ ] Create product performance reports
  Step-by-step:
  1. Open source/classes/Inventory.py
  2. Add a method to generate product performance reports:
     ```
     def generate_product_performance_report(self):
         """
         Generate a product performance report
         :return: String with formatted performance report
         """
         report = "=== PRODUCT PERFORMANCE REPORT ===\n"
         report += f"Total Products: {self.product_count()}\n\n"

         # Group products by type
         product_groups = self.product_groups()
         for product_type, products in product_groups.items():
             report += f"--- {product_type.upper()} ---\n"
             for product in products:
                 report += f"  {product.name}:\n"
                 report += f"    ID: {product.id}\n"
                 report += f"    Price: ${product.price:.2f}\n"
                 report += f"    Quantity: {product.quantity}\n"
                 report += f"    Value: ${product.calculate_value_of_stock():.2f}\n"
                 report += f"    Created: {product.created_at}\n"

                 # Add product-specific info
                 if hasattr(product, 'warranty_months'):
                     report += f"    Warranty: {product.warranty_months} months\n"
                 elif hasattr(product, 'size') and hasattr(product, 'material'):
                     report += f"    Size: {product.size}, Material: {product.material}\n"
                 elif hasattr(product, 'expiry_date'):
                     report += f"    Expiry: {product.expiry_date}\n"
                     if hasattr(product, 'is_expired') and product.is_expired():
                         report += f"    STATUS: EXPIRED\n"
                 report += "\n"

         return report
     ```
  3. Add a method to get top performing products:
     ```
     def get_top_performing_products(self, limit=5):
         """
         Get the top performing products based on value
         :param limit: Number of products to return
         :return: List of top performing products
         """
         sorted_products = sorted(
             self._products.values(),
             key=lambda p: p.calculate_value_of_stock(),
             reverse=True
         )
         return sorted_products[:limit]
     ```
  4. Save the file
- [ ] Add visual representation methods (text-based charts)
  Step-by-step:
  1. Open source/classes/Inventory.py
  2. Add a method to create a simple text-based bar chart for product quantities:
     ```
     def display_quantity_chart(self, max_width=50):
         """
         Display a text-based bar chart of product quantities
         :param max_width: Maximum width of the chart bars
         :return: String with the chart representation
         """
         chart = "=== INVENTORY QUANTITY CHART ===\n"
         max_quantity = max((p.quantity for p in self._products.values()), default=0)

         if max_quantity == 0:
             return chart + "No products in inventory\n"

         for product in self._products.values():
             bar_width = int((product.quantity / max_quantity) * max_width)
             bar = '█' * bar_width
             chart += f"{product.name[:20]:<20} |{bar:<50}| {product.quantity}\n"

         return chart
     ```
  3. Add a method to create a pie chart representation of inventory value by product type:
     ```
     def display_value_pie_chart(self):
         """
         Display a text-based representation of inventory value by product type
         :return: String with the pie chart representation
         """
         chart = "=== INVENTORY VALUE BY TYPE ===\n"

         # Calculate total value by type
         value_by_type = {}
         for product in self._products.values():
             product_type = product.get_product_type()
             value = product.calculate_value_of_stock()
             if product_type not in value_by_type:
                 value_by_type[product_type] = 0
             value_by_type[product_type] += value

         total_value = sum(value_by_type.values())
         if total_value == 0:
             return chart + "No value in inventory\n"

         for product_type, value in value_by_type.items():
             percentage = (value / total_value) * 100
             chart += f"{product_type:<15} |{'█' * int(percentage/2):<50}| {percentage:.1f}% (${value:.2f})\n"

         return chart
     ```
  4. Save the file
- [ ] Implement export functionality for reports (CSV, text)
  Step-by-step:
  1. Open source/classes/Inventory.py
  2. Add a method to export inventory data to CSV:
     ```
     def export_to_csv(self, filename="inventory_export.csv"):
         """
         Export inventory data to a CSV file
         :param filename: Name of the output CSV file
         """
         import csv
         with open(filename, 'w', newline='') as csvfile:
             fieldnames = ['id', 'name', 'price', 'quantity', 'product_type', 'additional_info']
             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

             writer.writeheader()
             for product in self._products.values():
                 row = {
                     'id': product.id,
                     'name': product.name,
                     'price': product.price,
                     'quantity': product.quantity,
                     'product_type': product.get_product_type(),
                     'additional_info': ''
                 }
                 # Add product-specific information
                 if hasattr(product, 'warranty_months'):
                     row['additional_info'] = f"Warranty: {product.warranty_months} months"
                 elif hasattr(product, 'size') and hasattr(product, 'material'):
                     row['additional_info'] = f"Size: {product.size}, Material: {product.material}"
                 elif hasattr(product, 'expiry_date'):
                     row['additional_info'] = f"Expiry: {product.expiry_date}"
                 writer.writerow(row)
     ```
  3. Add a method to export reports to text file:
     ```
     def export_report_to_text(self, report_content, filename="inventory_report.txt"):
         """
         Export a report to a text file
         :param report_content: Content of the report to export
         :param filename: Name of the output text file
         """
         with open(filename, 'w') as file:
             file.write(report_content)
     ```
  4. Add a method to export detailed inventory report:
     ```
     def export_detailed_report(self, filename="detailed_inventory_report.txt"):
         """
         Export a detailed inventory report to a text file
         :param filename: Name of the output text file
         """
         report = self.generate_inventory_report()
         self.export_report_to_text(report, filename)
     ```
  5. Save the file
- [x] Add inventory analytics methods (turnover rates, performance metrics) - methods like product_groups, low_stock_products already exist

## 16. Write documentation and usage examples
- [ ] Add comprehensive docstrings to all classes and methods (add docstrings to all methods in Product, Inventory, Supplier, Order, Electronics, Clothing, and Food classes)
  Step-by-step:
  1. Open source/classes/Product.py
  2. Add docstrings to the class and all methods:
     - Add a class docstring at the top of the class
     - Add docstrings to __init__, all property getters and setters, add_stock, remove_stock, calculate_value_of_stock, get_product_type, and __repr__ methods
  3. Open source/classes/Inventory.py
  4. Add docstrings to the class and all methods:
     - Add a class docstring at the top of the class
     - Add docstrings to __init__, all property getters, calculate_inventory_value, create_sample_inventory, add_product, remove_product, find_product_by_id, find_product_by_name, find_product_by_type, find_product_by_price, find_product_by_quantity, find_product_by_date, list_product, product_count, low_stock_products, product_groups, generate_inventory_report, textify, get_expired_products, transaction_history, and any new methods
  5. Open source/classes/Supplier.py
  6. Add docstrings to the class and all methods:
     - Add a class docstring at the top of the class
     - Add docstrings to __init__, all property getters and setters, add_product, remove_product, get_supplied_products, and __repr__ methods
  7. Open source/classes/Order.py
  8. Add docstrings to the class and all methods:
     - Add a class docstring at the top of the class
     - Add docstrings to __init__, all property getters, add_item, remove_item, _calculate_total, execute_order, and __repr__ methods
  9. Open source/products/Electronics.py
  10. Add docstrings to the class and all methods:
     - Add a class docstring at the top of the class
     - Add docstrings to __init__, all property getters and setters, get_product_type, __repr__, and any new methods
  11. Open source/products/Clothing.py
  12. Add docstrings to the class and all methods:
     - Add a class docstring at the top of the class
     - Add docstrings to __init__, all property getters and setters, get_product_type, __repr__, and any new methods
  13. Open source/products/Food.py
  14. Add docstrings to the class and all methods:
     - Add a class docstring at the top of the class
     - Add docstrings to __init__, all property getters and setters, is_expired, get_product_type, __repr__, and any new methods
  15. Save all files
- [ ] Create README.md with project overview and setup instructions
- [ ] Write usage examples demonstrating all OOP concepts
- [ ] Document the class hierarchy and relationships
- [ ] Create API documentation for all public methods
- [ ] Add code comments explaining complex logic
- [ ] Update docstrings to follow Python documentation standards

## 17. Create unit tests demonstrating OOP concepts
- [ ] Create test files for each class (test_Product.py, test_Inventory.py, etc.)
- [ ] Write tests for encapsulation (private attributes, property validation)
- [ ] Write tests for inheritance (subclass behavior, method overriding)
- [ ] Write tests for polymorphism (different behavior by product type)
- [ ] Write tests for abstraction (abstract base class functionality)
- [ ] Test error handling and validation scenarios
- [ ] Test all class methods and static methods
- [ ] Write integration tests for the complete system
- [ ] Test order processing functionality
- [ ] Test inventory management operations
- [ ] Test supplier management functionality

## 18. Update run.py to demonstrate the complete system functionality
- [x] Create main function that demonstrates all system features (already implemented)
- [x] Show creation of different product types (Electronics, Clothing, Food)
- [x] Demonstrate inventory management operations
- [x] Show supplier management functionality
- [x] Demonstrate order processing (both purchase and sales)
- [x] Display reports and analytics
- [x] Include examples of all OOP concepts in action
- [x] Add user interaction options for manual testing
- [ ] Add more comprehensive examples showing all features (add examples for all filtering methods like find_product_by_type, find_product_by_price, etc.)
  Step-by-step:
  1. Open source/run.py
  2. Add examples for all filtering methods in the main function:
     ```
     # Additional filtering examples
     print("\n=== FILTERING EXAMPLES ===")
     print("Products by type (Electronics):")
     electronics = inventory.find_product_by_type("Electronics")
     for e in electronics:
         print(f"  - {e}")

     print("\nProducts by price range ($10-$100):")
     price_filtered = inventory.find_product_by_price(10, 100)
     for p in price_filtered:
         print(f"  - {p}")

     print("\nProducts by quantity range (5-50):")
     quantity_filtered = inventory.find_product_by_quantity(5, 50)
     for q in quantity_filtered:
         print(f"  - {q}")

     print("\nProducts by creation date (last 10 days):")
     import datetime
     date_filtered = inventory.find_product_by_date(
         datetime.datetime.now() - datetime.timedelta(days=10),
         datetime.datetime.now()
     )
     for d in date_filtered:
         print(f"  - {d}")
     ```
  3. Add examples for supplier search and filtering:
     ```
     # Supplier examples
     print("\n=== SUPPLIER EXAMPLES ===")
     supplier_list = inventory.get_all_suppliers()
     print(f"Total suppliers: {len(supplier_list)}")

     supplier_by_name = inventory.find_supplier_by_name("Tech Supplies Inc.")
     if supplier_by_name:
         print(f"Found supplier: {supplier_by_name}")
     ```
  4. Add examples for order validation and approval:
     ```
     # Order validation and approval examples
     print("\n=== ORDER VALIDATION EXAMPLES ===")
     test_order = inventory.create_order("Sale")
     if smartphone.quantity > 0:  # Only add item if available
         test_order.add_item(smartphone, 1)

     is_valid = test_order.validate_order()
     print(f"Is order valid? {is_valid}")

     # Approve the order
     test_order.approve("Manager")
     print(f"Order approved by: {test_order._approver}")
     ```
  5. Add examples for inventory adjustment:
     ```
     # Inventory adjustment examples
     print("\n=== INVENTORY ADJUSTMENT EXAMPLES ===")
     initial_qty = smartphone.quantity
     inventory.adjust_inventory(smartphone.id, -2, "Test adjustment")
     print(f"Adjusted smartphone quantity from {initial_qty} to {smartphone.quantity}")

     # Correct the inventory back
     inventory.correct_inventory(smartphone.id, initial_qty, "Revert test adjustment")
     print(f"Corrected smartphone quantity back to {smartphone.quantity}")
     ```
  6. Save the file
- [ ] Add error handling examples in the demo (add try/catch blocks to demonstrate what happens when invalid operations are attempted)
  Step-by-step:
  1. Open source/run.py
  2. Add error handling examples in the main function:
     ```
     # Error handling examples
     print("\n=== ERROR HANDLING EXAMPLES ===")

     # Example 1: Attempt to set negative price
     try:
         smartphone.price = -50
     except ValueError as e:
         print(f"Error setting negative price: {e}")

     # Example 2: Attempt to set empty name
     try:
         smartphone.name = ""
     except ValueError as e:
         print(f"Error setting empty name: {e}")

     # Example 3: Attempt to remove more stock than available
     original_qty = smartphone.quantity
     try:
         result = smartphone.remove_stock(original_qty + 10)
         if not result:
             print(f"Could not remove {original_qty + 10} items, only {original_qty} available")
     except ValueError as e:
         print(f"Error removing too much stock: {e}")

     # Example 4: Attempt to add negative stock
     try:
         smartphone.add_stock(-5)
     except ValueError as e:
         print(f"Error adding negative stock: {e}")

     # Example 5: Attempt to create order with invalid type
     try:
         invalid_order = inventory.create_order("InvalidType")
     except ValueError as e:
         print(f"Error creating order with invalid type: {e}")
     ```
  3. Add examples for order processing errors:
     ```
     # Order processing error examples
     print("\n=== ORDER PROCESSING ERROR EXAMPLES ===")
     large_order = inventory.create_order("Sale")

     # Try to order more than available stock
     if smartphone.quantity > 0:
         try:
             large_order.add_item(smartphone, smartphone.quantity + 100)
             large_order.execute_order()
         except ValueError as e:
             print(f"Error executing order with insufficient stock: {e}")
     ```
  4. Save the file
- [ ] Add examples of custom exceptions in action (once custom exceptions are created, demonstrate them in run.py)

## 19. Code Quality and Performance Improvements
- [ ] Add comprehensive type hints throughout the codebase
  Step-by-step:
  1. Open source/classes/Product.py
  2. Add type hints to all method parameters and return values:
     - Add import typing at the top if needed for complex types
     - Add type hints to __init__ method parameters and return type
     - Add type hints to all property getters and setters
     - Add type hints to all method parameters and return types
  3. Open source/classes/Inventory.py
  4. Add type hints to all method parameters and return values:
     - Add import typing at the top if needed for complex types
     - Add type hints to __init__ method parameters and return type
     - Add type hints to all property getters
     - Add type hints to all method parameters and return types
  5. Open source/classes/Supplier.py
  6. Add type hints to all method parameters and return values:
     - Add import typing at the top if needed for complex types
     - Add type hints to __init__ method parameters and return type
     - Add type hints to all property getters and setters
     - Add type hints to all method parameters and return types
  7. Open source/classes/Order.py
  8. Add type hints to all method parameters and return values:
     - Add import typing at the top if needed for complex types
     - Add type hints to __init__ method parameters and return type
     - Add type hints to all property getters
     - Add type hints to all method parameters and return types
  9. Open source/products/Electronics.py
  10. Add type hints to all method parameters and return values:
     - Add import typing at the top if needed for complex types
     - Add type hints to __init__ method parameters and return type
     - Add type hints to all property getters and setters
     - Add type hints to all method parameters and return types
  11. Open source/products/Clothing.py
  12. Add type hints to all method parameters and return values:
     - Add import typing at the top if needed for complex types
     - Add type hints to __init__ method parameters and return type
     - Add type hints to all property getters and setters
     - Add type hints to all method parameters and return types
  13. Open source/products/Food.py
  14. Add type hints to all method parameters and return values:
     - Add import typing at the top if needed for complex types
     - Add type hints to __init__ method parameters and return type
     - Add type hints to all property getters and setters
     - Add type hints to all method parameters and return types
  15. Save all files
- [ ] Implement proper exception handling throughout the codebase
- [ ] Add logging functionality to track operations
- [ ] Optimize data structures for faster lookups
- [ ] Add caching for frequently accessed data
- [ ] Implement lazy loading for large inventories
- [ ] Add data persistence using JSON, CSV, or SQLite
- [ ] Implement methods to save and load inventory data

## 20. Advanced Features and Design Patterns
- [ ] Consider implementing the Observer pattern for inventory change notifications
- [ ] Use the Factory pattern for creating different product types
- [ ] Implement the Strategy pattern for different pricing strategies
- [ ] Add search and filtering capabilities
- [ ] Implement inventory alerts for low stock
- [ ] Add more detailed reporting features
- [ ] Implement user authentication if needed for a multi-user system
- [ ] Create a clean API layer for the inventory system
- [ ] Add RESTful endpoints if converting to a web service
- [ ] Implement proper request/response handling
