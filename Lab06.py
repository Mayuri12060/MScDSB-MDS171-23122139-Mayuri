import random 
#opened a file in txt form
file=open("23122139.txt","w+")
#to write in file 
file.write("choco_list,qty,price\n")
#3 lists with items ,quantity and price
choco_list = ["kitkat","cadbury","bournville","eclairs","alpenlibe","mango bite","bounty","ferrero rocher","5  star","milkybar"]
qty = ["1","2","3","4","5","6","7","8","9","10"]
price = ["10","20","10","20","10","20","10","20","10","20"]

for i in range(0,99,1):
    I=random.randint(0,9)
    Q=random.randint(0,9)
    P=random.randint(0,9)
    file.write(choco_list[I]+","+qty[Q]+","+price[P]+"\n")
file.close()





   