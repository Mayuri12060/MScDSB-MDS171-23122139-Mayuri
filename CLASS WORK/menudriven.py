# listNames = [] 
 
# def storenames(name):
#     name = name.strip().title()
#     if name in listNames:
#         return False
#     else:
#         listNames.append(name)
#         return True

# def printNames():
#     print("_"*30)
#     for name in listNames:
#         print(name)
#     print("_"*30)

# # function to search for a name
# def searchName(name):
#     name = name.strip().title()
#     flag = False
#     for name in listNames:
#         if name == item:
#             flag == True
            
# while True:
#     print("Menu options")
#     print("*"*30)
#     print("1.Enter a Name")
#     print("Search a name")
#     print("3. List all names")
#     print("4. exit")

#     choice = int(input("Enter your choice : "))

# if choice == 1:
#     userInp = input("enter a name")
#     retVal = storenames(userInp)
#     if retVal ==  True:
#         print("Name added successfully")
#     else :
#         print("name exists in the list")
# elif choice == 2:
#     userInp = input("Enter the name to be searched")
#     searchName(userInp)
# elif choice == 3:
#     printNames()
# elif choice == 4:
#     exit ()
# else:
#     print("Invalid option,please choose correct one")

#------------------------------------
 #create a menu driven program that collects students details 
 #>Name register no. >email >phone >use dictionary to store student details  
#menu options 1. create 2.search 3.print

# st_dict = {}

# def create(name):
#     name = name.strip().title()
#     if name in st_dict:
#         return False
#     else:
#         st_dict.append(name)
#         return tu
# Create a menu driven program that collects students details
# > Name, Register Number, Email & Phone
# [Use dictionary to store student details]

# Menu Options
# 1. Create Students
# 2. Search for Students
# 3. Print Students

studentDict = {}

def createStudent(name,regno,email,phone):
    student = {
        "Name": name,
        "Email": email,
        "Phone": phone
    }
    studentDict[regno] = student

def colletStudentInfo():
    name = input("Enter Student Name: ")
    regno = input("Enter Student regno: ")
    email = input("Enter Student Email: ")
    phone = input("Enter Student Phone: ")
    return name, regno, email, phone

def printStudents():
    print("Regno\tName\tEmail\tPhone")
    for regno in studentDict.keys():
        print(regno,end="\t")
        for key in studentDict[regno]:
            print(studentDict[regno][key],end='\t')
        print()

while True:
    print("Menu Options")
    print("1. Enter Student Info")
    print("2. List Students")
    print("3. Exit")

    choice = input("Enter the choice").strip()
    if choice == "1":
        name, regno, email, phone = colletStudentInfo()
        createStudent(name, regno, email, phone)
    elif choice == "2":
        printStudents()
    elif choice == "3":
        exit()
    else:
        print("Invalid Choice")
    