import random

# erstelle dictionary mit Burgern als "key" und Zutaten als tuple-"Values" 
burgerlexikon = { "Cheeseburger": ("Fleisch", "Brot", "Senf", "Käse"),
                  "Hamburger": ("Fleisch", "Brot", "Senf"),
                  "WALDMEISTER (VEGGI)": ("Soja", "Gebratene Champignons", "Käse")
                  }

# zeigt die Burger im Dictionary
def print_burgers(lexikon):
    for i in lexikon:
        print(i, "-->", lexikon[i])

print_burgers(burgerlexikon)

# checkt ob der bestellte burger bei uns existiert
def check_produkte(lexikon, wunsch):
    if wunsch in lexikon:
        print("Kommt sofort!")
        check_zutaten(burgerlexikon, kundenwunsch)

    else:
        print("Das haben wir leider nicht. Aber wir haben:",end=" ")
        print(random.choice(list(lexikon.keys())))

# abfragen ob man die Zutaten weiss
def check_zutaten(lexikon, wunsch):
    for i in range(len(lexikon[wunsch])):
##        print(lexikon[wunsch][i])
        if input("") == lexikon[wunsch][i]:
            print("ok.")
        else:
            print("eeehhh.... ciao..")
            return

# Loop für 5 Bestellungen
for i in range(5):
    print("Bestellung Nr.: "+str(i+1)+":")
    kundenwunsch = input("Was hätten Sie den gerne?: ")
    check_produkte(burgerlexikon, kundenwunsch)
