""" 
    Program: Warehouse Management System
    Functionality: 
        - Repeated menu
        - Register items to the catalog
            id (auto generated)
            title
            category
            price
            stock
        - Display Catalog
        - Display items with no stock (out of stock)
""" 

from menu import menu, clear, header
from item import Item

# global vars
catalog = []

# funciton methods

def register_item():
    header("Register new item")

    title = input("New item title: ")
    cat = input("New item category: ")
    price = float(input("New item price: "))
    stock = int(input("New item stock: "))

    new_item = Item() # <- create instances of a class (objects)
   
    new_item.title = title
    new_item.category = cat
    new_item.price = price
    new_item.stock = stock

    catalog.append(new_item)

    print("Item created")

def display_catalog():
    size = len(catalog)
    header("Current Catalog (" + str(size) + " items)")

    print(" | " + 'ID'.rjust(2) 
        + " | " + 'Title'.ljust(24)
        + " | " + 'Category'.ljust(15)
        + " | " + 'Price'.rjust(10)
        + " | " + 'Stock'.rjust(5) + "|" )
    print("-" * 70) 

    for item in catalog:
        print(" | " + str(item.id).rjust(2) 
        + " | " + item.title.ljust(24)
        + " | " + item.category.ljust(15)
        + " | " + str(item.price).rjust(10)
        + " | " + str(item.stock).rjust(5) + "|" )


def no_stock():
    size = len(catalog)
    header("Current Catalog (" + str(size) + " items)")

    print(" | " + 'ID'.rjust(2) 
        + " | " + 'Title'.ljust(24)
        + " | " + 'Category'.ljust(15)
        + " | " + 'Price'.rjust(10)
        + " | " + 'Stock'.rjust(5) + "|" )
    print("-" * 70) 

    for item in catalog:
            if(item.stock == 0):
                print(" | " + str(item.id).rjust(2) 
                + " | " + item.title.ljust(24)
                + " | " + item.category.ljust(15)
                + " | " + str(item.price).rjust(10)
                + " | " + str(item.stock).rjust(5) + "|" )


# instructions
# start menu
opc = ''
while(opc != 'x'):

    clear()
    menu()
    print("\n\n")
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_item()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        no_stock()

    input("Press enter to continue...")