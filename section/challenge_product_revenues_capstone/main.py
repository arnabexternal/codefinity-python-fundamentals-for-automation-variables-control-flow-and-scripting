# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
 
 
def calculate_revenue(prices, quantities_sold):
    revenues = []
    for price, quantity in zip(prices, quantities_sold):
        revenues.append(price * quantity)
    return revenues
 
 
def formatted_output(revenues):
    sorted_revenues = sorted(revenues)
    for revenue in sorted_revenues:
        print(f"{revenue[0]} has total revenue of ${revenue[1]}")
 
 
# Calculate revenue for each product
revenue = calculate_revenue(prices, quantities_sold)
 
# Combine products and revenue into a list of tuples
revenue_per_product = list(zip(products, revenue))
 
# Sort alphabetically by product name and print
formatted_output(revenue_per_product)
 