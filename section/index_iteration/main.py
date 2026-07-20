discount_dict = {
    0 : 0.9,
    1 : 0.8,
    2 : 0.85,
    3 : 0.95,
}
prices = [29.99, 45.50, 12.75, 38.20]

item_index = 0
for item_index in range(0, len(prices)):
    prices[item_index] = prices[item_index] * discount_dict.get(item_index)
    print(f'Updated price for item {item_index}: ${prices[item_index]:.2f}')