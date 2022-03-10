import uuid
from Data.data_read_write import FileReadAndWrite
from Items.item_list import Item
class Admin(FileReadAndWrite):

    def adminLogin(self):
        username=input('Enter Username: ')
        password=input('Enter Password: ')
        print('logged in successfully')
        self.adminAccess()

    def adminAccess(self):
        admin_roles={1:'Add Item to database',
                     2:'Update Item on database',
                     3:'Remove Item from database',
                     4:'Search Item on database',
                     5:'Add Store to database',
                     6:'Update Store on database',
                     7:'Remove Store from database',
                     8:'Search Store on database',}

        for role,role_desc in admin_roles.items():
            print('{a}. {b}'.format(a=role,b=role_desc))
        
        selected_role=int(input("What you want to select from above?"))

        if selected_role==1:
            add_item=Item()
            add_item.addItemToDB()
        elif selected_role==4:
            find_item=Item()
            find_item.findItemFromDB()

    def register(self,customer_id,username, first_name,last_name, email, phone, gender,address_type,add_1,city,country,pin):
        path="Customer/Data/{b}_details.json".format(b=username)
        self.writeCustomerFileData(path, customer_id,username, first_name,last_name, email, phone, gender,address_type,add_1,city,country,pin)
        searchProducts()


def searchProducts():
    print("Type something what you want to search")
    product=input('Enter keyword to search : ')
    searched_product=Item()
    searched_product.item_find(product)

   