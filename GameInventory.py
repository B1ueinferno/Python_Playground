
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby', 'ruby', 'ruby', 'ruby', 'ruby', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print("{}: {}".format(item.title(), count))
        item_total = item_total + count
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
                inventory.setdefault(item, 1)
        else:
            inventory[item]= inventory[item]+1

addToInventory(inv, dragonLoot)
displayInventory(inv)