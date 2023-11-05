# create a sportMart class, where you will have 
# -> inventory / shelf of items
# -> Orders of customers

# Create csv file which will store your inventory details and order details

# with the help of file handling technqiues in python, read the file and create an object for trinity store and populate the inventory items and orders into the trinity stor

# -------> 1)make  2 excel (csv)sheets to store order details and inventory 
# 2)start with class and keep order and inventory in empty dict
# further make a class and add functions to it 

class sportMart:
    def __init__(self):
         self.inventory ={}
         self.orders = {}

    def createOrder(self,Orderid,Itemname,Quantity,Price,Total):
        temp_1 = {
             "Orderid": Orderid,
             "itemname":Itemname,
             "Quantity": Quantity,
             "Price": Price,
             "total": Total
         }
        self.orders[Orderid]= temp

    def createInventory(self,Productid,ProductName,Quantity,Price):
        temp = {
                "Product_id": Productid,
                 "Product_name": Productname,
                 "Quantity": Quantity,
                 "Price": Price,
              }
        self.inventory[Productid] = temp

    def printOrders(self):
        print(self.orders)

    def printInventory(self):
        print(self.inventory)

trinity = sportMart()
orders = open("orders.csv","r")
orders_header = orders.readline()
orders_orders = orders.readlines()
for item in orders_orders:
    temp = item.strip().split(',')
    trinity.createOrder(temp[0],temp[1],temp[2],temp[3],temp[4])

trinity.printOrders()

inevntory = open("Inventory.csv","r")
inventory_header = inventory.readline()
inventory_inventory = inventory.read()
for item in inventory_inventory :
    temp = item.strip ().split(",")
    trinity.createInventory(temp[0],temp,[1],temp[2],temp[3])

# menu driven program
def menu():
    print("1.Create Order")
    print("2. Update the inventory")
    print("3.printinventory")
    print("4.printorders")
    print("5.exit")
choice = int(input("enter your choice:"))
if choice == 1:
    OrderID = input("Enter Order ID:")
    ItemName = input("enter the ItemName:")
    quantity = int(input("enter the quantity:"))
    price = int(input("enter the price:"))
    total = int(input("enter the total:"))
                      
elif choice == 2:
    ProductID = input("Enter the ProductID:")
    ProductName = input("enter the ProductName:")
    quantity = int(input("enter the quantity:"))
    price = input("enter the price:")

elif choice == 3:
    trinity.printinventory("ProductID","ProductName","quantity","price")

elif choice == 4:
    trinity.printorders("OrderID","ItemName","quantity","price","total")

elif choice == 5:
    exit()
else: 
    print("Invalid Choice")