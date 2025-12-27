# OOP Inventory Management System

A comprehensive inventory management system built in Python that demonstrates advanced Object-Oriented Programming (OOP) concepts. This project showcases all core OOP principles including encapsulation, inheritance, polymorphism, and abstraction in a practical, real-world application.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [OOP Concepts Demonstrated](#oop-concepts-demonstrated)
- [Installation](#installation)
- [Usage](#usage)
- [Classes Overview](#classes-overview)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Product Management**: Create and manage different product types with validation
- **Inventory Tracking**: Monitor stock levels and calculate inventory value
- **Supplier Management**: Associate suppliers with products
- **Order Processing**: Handle both purchase and sales orders
- **Reporting**: Generate inventory reports with low stock alerts
- **Data Validation**: Comprehensive input validation with error handling
- **Polymorphic Behavior**: Different product types with specialized functionality

## Project Structure

```
OOPTest/
├── documentation/
│   ├── comprehensive_oop_solution.py    # Complete implementation example
│   ├── job_description.txt              # Project requirements
│   └── tasklist.md                      # Development task list
└── source/
    ├── classes/
    │   ├── __init__.py
    │   ├── Inventory.py                 # Inventory management class
    │   ├── Order.py                     # Order processing class
    │   ├── Product.py                   # Base Product class
    │   └── Supplier.py                  # Supplier management class
    ├── products/
    │   ├── __init__.py
    │   ├── Clothing.py                  # Clothing product type
    │   ├── Electronics.py               # Electronics product type
    │   └── Food.py                      # Food product type
    ├── items.csv                        # Sample product data
    └── run.py                           # Main application entry point
```

## OOP Concepts Demonstrated

### Encapsulation
- Private attributes using underscore prefix (`_id`, `_name`, `_price`, etc.)
- Property decorators for controlled access with validation
- Getter and setter methods with input validation

### Inheritance
- Base `Product` class with common functionality
- Specialized product classes inheriting and extending base functionality
- Proper use of `super()` to call parent class methods

### Polymorphism
- Abstract `get_product_type()` method implemented differently by each product type
- Common interfaces with type-specific behavior

### Abstraction
- Abstract base class using `ABC` and `@abstractmethod`
- Common interface definition without implementation details

## Installation

1. Clone the repository:
```bash
git clone https://github.com/huma8/InventoryManagerOOP.git
```

2. Navigate to the project directory:
```bash
cd InventoryManagerOOP
```

3. The project uses only Python standard library modules, so no additional installation is required.

## Usage

### Running the Example

To run the example implementation:

```bash
cd source
python run.py
```

### Basic Usage

```python
from classes.Product import Product
from products.Electronics import Electronics
from products.Clothing import Clothing
from products.Food import Food

# Create different product types
laptop = Electronics("Laptop", 999.99, 10, 24)  # 24 months warranty
shirt = Clothing("T-Shirt", 19.99, 50, "M", "Cotton")
milk = Food("Milk", 3.99, 20, "2023-12-31")  # Expiry date

# Create an inventory
from classes.Inventory import Inventory
inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(shirt)
inventory.add_product(milk)

# Manage inventory
laptop.add_stock(5)
shirt.remove_stock(3)

# Process orders
from classes.Order import Order
order = Order("Sale")
order.add_item(laptop, 2)
order.execute_order(inventory)
```

## Classes Overview

### Product Classes
- **Product**: Abstract base class with common functionality
- **Electronics**: Inherits from Product, adds warranty information
- **Clothing**: Inherits from Product, adds size and material properties
- **Food**: Inherits from Product, adds expiry date and expiration checking

### Management Classes
- **Inventory**: Central hub for managing all inventory operations
- **Order**: Handles purchase and sales orders with item management
- **Supplier**: Manages supplier information and associated products

## Examples

### Creating Products

```python
from products.Electronics import Electronics
from products.Clothing import Clothing
from products.Food import Food

# Create electronics product
phone = Electronics("Smartphone", 699.99, 15, 12)  # 12 months warranty

# Create clothing product
jeans = Clothing("Jeans", 79.99, 25, "32", "Denim")

# Create food product
bread = Food("Bread", 2.49, 30, "2023-12-28")  # Expiry date
```

### Managing Inventory

```python
from classes.Inventory import Inventory

inventory = Inventory()

# Add products to inventory
inventory.add_product(phone)
inventory.add_product(jeans)
inventory.add_product(bread)

# Check inventory
print(f"Total products: {inventory.get_product_count()}")
print(f"Total inventory value: ${inventory.get_total_value():.2f}")

# Find low stock products
low_stock = inventory.get_low_stock_products(threshold=10)
print(f"Low stock products: {low_stock}")
```

### Processing Orders

```python
from classes.Order import Order

# Create a sales order
sales_order = Order("Sale")
sales_order.add_item(phone, 2)
sales_order.add_item(jeans, 1)

# Execute the order (updates inventory)
sales_order.execute_order(inventory)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

[Mail](egocak8@gmail.com)

---

This project serves as an excellent example of Python OOP best practices and can be used as a foundation for more complex inventory management systems.