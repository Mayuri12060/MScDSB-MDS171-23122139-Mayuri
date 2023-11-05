
def gsms(product,price,quantity,total,custname,phone):
    filename = open("LAB04","a+")
    filename.write("Product Name\t: \t"+product)
    filename.write("\nPrice\t: "+price)
    filename.write("\nQuantity\t: \t"+quantity)
    filename.write("\nTotal Amount\t: \t"+total)
    filename.write("\nName of the customer\t: \t"+custname)
    filename.write("\nPhone number\t: \t"+phone)
    filename.close()
gsms()
item = input("Enter the product: ")
price = input("Item Price: ")
qty = input("Number of Products: ")
total = input("Total amount is: ")
cname = input("Enter the name of the customer: ")
mob = input("Enter the phone number of the customer: ")
gms = gsms(product,price,quantity,total,custname,phone)
# if gms:
#     print("Thank you for Grocery Shopping")
#     print("---------------------------------------------")
#     for line in open("LAB04.txt", "r+"). readlines() :
#         print(line)
#         print("---------------------------------------------")
# else:
#     print("error")
    