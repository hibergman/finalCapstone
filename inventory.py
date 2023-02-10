#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity 
         
    def get_cost(self):
        return(self.cost)

    def get_quantity(self):
        return(self.quantity)

    def __str__(self):
        return(str(self.country + self.code + self.product + str(self.cost) + str(self.quantity)))
        

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
quantity_list = []
#==========Functions outside the class==============
def read_shoes_data():
    with open("inventory.txt", "r") as file:
        inventory_data = file.read()
    
    inventory_data = inventory_data.splitlines()
    inventory_data.remove(inventory_data[0])
    for line in inventory_data:
        items = line.split(",")
        shoe_list.append(Shoe(items[0], items[1], items[2], int(items[3]), int(items[4])))

read_shoes_data()   
   
def capture_shoes():
    country = input("Please input country of origin")
    code = input("Please input product code")
    product = input("Please input product name")
    cost = float(input("Please input the retail price of the product"))
    quantity = int(input("Please input the stock quantity of the product"))
    shoe_list.append(Shoe(country, code, product, cost, quantity))
  

def view_all():
    print("_________________________________________")
    print("Report of All Shoe Class Summary Strings:")
    print("_________________________________________\n")
    for shoe in shoe_list:
        print(shoe.__str__()+"\n")


def re_stock():
    for shoe in shoe_list:
        quantity_list.append(getattr(shoe, "quantity"))
    min_quanitity = min(quantity_list)
    for shoe in shoe_list:
        if getattr(shoe, "quantity") == min_quanitity:
            print(("-------------------------------------"))
            print("The shoe with the lowest quantity is:")
            print("-------------------------------------")
            print(f"Country: {getattr(shoe,'country')}")
            print(f"Code: {getattr(shoe,'code')}")
            print(f"Product: {getattr(shoe,'product')}")
            print(f"Remaining quanitity: {getattr(shoe,'quantity')}\n")
            print("-------------------------------------")
            restock = input("Would you like to restock this item?")
            restock_value = int(input("How many units would you like to reorder?"))
            if restock == "yes":
                setattr(shoe, "quantity", getattr(shoe,'quantity') + restock_value)
    
    with open ("inventory.txt2", "w") as updated_file:
        updated_file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            updated_file.write(getattr(shoe,'country') + "," + getattr(shoe,'code') + "," + getattr(shoe,'product') + "," + str(getattr(shoe,'cost')) + "," + str(getattr(shoe,'quantity')) + "\n")
    
    print("This has been updated in the inventory - thank you!")

def seach_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''