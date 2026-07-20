# 1. Create the Dictionary
grocery_inventory = {
    "Milk":   ("Dairy",   3.50,  8),
    "Eggs":   ("Dairy",   5.50, 30),
    "Bread":  ("Bakery",  2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# 2. Check and Update Price
egg_price = grocery_inventory["Eggs"][1]
if egg_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (
        grocery_inventory["Eggs"][0],
        grocery_inventory["Eggs"][1] - 1,
        grocery_inventory["Eggs"][2]
    )
else:
    print("The price of Eggs is reasonable.")

# 3. Add a New Item
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

# 4. Manage Stock
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        grocery_inventory["Milk"][2] + 20
    )
else:
    print("Milk has sufficient stock.")

# 5. Remove Item Based on Price
if grocery_inventory["Apples"][1] > 2:
    del grocery_inventory["Apples"]
    print("Apples removed from inventory due to high price.")

# 6. Final Print
print("Updated inventory:", grocery_inventory)