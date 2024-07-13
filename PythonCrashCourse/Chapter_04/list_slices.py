pizzas = ["Pepperoni - Mushroom - Black Olive", "Hawaiian", "Pepperoni - Green Olive", "Supreme", "Hillbilly", "Fireman", "Cheese"]

print(pizzas[:3])
print(f"Pizzas in the middle of the list are {pizzas[2:5]}")
print(f"The last three items in the list are {pizzas[-3:]}")

friends_pizzas = pizzas[:]
pizzas.append("Margherita")
friends_pizzas.append("Cookie Dough")

print(f"My last pizza items are: {pizzas[-3:]}")
print(f"My friend's last pizza items are: {friends_pizzas[-3:]}")