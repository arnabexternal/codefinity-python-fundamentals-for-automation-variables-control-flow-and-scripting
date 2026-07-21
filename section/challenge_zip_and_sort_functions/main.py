
# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]
# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]
# List of quantity sold
quantities_sold = [50, 100, 25, 40]
 
# Combine the three lists into a list of tuples
combined_list = list(zip(products, prices, quantities_sold))
 
# Sort by product name in ascending order
sorted_products = sorted(combined_list)
 
# Display each product
for product_name, product_price, quantity_sold in sorted_products:
    print(f"Product: {product_name}, Price: {product_price}, Quantity Sold: {quantity_sold}")