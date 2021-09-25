from random import *
sterne=0
hamburger={"cheesburger":["Brot",
                          "Käse",
                          "Zwiebeln",
                          "Fleisch",
                          "Käse",
                          "Brot"],
           "Pizza Magerita":["Teig",
                             "Tomatensoße",
                             "Käse",
                             "Basilikum"]}

class Kunde():
    def __init__(self,gericht,sterne):
        self.sterne=sterne
        if gericht==1:
            self.gericht="cheesburger"
        if gericht==2:
            self.gericht="Pizza Magerita"
    def __str__(self):
        return("Ich hätte gerne "+self.gericht)
    def essen_machen(self):
        zutaten=[]
        for i in range(len(hamburger[self.gericht])):
            zutaten.append(input())
        if zutaten==hamburger[self.gericht]:
            self.sterne+=1
            print("Vielen Dank")
        else:
            self.sterne-=1
            print("Hierhin komme ich nie wieder")
        del(self)
while True:
    k=Kunde(randint(1,2),sterne)
    print(k)
    k.essen_machen()

