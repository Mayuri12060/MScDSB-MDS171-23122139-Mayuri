def Gsms(name,product,quantity):
    file=open("Gsms.txt","a+")
    file.write("Name\t:\t"+name)
    file.write("\nproduct\t:\t"+product)
    file.write("\nquantity\t:\t"+quantity)
name=input("enter your name")
product=input("enter product you want from gsms")
quantity=input("enter quantity")
Gsms(name,product,quantity)
