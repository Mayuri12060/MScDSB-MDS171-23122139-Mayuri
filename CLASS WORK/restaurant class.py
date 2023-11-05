# restaurant class
# customers -> orders (Menu)
# collecting orders
# billing
# update order 
# search for an order 
import random
class restaurant():
    def __init__(self):
        self.menu = {
            "rice": 30,
            "dosa": 50,
        }
        # order id : {set of order details}
        self.order = {}
    def printmenu(self):
        print("*"*30)
        print("the correct options in the menu are :")
        print("*"*30)
        print(self.menu)
        print("*"*30)
    def generateOrderID(self):
        orderid = ""
        for i in range(1,6,1):
            orderid+= str(random.randint(i,10))
        return orderid
    def collectorder(self):
        self.printmenu() #print menu
        phone = int(input("Enter Customer Phone Number:"))
        order = {}
        while True:
            item=input("Enter the item you want to order")
            qty= int(input("enter quantity"))
            order[item]= qty
            choice = input("DO you want to complete order ?""Y") 
            if choice == 'Y':
                break
        orderid = self.generateOrderID()
        self.order[orderid]= {
            "Phone": phone,
            "Order": order
        }   
        #ask user to enter value
        #collect value and update order 
        #print order

        def bill(self):
            bill=qty*30
            print("bill is",bill)
obj= restaurant()
obj.collectorder()
obj.generateOrderID()
