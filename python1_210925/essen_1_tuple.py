# in tuples kann man elemente nicht tauschen

burgertuple = (1,2,3)

burger_namentuple = ("Cheeseburger", "hamburger", "Double Cheeseburger")

burger_zutatentuple = ( ("Käse", "fleisch", "Brot"),  ("fleisch", "Brot"), ("DoppelKäse", "fleisch", "Brot") )


def burgerprinter(zahl):
    print(burgertuple[zahl])
    print(burger_namentuple[zahl])
    print(burger_zutatentuple[zahl])
    
burgerprinter(2)
random.shuffle(burger_zutatentuple)
