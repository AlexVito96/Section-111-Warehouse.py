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

        - Remove an Item from the catalog
            - save the changes
        
        - Register a sale
            - show the list of items
            - ask the user to choose an id
            - ask the user to provide the quantity
            - update the stock  

        - Have a log of events
            - file name for the logs
            - a list for the log entries
            - add_log_event function that receives a string
            - save_log
            - read_log
            - update existing functions to register log entries

        - Display the log of events
        
        - ** HW/ CR ** Display list of categories (unique cats)
""" 

from menu import menu, clear, header
from item import Item
import pickle
import datetime
import pandas as pd

# global vars
log = []
catalog = []
last_id = 0
data_file = 'warehouse.data'
file_data= 'log.data'

def save_log():
    global file_data
    writer = open(file_data, "wb")
    pickle.dump(log, writer)
    writer.close()
    print("** Log saved!!")

def read_log():
    try:
        global file_data
        reader = open(file_data, "rb")
        temp_list = pickle.load(reader)

        for entry in temp_list:
            log.append(entry)

        how_many = len(log)
        print("** Loaded " + str(how_many) + " log entries")
    except:
        print("** Error loading log entries")


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
    add_log_event("New Item", "Added item: " + str(last_id))

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

def update_stock(opc):
    display_catalog()
    id = int(input("Please select an Id from the list: "))
    
    # find the item with id = id
    found = False
    for item in catalog:
        if(item.id == id):
            found = True
            
            if(opc == 1):
                stock = int(input("New Stock Value: "))
                item.stock = stock
                print('Stock updated!')
                add_log_event("Set Stock", "Updated Stock for item: " + str(item.id))
            else:
                sold = int(input("Number of items to sale: "))
                item.stock -= sold # decrease the stock value by the number of sold items
                print('Sale Registered!')
                add_log_event("Sale", "Sold " + str(sold) + "items of item: " + str(item.id))

            
    if(not found):
        print("Error: Selected Id does not exist, try again")

def calculate_stock_value():
    total = 0.0
    for item in catalog:
        total += (item.price * item.stock)

    print("Total Stock Value: $" + str(total))

def remove_item():
    display_catalog()
    id = int(input("Select the id of the item to remove: "))
    found = False
    for item in catalog:
        if(item.id == id):
            catalog.remove(item)
            found = True
            add_log_event("Remove", "Removed item: " + str(item.id))
            break
    if(found):
        print("Item remove from catalog")
    else:
        print("**Error, selected id does not exist")

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%b-%d-%Y %T")

def add_log_event(event_type, event_description):
    entry = get_current_time() + " | " + event_type.ljust(10)  + " | " + event_description
    log.append(entry)
    save_log()

def print_log():
    size = len(log)
    header("Log of Events")
    for entry in log:
        print(entry)

def categorize():
    size = len(catalog)
    
    temp_list = []

    for item in catalog:
        category = item.category
        
        if(category not in temp_list):
            temp_list.append(category)
    
    for category in temp_list:
        print("\n" + category + "\n")
        
        
       
        

# instructions
# start menu

# first load data
read_catalog()
read_log()
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
        update_stock(1) #update stock
    elif(opc == '5'):
        calculate_stock_value()
    elif(opc == '6'):
        remove_item()
        save_catalog()
    elif(opc == '7'):
        update_stock(2) #register a sale
        save_catalog()
    elif(opc == '8'):
        print_log()
    elif(opc== '9'):
        categorize()
    
    input("Press enter to continue...")