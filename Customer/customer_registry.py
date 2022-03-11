import uuid
from Data.data_read_write import FileReadAndWrite
from Items.item_list import Item
from Session.cart_management import Cart
class Customer(FileReadAndWrite):
    def access(self,option):
        if option==1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.login(username,password)
            #self.findItemFromDB()
        elif option==2:
            print('Create new Account')
            username = input("Create your username: ")
            password = input("Create your password: ")
            first_name = input("Enter you first name: ")
            last_name = input("Enter you last name: ")
            email=input("Enter your email: ")
            phone=int(input("Enter phone number of user: "))
            gender=input("Enter gender of user: ")
            address_type=input("Enter address_type of user: ")
            add_1=input("Enter add_1 of user: ")
            city=input("Enter city of user: ")
            country=input("Enter country of user: ")
            pin=int(input("Enter pin of user: "))
            self.register( username,password, first_name,last_name, email, phone, gender,address_type,add_1,city,country,pin)

    def register(self,username,password, first_name,last_name, email, phone, gender,address_type,add_1,city,country,pin):
        path="Customer/Data/{b}_details.json".format(b=username)
        self.writeCustomerFileData(username,password, first_name,last_name, email, phone, gender,address_type,add_1,city,country,pin)
        self.login(username,password)
    
    def login(self,username,password):
        customer_login_data= self.validateCustomerLoginData(username,password)
        if customer_login_data['username']==username and customer_login_data['password']==password:
           print("successfully logged in")
           session=Cart()
           current_session_id=session.insertCustomerSessionDetails(customer_login_data)
           #print(session.insertCustomerSessionDetails.current_session_id)
           self.findItemFromDB(current_session_id)
        else:
            print("Login failed. Please try again")



    def findItemFromDB(self,current_session_id):
        z=True
        while z:
            b=input('Do you want to search product? y/n :')
            if b.upper()!='Y':
                z=False
            else:
                print("Type something what you want to search")
                product=input('Enter keyword to search : ')
                product_description=self.getItemsFileData(product)
                print('PRODUCT : {a}'.format(a=product_description['item_name']))
                print('PRICE : {a}'.format(a=product_description['price']))
                add_to_cart=input('Do you want to add the product to cart? y/n :')
                if add_to_cart.upper()=='Y':
                    add_item_cart=Cart()
                    add_item_cart.addItemsToCart(current_session_id,product_description)
                    add_item_rating=Item()
                    add_item_rating.addItemCustomerRating(current_session_id,product_description)
                else:
                    z=False
 