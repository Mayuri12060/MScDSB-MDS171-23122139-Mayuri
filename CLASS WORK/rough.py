# Write a Python program to calculate the sum of all numbers from 1 to a given positive integer n.

# def sum_num(x):
#     sum=0
#     for i in range(1,x+1):
#         sum=sum+i
#     print(sum)
# n=int(input("enter num:"))
# sum_num(n)

# Palindrome program
# a = input("enter an input:")
# to check whether its a palindrome
# b=a[::-1]
# if (b == a):
#     print("its a palindrome")
# else:
#     print("its not a palindrome")

# Write a Python program to find the factorial of a given number using recursion.

# a= 1
# b= int(input("enter any number"))

# fact = 1
# for i in range(a,b+1):
#     fact=fact*i
# print("factorial is",fact)

# reverse a string
# w = input("enter a word :")
# y = w[::-1]
# print(y)

# Basic To-Do List: Create a basic to-do list program where
#  the user can add, remove, and view tasks.
# Todo= ["exercises","lunch","dinner","classes","studies","programming"]
# Todo.append("cooking")
# Todo.pop(2)
# print(Todo)

# prime or composite
# num = int(input("enter the num to check"))
# if num > 1 :
#     for i in range(2,num):
#         if num%2 : 
#             print("num is composite")
#             break
#         else :
#             print("it is a  prime number")
# else :
#     print("invalid input")

#calculator using functions
# a = int(input("enter num1"))
# b = int(input("enter num2"))
# def sum(a,b):
#     sum = a + b
#     print(sum)
# def sub(a,b):
#     sub = a-b
#     print(sub)
# def multi(a,b):
#     multi = a*b
#     print(multi)
# def div(a,b):
#     div = a//b
#     print(div)
# sum(a,b)
# sub(a,b)
# multi(a,b)
# div(a,b)

# Define a function that accepts a list of numbers and returns the largest number in the list
# def find(numbers):
#     if not numbers:
#         return None
#     else :
#         largest = numbers[0]
# for i in range(numbers):
#     if num > largest:
#         print("num is largest",)

# season code
# m = int(input("enter a month num"))
# if (m >= 3 and m <= 5):
#     print("its summer season")
# elif (m >= 6 and m <= 8):
#     print("its spring season")
# elif (m >= 9 and m <= 11):
#     print("its autumn season")
# elif (m == 12 or m==1 or m == 2):
#     print("winter")
# else:
#     print("invalid input")

# placement code
# c = int(input("enter placements in cse"))
# e = int(input("enter placements in ele"))
# m = int(input("enter placements in mec"))

# if(c>e and c>m):
#     print("cse has highest")
# elif(e>c and e>m):
#     print("ele has highest")
# elif(m>e and mc):
#     print("mech has highest")
# else :
#     print("invalid input ")

# electric bill
# u = int(input("enter units consumed"))

# if (u <= 100):
#     bill_1 = u*3
#     print("bill is $",bill_1)
# elif (u >100 and u < 300):
#     u_2=u-100
#     bill_2 = 400 +(u_2*4)
#     print("bill is",bill_2)
# elif (u> 300):
#     u3=u-300
#     bill_3 =  1200+(u3*5)
#     print("bill is",bill_3)
# else:
#     print("invalid input")
# def pencils():
#     n = int(input('enter standard'))
#     sum = 0
#     if(n>12):
#         print("invalid")
#     else:
#         for i in range (1,n+1):
#             sum= (i*i)+sum
#             print("pencils",sum)
# pencils()
# def digi():
#     n= input("enter number")
#     count=0
#     for i in n:
#         count+=1        
#     print("digits is",count)
# digi()

# spy no:
# class spy_num:
#     def __init__(self):
#         self.n = input("enter number")
#         self.sum
#         self.multi
#     def sum_nums(self):
#         sum=0 
#         for i in self.n:
#             z=int(i)
#             sum=sum+z       
#         print(sum)
#         return sum
#     def multi_nums(self):
#         multi=1
#         for i in self.n:
                # x=int(i)
