#problem mit listen: Sie können sich mischen

import random

burgerliste = [1,2,3]

burger_namen = ["Cheeseburger", "hamburger", "Double Cheeseburger"]

burger_zutaten = [ ["Käse", "fleisch", "Brot"],  ["fleisch", "Brot"], ["DoppelKäse", "fleisch", "Brot"] ]


def burgerprinter(zahl):
    print(burgerliste[zahl])
    print(burger_namen[zahl])
    print(burger_zutaten[zahl])
    
    

burgerprinter(2)

random.shuffle(burger_zutaten)

burgerprinter(2)
