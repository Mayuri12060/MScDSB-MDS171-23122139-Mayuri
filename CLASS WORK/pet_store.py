class Pet:
    def __init__(self):
        self.pets ={
            "dogs":[],
            "cats":[],
            "rabbits":[],
            "parrots":[]
        }
    def collectDet(self,type_,breed,colour,price):
        Details ={
            "type"  :type_,
            "breed" : breed,
            "colour": colour,
            "price": price
        }
        if type_ in self.pets:
            self.pets["dogs"].append(Details)
        elif type_ in self.cats:
            self.cats["cats"].append(Details)
        elif type_ in self.rabbit:
            self.rabbits["rabbits"].append(Details)
        elif type_ in self.parrots:
            self.parrots["parrots"].append(Details)
        else:
            print("invalid type")
P = Pet()
print(P.pets)
P.collectDet("dogs","labrador","white","5000")
print(P.pets)
P.collectDet("cats","persian","black","4400")
print(P.pets)
    # def storeDet(self,type,breed,age):
for i in P.pets:
    print(i)
    print(P.pets[i])
    for item in P.pets[i]:
        print(item)
    print(item['colour'])
    