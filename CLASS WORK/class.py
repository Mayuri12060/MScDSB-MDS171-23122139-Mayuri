# # def sumlistfn(lst):
# #     sum=0
# #     for item in lst:
# #         sum=sum+int(item)
# #     return sum
 
# # userInput=input("enter a list")
# # array=userInput.strip().split(',')
# # sum = sumlistfn(array)
# # print("sum :",sum)

# # print("hello")

# #convert num into words
# #num = int(input("enter start"))
# #while num < 100:
#  #   name = (num*num)*num
#   #  print(num,name)
#    # num= num+1

# #names=[]
# #for i in range(0,20,1):
# #name = input("enter age")
#     # name = name.upper() 
#     # nae = name.append(name)
    
# my_dict = {
#     "Name": "Mayuri",
#     "class" : "MSC DS B",
#     "Reg no.": "23122139"
# }
# my_dict["Name"] = "Mrunmayi"
# print(my_dict)

# my_dict["R/No."] = "230"
# print(my_dict)

# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)

# students = {
#     "Names" : ["mayuri","rayan","yashi","shravani","shivangi"],
#     "roll no." : ["1","2","3","4","5"]

# }
# #for name in students["Names"]:
# print(students["Names"][2])
    
# mscdsb = [
#     {
#         "Roll no.": 301,
#         "name": "Mayu",
#         "email" : "mayuri@yahoo"
#     }
    
# ]
# list to store names
listNames = [] 
 
def storenames(name):
    name = name.strip().title()
    if name in listNames:
        return False
    else:
        listNames.append(name)
        return True

def printNames():
    print("_"*30)
    for name in listNames:
        print(name)
    print("_"*30)

# function to search for a name
def searchName(name):
    name = name.strip().title()
    flag = False
    for name in listNames:
        if name == item:
            flag == True
            
while True:
    print("Menu options")
    print("*"*30)
    print("1.Enter a Name")
    print("Search a name")
    print("3. List all names")
    print("4. exit")

    choice = int(input("Enter your choice : "))

if choice == 1:
    userInp = input("enter a name")
    retVal = storenames(userInp)
    if retVal ==  True:
        print("Name added successfully")
    else :
        print("name exists in the list")
elif choice == 2:
    userInp = input("Enter the name to be searched")
    searchName(userInp)
elif choice == 3:
    printNames()
elif choice == 4:
    exit ()
else:
    print("Invalid option,please choose correct one")





