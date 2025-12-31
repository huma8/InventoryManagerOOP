from classes.Inventory import Inventory
from classes.Supplier import Supplier
from products.Electronics import Electronics
from products.Clothing import Clothing
from products.Food import Food
import datetime

def main():
    """
    Main function demonstrating the inventory management system
    """
    print("=== INVENTORY MANAGEMENT SYSTEM ===\n")

    # Create inventory manager
    inventory = Inventory.create_sample_inventory()

    # Add more products of different types
    smartphone = Electronics("Smartphone", 699.99, 10, 12)
    jeans = Clothing("Denim Jeans", 49.99, 25, "L", "Denim")
    bread = Food("Whole Wheat Bread", 3.49, 15, datetime.date.today() + datetime.timedelta(days=3))

    inventory.add_product(smartphone)
    inventory.add_product(jeans)
    inventory.add_product(bread)

    print("1. Initial Inventory:")
    print(inventory.generate_inventory_report())

    # Demonstrate polymorphism - different product types behave differently
    print("2. Polymorphism - Different Product Types:")
    for product in inventory.products.values():
        print(f"  {product} - Type: {product.get_product_type()}")

    # Create a supplier and associate with products
    print("\n3. Supplier Management:")
    supplier = Supplier("Tech Supplies Inc.", "contact@techsupplies.com")
    supplier.add_product(smartphone)
    laptop = inventory.get_product(1)  # Get the laptop from the sample inventory
    if laptop:
        supplier.add_product(laptop)
    inventory.add_supplier(supplier)

    print(f"Supplier: {supplier}")
    print(f"Products supplied: {[p.name for p in supplier.get_supplied_products()]}")

    # Create and execute orders
    print("\n4. Order Processing:")

    # Purchase order
    purchase_order = inventory.create_order("Purchase")
    purchase_order.add_item(smartphone, 5)
    purchase_order.add_item(jeans, 10)
    print(f"Created purchase order: {purchase_order}")

    # Execute the purchase order
    purchase_order.execute_order()
    print(f"Executed purchase order. New smartphone stock: {smartphone.quantity}")

    # Sale order
    sale_order = inventory.create_order("Sale")
    sale_order.add_item(smartphone, 3)
    sale_order.add_item(jeans, 2)
    print(f"\nCreated sale order: {sale_order}")

    # Execute the sale order
    sale_order.execute_order()
    print(f"Executed sale order. New smartphone stock: {smartphone.quantity}")

    # Show updated inventory
    print(f"\n5. Updated Inventory Report:")
    print(inventory.generate_inventory_report())

    # Demonstrate encapsulation with property setters
    print("\n6. Encapsulation - Property Setters:")
    try:
        smartphone.name = "Updated Smartphone Name"
        print(f"Updated product name: {smartphone.name}")

        # This will raise an error due to validation
        smartphone.price = -100
    except ValueError as e:
        print(f"Error setting price: {e}")

    # Demonstrate static method
    print(f"\n7. Static Method - Inventory Value:")
    total_value = Inventory.calculate_inventory_value(list(inventory.products.values()))
    print(f"Total inventory value: ${total_value:.2f}")

    # Demonstrate class method
    print(f"\n8. Class Method - Creating Sample Inventory:")
    new_inventory = Inventory.create_sample_inventory()
    print(f"New sample inventory has {len(new_inventory.products)} products")

if __name__ == "__main__":
    main()