#             multi = multi*x
#         print(multi)
#         return multi
#     def spy(self):
#         total_sum = self.sum_nums()
#         product = self.multi_nums()
#         if total_sum == product:
#             print("its a spy num")
#         else:
#             print("its not a spy num")
# if __name__=="__main__":
#     M = spy_num()
#     # M.sum()
#     # M.multi()
#     M.spy()

# class greatest:
#     def __init__(self,name1,name2,name3):
#         self.name1 = name1
#         self.name2 = name2 
#         self.name3 = name3 
#     def len_names(self):
#         n1 = len(self.name1)
#         n2 = len(self.name2)
#         n3 = len(self.name3)
#         if(n1 > n2 and n1 > n3):
#             print(n1 ,"is greatest")
#         elif(n2 > n1 and n2 > n3):
#             print(n2 ,"is greatest")
#         elif(n3 > n2 and n3 > n1):
#             print(n1 ,"is greatest")
#         elif(n1 == n2 and n2 == n3):
#             print(n1 ,"is greatest")
#             print(n1 ,"is greatest")
#             print(n1 ,"is greatest")
#         else:
#             print("invalid input")
# name1 = str(input("enter name1"))
# name2 = str(input("enter name2"))
# name3 = str(input("enter name3"))
# A = greatest(name1,name2,name3)
# A.len_names()


# file handling
# def file():
# x = open("rayan.txt","+r")
    # x.write("you are mad")
# x.readline()
    # x.close()
# file()
# def newOrder(self,OrderID,ItemName,Quantity,Price,Total):
#         file=open("Customer.csv","a+")
#         file.write(OrderID,ItemName,str(Quantity),str(Price),str(Total))
#         file.close()
# OrderID = input("Enter Order ID")
# ItemName = input("Enter Item Name")
# Quantity = int(input("Enter Quantity"))
# Price = int(input("Enter Price"))
# Total = Quantity*Price
# newOrder()
class sportMart:
    def _init_(self):
        self.inventory = {}
        self.orders = {}
        
    def createOrder(self,OrderID,ItemName,Quantity,Price,Total):
        temp = {
            "orderid" : OrderID,
            "itemname" : ItemName,
            "qty" : Quantity,
            "price" : Price,
            "total" : Total
        }
        self.orders[OrderID] = temp
        
    def createInventory(self,ProductID,ItemName,Quantity,Price):
        inven = {
            "product" : ProductID,
            "itemname" : ItemName,
            "qty" : Quantity,
            "price" : Price
        }
        self.inventory[ProductID] = inven
        
    def displayOrder(self):
        print(self.orders)
        
    def displayInventory(self):
        print(self.inventory)
        
    def neworder(self):
        id = str(input("Enter the id"))
        product = input("Enter the product name")
        qty = str(input("Enter the quantity"))
        price = str(input("Enter the price"))
        total = qty*price
        self.createOrder(id,product,qty,price,total)
    
a=sportMart()
# a.newOrder()
        
trinity = sportMart()
orders = open("Customers.csv","r")

#     orders.write([OrderID]+","+ItemName,str(Quantity),str(Price),str(Total))
# OrderID = input("Enter Order ID")
# ItemName = input("Enter Item Name")
# Quantity = int(input("Enter Quantity"))
# Price = int(input("Enter Price"))
# Total = Quantity*Price

invent = open("Inventory.csv","r")
order_head = orders.readline()
order_orders = orders.readlines()
inve_head = invent.readline()
inve_data = invent.readlines()
for i in order_orders:
    newtemp = i.strip().split('\t')
    # print(newtemp)
    trinity.createOrder(newtemp[0],newtemp[1],newtemp[2],newtemp[3],newtemp[4])
print()
trinity.displayOrder()
print()
print("-"*100)
print()

for j in inve_data:
    newtemp2 =j.strip().split('\t')
    # print(newtemp)
    trinity.createInventory(newtemp2[0],newtemp2[1],newtemp2[2],newtemp2[3])
trinity.displayInventory()
print()
print("hello")
# open the file in writemode
with open("newfile.csv","w") as file:
    for item in trinity.orders:
        # print(trinity.orders[item])
        temp = ""
        for key in trinity.orders[item]:
            # print(key,trinity.orders[item][key])
            temp+= trinity.orders[item][key]+","
        print(temp)
        file.write(temp[1:]+"\n")













































































































































 
       







