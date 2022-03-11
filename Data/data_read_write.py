import pymongo
from datetime import datetime
client=pymongo.MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
db=client['dunderstore']
class FileReadAndWrite():
        users=db['customers']
        items=db['items']
        stores=db['stores']
        sessions=db['sessions']

        def writeCustomerFileData(self, username, password,first_name,last_name, email, phone, gender,address_type,add_1,city,country,pin):
            data={'username':username,
                  'password': password,
                  'first_name':first_name,
                  'last_name':last_name,
                  'email':email,
                  'phone':phone,
                  'gender':gender,
                  'cust_address':[{'add_1':add_1,
                                               'city': city,
                                               "address_type":address_type,
                                               'country': country,
                                               'pin':pin}]
                  }

            self.users.insert_one(data)
            print("Registration Successfull")

        def validateCustomerLoginData(self,username,password):
            results=self.users.find({'username':username,'password':password},{'username': 1,'password':1,'_id':1})
            a=[]
            for result in results:
                a.append(result)
            return a[0]     
        
        def getItemsFileData(self,product):
            results=self.items.find({"$text": {"$search":product}}).limit(10)
            a=[]
            for result in results:
                a.append(result)
            return a[0]             

        def writeItemFileData(self,item_name, item_desc,item_category, create_date,brand, brand_email, brand_phone,price):
            data={'item_name':item_name,
                  'item_desc':item_desc,
                  'item_category':item_category,
                  'create_date':create_date,
                  'brand':brand,
                  'brand_email':brand_email,
                  'brand_phone':brand_phone,
                  'price':price,
                  'ratings':[]
                  }

            self.items.insert_one(data)
            print("Item created successfully")   

        def updateItemFileData(self,item,data):   
            self.items.update_one({'_id':item['_id']}, { "$push": { 'rating': data }}) 
   
        
        def writeSessionFileData(self,cust_detail):
            data={'customer_id':cust_detail['_id'],
                  'login_time':datetime.now(),
                  'cart':[{"cart_items":[]}]
                  }
            self.sessions.insert_one(data)

        def getSessionFileData(self,cust_detail):
            data={'customer_id':cust_detail['_id']}
            results=self.sessions.find(data).sort("_id",pymongo.DESCENDING).limit(1)
            a=[]
            for result in results:
                a.append(result)
            return a[0]   

        def updateSessionFileData(self,session,data):   
            self.sessions.update_one({'_id':session['_id']}, { "$push": { 'cart.$[].cart_items': data }}) 

        def getStoreFileData(self,store):
            results=self.stores.find({'store_name':store})
            for result in results:
                print(result)


