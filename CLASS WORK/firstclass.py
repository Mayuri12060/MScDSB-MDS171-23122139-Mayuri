# class MSCDSB:
# class car:
#     def __init__(self,mft,mdl,yr):
#         self.Manufacturer = mft
#         self.Model = mdl 
#         self.Year = yr

# # name = input("enter name of manufacturer")
# # model = input("enter model")
# # year = int(input("enter year"))
# # bmw = car(name,model,year)
# print(bmw.Manufacturer,bmw.Model,bmw.Year)


# create a class restaurant,that accepts item name and qty as input
# inside your class you are having the item and its cost (unit price) as a dictionary 
# create function calculate totalcost.

# class restaurant:
#     def __init__(self,i,q):
#         self.item = i
#         self.qty = q  
#         self.menu = {
#             "BURGER": 90,
#             "SANDWICH" : 80 ,
#             "PIZZA" : 100,
#             "BREADJAM" : 40
#         }
#     def tot(self):
#         print("Total cost of the order")
#         print("item\t:",self.item)
#         print("Quantity\t:",self.qty)
#         total = self.qty * self.menu[self.item]
#         print("Total\t:",total)
# item = input("enter your choice")
# qtty = int(input("enter quantity"))
# order = restaurant(item,qtty)
# print(order.item,order.qty)
# order.tot()

#define a class expense tracker that stores the expenses and income in a dictionary
#implement the method to store the transaction ;
#view transactions ; calculate the total expense/income

class expense_tracker():
    def __init__(self):
        # self.expense = expense 
        # self.income = income
        self.expensedict = {
            "expense" : [],
            "income" : []
        }
    def  store_transactions(self,type,amt,category,date,details):
        trans = {
            "Amount": amt,
            "Category": category,
            "Date" : date,
            "Details": details,
        }
        if type == "income":
            self.expensedict['income'].append(trans)
        else:
            self.expensedict['expense'].append(trans)
    def view_transactions(self):
        for item in self.expensedict["income"]:
            print(item)
        print("your expense:")
        for item in self.expensedict["expense"]:
            print(item)
    def calculate_transaction(self):
        total_income=0
        for item in self.expensedict["income"]:
            total_income += item["ampount"]
        print("total income\t",total_income)
        total_expense=0
        for item in self.expensedict["expense"]:
            total_expense += item["amount"]
        print("total expense\t",total_expense)

#define a menu that will let users to enter expenses,view expenses
#or income, get totals in each and exit from the program
def collectInput():
    amt = int(input("Enter the amout: "))
    category = input("Enter Category: ")
    date = input("Enter Date (DD/MM/YYYY): ")
    details = input("Enter description: ")
    return amt, category, date, details
myexpense = expense_tracker()
# print(myexpense)
while True:
    print("..MY EXPENSE TRACKER..")
    print("1.record 2.income")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Records")
    print("4. View My Spendings")
    print("5. Exit")

    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        print("Enter the details of income")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        exit()
    else:
        print("In valid choice")