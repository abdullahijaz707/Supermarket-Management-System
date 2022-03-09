 #Display screen
from ast import While
import pandas as pd

screen=print("Welcome to The Supermarket management system. \n What would you like to access? \n 1-Staff \n 2-Inventory \n 3-Equipments")

while True:

    screen_option=eval(input(" "))

#For staff
    if(screen_option==1):

        staff_screen= print("How would you like to search? \n 1-Search by ID \n 2-Search by Name")

        staff_option=eval(input(" "))

#When user selects (Search by ID)
        if staff_option==1:

            #making dataframe from csv file and selecting ID column

            staff_data= pd.read_csv("newstaff.csv",index_col= "ID")
            
            #Taking ID from the user
            staff_id=input("Enter your ID (S001-S048): ")
            
            #using indexing to access user entered id
            id= staff_data.loc[staff_id]
            print(id.to_string())
#When user selects (Search by Name)
        if staff_option==2:

            #making dataframe from csv file and selecting Name column
            staff_data=pd.read_csv("newstaff.csv",index_col="Name")

            #Taking name from the user
            staff_name= input("Enter your name: ")
            staff_name=staff_name.replace(" ",'')
            staff_name=staff_name.lower()

            #using indexing to access user entered name
            name=staff_data.loc[staff_name]
            print(name.to_string())
#Staff end

#For Inventory

    if (screen_option==2):

        inventory_screen= print("How would you like to search? \n 1-Search by Product ID \n 2- Search by Product Name ")

        inventory_option=eval(input(" "))
    
#When user selects Search by Product ID

        if (inventory_option==1):

            #making dataframe from csv file and selecting Product ID column
            inventory_data= pd.read_csv("newinventory.csv",index_col="Product ID")

            #Taking id from the user
            product_id=input("Enter Product ID (P001-P059): ")

            #using indexing to access user entered Product id
            product= inventory_data.loc[product_id]
            print(product.to_string())

#When user selects Search by Product Name

        if (inventory_option==2):

            #making dataframe from csv file and selecting Product Name column

            inventory_data= pd.read_csv("newinventory.csv", index_col="Product Name")

            #Taking Product Name from the user
            product_name=input("Enter Product Name: ")
            product_name=product_name.replace(" ",'')
            product_name=product_name.lower()

            #using indexing to access user entered Product name

            product=inventory_data.loc[product_name]
            print(product.to_string())

#Inventory end

#For equipment

    if (screen_option==3):

        equipment_screen=print("How would you like to Search? \n 1-Search by Item ID \n 2-Search by Item Name")

        equipment_option=eval(input(" "))

#When user selects Search by Item ID
        if(equipment_option==1):
            
            #making dataframe from csv and selecting Item ID column

            equipment_data=pd.read_csv("newequipments.csv",index_col="Item ID")

            #Taking Item ID from the user

            item_id=input("Enter the Item ID (I001-I013): ")

            #using indexing to access user entered Item ID

            item=equipment_data.loc[item_id]

            print(item.to_string())

#when user selects Search by Item Name
        if(equipment_option==2):

            #making dataframe from csv and Selecting Item Name column

            equipment_data=pd.read_csv("newequipments.csv", index_col="Item Name")

            #Taking Item Name from the user

            item_name=input("Enter the Item Name: ")
            item_name=item_name.replace(" ",'')
            item_name=item_name.lower()

            #using indexing to access user entered Item Name

            item=equipment_data.loc[item_name]

            print(item.to_string())










