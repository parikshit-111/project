import uuid
from Data.data_read_write import FileReadAndWrite
from Items.item_list import Item
class Customer(FileReadAndWrite):
    def access(self,option):
        if option==1:
            print('loged in successfully')
            self.findItemFromDB()
        elif option==2:
            print('Create new Account')
            username = input("Enter you username: ")
            first_name = input("Enter you first name: ")
            last_name = input("Enter you last name: ")
            email=input("Enter your email: ")
            phone=input("Enter phone number of user: ")
            gender=input("Enter gender of user: ")
            address_type=input("Enter address_type of user: ")
            add_1=input("Enter add_1 of user: ")
            city=input("Enter city of user: ")
            country=input("Enter country of user: ")
            pin=input("Enter pin of user: ")
            self.register( username, first_name,last_name, email, phone, gender,address_type,add_1,city,country,pin)

    def register(self,username, first_name,last_name, email, phone, gender,address_type,add_1,city,country,pin):
        path="Customer/Data/{b}_details.json".format(b=username)
        self.writeCustomerFileData(username, first_name,last_name, email, phone, gender,address_type,add_1,city,country,pin)
        self.findItemFromDB()


    def findItemFromDB(self):
        print("Type something what you want to search")
        product=input('Enter keyword to search : ')
        product_description=self.getItemsFileData(product)
        add_to_cart=input('Do you want to add the product to cart? y/n :')
        if add_to_cart.upper()=='Y':
            print(product_description)
 