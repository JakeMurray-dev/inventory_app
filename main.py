#############################################
#               Inventory App               #
#             Jake Murray 2020              #
#           First Python Project            #
#############################################

""" 
1. A place to store items
2. A structure for the data of each item
3. Func to add items
4. Func to remove items
5. Func to display items
"""

""" Store -- to store the items in inventory """
store = []


class Product:
    """ Class for inventory items"""

    def __init__(self, item_name, item_quantity):
        """ Initialize item_name and item_quantity attributes """
        self.item_name = item_name
        self.item_quantity = item_quantity


response = input("Would you like to add or remove an item?\n")


def add():
    item = input("What item would you like to add? ").strip()
    quantity = int(input("How many would you like to add? ").strip())
    store.append(Product(item, quantity))


def remove():
    item = input("What item would you like to remove?\n")
    print(f"removing 1 {item.title()}")


if response.lower() == "add":
    add()
elif response.lower() == "remove":
    remove()

store.append(Product("Pencil", 35))

for item in store:
    print(f"{item.item_name.title()}: {item.item_quantity}")
