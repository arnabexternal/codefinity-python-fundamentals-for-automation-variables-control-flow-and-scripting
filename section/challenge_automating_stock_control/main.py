# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}
discount_threshold = 100
 
print("Processing started")
 
# Go through each item in the inventory
for item, details in inventory.items():
    current_stock, min_stock, restock_qty, on_sale = details
 
    # Restock until stock is at or above the minimum
    while current_stock < min_stock:
        current_stock += restock_qty
 
    # Update the stock value in the dictionary
    inventory[item][0] = current_stock
 
    # Apply discount if stock exceeds threshold and item is not on sale
    if current_stock > discount_threshold and not on_sale:
        inventory[item][3] = True
 
    print(f"Processing {item}")
 
print("Processing completed")
 