inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}
for x in inventory:
    print("Item: ", end = "")
    print(x + ", Quantity: " + str(inventory[x][0]) + ", Price: $" + str(inventory[x][1]))
print("Adding a new item: mango")
inventory["mango"] = (15, 3.0)
print("Updated inventory")
for x in inventory:
    print("Item: ", end = "")
    print(x + ", Quantity: " + str(inventory[x][0]) + ", Price: $" + str(inventory[x][1]))
print("Removing banana")
del inventory["banana"]
print("Changing price of apples.")
inventory["apple"] = (10, 3.0)
print("Updated inventory")
sum = 0
for x in inventory:
    print("Item: ", end = "")
    print(x + ", Quantity: " + str(inventory[x][0]) + ", Price: $" + str(inventory[x][1]))
    sum = sum + (inventory[x][0] * inventory[x][1])
print("Total value of inventory: $" + str(sum))