# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# JIn,12/4/19,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Jin,12/4/19,Modified code to complete assignment 8
    """
    # --Fields--
    # --Constructor--
    def __init__(self, product_name: str, product_price: float):
        # --Attribute --
        self.__product_name = product_name
        self.__product_price = product_price
    #--Properties--
    @property
    #product name
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, name):
        if str(name).isnumeric() == False:
            self.__product_name = name
        else:
            raise Exception("Product Name cannot be numbers")

    #product_price
    @property
    def product_price(self):
        return float(self.__product_price).title()

    @product_price.setter
    def product_price(self, value):
        if float(value).isnumeric() == True:
            self.__product_price = value
        else:
            raise Exception("Product Price has to be numbers.")

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Jin,12/4/2019,Modified code to complete assignment 8
    """
    #methods:
    @staticmethod
    def read_data_from_file(file_name):
        """
        :param file_name: (string) with name of file:
        :return: list_of_products: (list) of products
        """
        list_of_products = []
        objFile = open(file_name, "r")
        for line in objFile:
            row = line.split(",")
            list_of_products.append(row)
        objFile.close()
        return list_of_products

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """
        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you want to write into the file:
        """
        objFile = open(file_name,"w")
        for product in list_of_product_objects:
            objFile.write(product[0] + ","+product[1]+"\n")
        objFile.close()
        return "Data stored to file"



# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """
    desc: class for input/output
    methods includes:
        print_menu(): show menu to user and ask for user choice
        print_data(list_of_products): prints out the current product list for user
        add_product(): add more product data from user
    """
    pass
    @staticmethod
    def print_menu():
        '''
        desc: method to print menu to display to user and return user choice
        :return: menu_choice: (str) user choice from menu
        '''
        print('''
        Menu:
        1) Show current data from file
        2) Add a new product and price
        3) Save Data
        4) Exit
        
        ''')
        menu_choice = input("What would you like to do?")
        return menu_choice

    @staticmethod
    def print_data(list_of_products):
        '''
        desc: prints out data from the list of products
        :param list_of_products: products to be displayed
        '''
        for product_data in list_of_products:
            print(product_data[0] + "  $"+product_data[1])
        print()

    @staticmethod
    def add_product():
        '''
        desc: asks user for product details and return that.
        :return:  product with the user input
        '''
        product_name = input("What's the name of the product you would like to add?")
        product_price = input("What's the price of the product you would like to add?")
        try:
            if product_price.isnumeric() == True:
                product=[product_name, product_price]
                return product
            else:
                raise Exception("Please Enter number for products")
        except Exception as e:
            print(e)

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
while True:
    user_choice = IO.print_menu()

    if user_choice =="1":
        IO.print_data(lstOfProductObjects)
        continue
    elif user_choice =="2":
        lstOfProductObjects.append(IO.add_product())
        continue
    elif user_choice =="3":
        FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
        continue
    elif user_choice == "4":
        break
    else:
        print("Please choose between 1-4.")
        continue


# Main Body of Script  ---------------------------------------------------- #

