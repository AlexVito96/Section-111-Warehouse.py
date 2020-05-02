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

        - Saving / retrieving data to/from file
        
        - Update the stock of an item
            - show the list of items
            - ask the user to choose an id
            - ask the user for the new stock value
            - find the item with selected id:
            - update the stock
            - save changes

        - Print the Total value of the stock (sum (price * stock))
""" 

from menu import menu, clear, header
from item import Item
import pickle

# global vars
catalog = []
last_id = 0
data_file = 'warehouse.data'

def save_catalog():
    global data_file
    writer = open(data_file, "wb") #create file (overwrite), open it to write binary
    pickle.dump(catalog, writer)
    writer.close()
    print("** Data Saved!!")

def read_catalog():
        try:
            global data_file
            global last_id
            reader = open(data_file, "rb")
            temp_list = pickle.load(reader)
            
            for item in temp_list:
                catalog.append(item)

            last = catalog[-1]
            last_id = last.id

            how_many = len(catalog)
            print("** Loaded " + str(how_many) + " items")
        except:
            print("** No data file found, db is empty")

# funciton methods

def register_item():
    global last_id
    header("Register new item")

    title = input("New item title: ")
    cat = input("New item category: ")
    price = float(input("New item price: "))
    stock = int(input("New item stock: "))

    new_item = Item() # <- create instances of a class (objects)
    last_id += 1   # No last_id++
    new_item.id = last_id
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

def update_stock():
    display_catalog()
    id = int(input("Please select an Id from the list: "))
    
    # find the item with id = id
    found = False
    for item in catalog:
        if(item.id == id):
            found = True
            stock = int(input("New stock value: "))
            item.stock = stock
            print('Stock updated!')
    if(not found):
        print("Error: Selected Id does not exist, try again")

def calculate_stock_value():
    total = 0.0
    for item in catalog:
        total += (item.price * item.stock)

    print("Total Stock Value: $" + str(total))

# instructions
# start menu

# first load data
read_catalog()
input("Press enter to continue")

opc = ''
while(opc != 'x'):

    clear()
    menu()
    
    print("\n\n")
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_item() 
        save_catalog()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        no_stock()
    elif(opc == '4'):
        update_stock()
        save_catalog()
    elif(opc == '5'):
        calculate_stock_value()
    
    input("Press enter to continue...")