
from Customer.customer_registry import Customer
from Admin.admin_control import Admin

print("Welcome to Dunder Mifflin Paper Company")
print("Press A for Admin login or U for customer login")
a=True
while a:
    choice=input("Enter :")
    if choice.upper() =='A':
        admin=Admin()
        admin.adminLogin()
        a=False
    elif choice.upper() =='U':
        print('Press 1 for Login or press 2 for register new account')
        b=True
        while b:
            choice=int(input("Enter :"))
            if choice in [1,2]:
                b=False
            else:
                print("wrong input, try again")
        user=Customer()
        user.access(choice)
        a=False
    else:
        print("wrong input, try again")