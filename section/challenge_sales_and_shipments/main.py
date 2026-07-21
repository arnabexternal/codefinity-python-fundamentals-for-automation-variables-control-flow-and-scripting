# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]
new_product_list = []
dummy_value = ''

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

print(dict(products))
print(dict(units_sold))
print(dict(shipment_received))

dict_product = dict(products)
dict_units_sold = dict(units_sold)
dict_shipment_received = dict(shipment_received)

for items in range(len(products)):
    for item in range(len(products[items])):
        dummy_value == ''

for items in dict_product.keys():
    dict_product[items] = dict_product.get(items) - dict_units_sold.get(items) + dict_shipment_received.get(items)
    new_product = [items,dict_product[items]]
    new_product_list.append(new_product)
    
products = new_product_list
print(f'Final stock levels for all products: {products}')