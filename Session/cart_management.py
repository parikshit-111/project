
from Data.data_read_write import FileReadAndWrite
class Cart(FileReadAndWrite):
    current_session_id=None
    def insertCustomerSessionDetails(self,cust_details):
        self.writeSessionFileData(cust_details)
        current_session_id=self.getSessionFileData(cust_details)
        return current_session_id
    
    def addItemsToCart(self,current_session_id,product_desc):
        item_id=product_desc['_id']
        quantity=int(input('Enter quantity: '))
        total_price=quantity*int(product_desc['price'])
        data={"item_id":item_id,"quantity":quantity,"total_price":total_price}
        self.updateSessionFileData(current_session_id,data)