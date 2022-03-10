
from Data.data_read_write import FileReadAndWrite
class Item(FileReadAndWrite):

    def findItemFromDB(self):
        print("Type something what you want to search")
        product=input('Enter keyword to search : ')
        self.getItemsFileData(product)

    
    def addItemToDB(self):
        
        print('Create new Item')
        item_name = input("Enter Item name: ")
        item_desc = input("Enter the item description: ")
        item_category=input("Enter the item category: ")
        create_date=input("Enter the item creation date: ")
        brand=input("Enter brand name: ")
        brand_email=input("Enter brand email: ")
        brand_phone=input("Enter brand phone: ")
        price=input("Enter price of item: ")
        self.writeItemFileData(item_name, item_desc,item_category, create_date,brand, brand_email, brand_phone,price)
