import pymongo
client=pymongo.MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
db=client['dunderstore']
class FileReadAndWrite():
        users=db['customers']
        items=db['items']
        stores=db['stores']

        def writeCustomerFileData(self, username, first_name,last_name, email, phone, gender,address_type,add_1,city,country,pin):
            data={'username':username,
                  'first_name':first_name,
                  'last_name':last_name,
                  'email':email,
                  'phone':phone,
                  'gender':gender,
                  'cust_address':[{"address":[{'add_1':add_1,
                                               'city': city,
                                               "address_type":address_type,
                                               'country': country,
                                               'pin':pin}]}]
                  }

            self.users.insert_one(data)
            print("Registration Successfull")

        def getCustomerFileData(self,username):
            results=self.users.find({'username':username})
            for result in results:
                print(result)
        
        def getItemsFileData(self,product):
            results=self.items.find({"$text": {"$search":product}}).limit(10)
            a=[]
            for result in results:
                a.append(result)
                print(result)
            return a   
            

        def writeItemFileData(self,item_name, item_desc,item_category, create_date,brand, brand_email, brand_phone,price):
            data={'item_name':item_name,
                  'item_desc':item_desc,
                  'item_category':item_category,
                  'create_date':create_date,
                  'brand':brand,
                  'brand_email':brand_email,
                  'brand_phone':brand_phone,
                  'price':price
                  }

            self.items.insert_one(data)
            print("Item created successfully")      
        
        def getStoreFileData(self,store):
            results=self.stores.find({'store_name':store})
            for result in results:
                print(result)


