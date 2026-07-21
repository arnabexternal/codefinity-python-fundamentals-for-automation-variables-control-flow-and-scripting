produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

for items in groceries:
    for item in items:
        print(f'Item name: {item}')