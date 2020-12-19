import turtle
import random

turtle.bgcolor("white")

#neuer Farbmodus. Anstatt "blue" etc. können jetzt r,g,b farben benutzt werden
turtle.colormode(255)

stift = turtle.Turtle() 

stift.speed(4) 

stift.shape('turtle')

stift.width(2)

#die drei werte stehen für r=rot, g=grün, b=blau und sollen zwischen 0-255 liegen
stift.color(20, 100, 0)

def raute(x):
    """
    packe raute in Funktion (= Bauplan)
    alles danach muss 4 leerzeichen nach rechts verschoben werden
    """
    stift.forward(x)
    stift.right(60)
    stift.forward(x)
    stift.right(120)
    stift.forward(x)
    stift.right(60)
    stift.forward(x)
    stift.right(120)

k=random.randint(3,8)
print("Zufallszahl lautet:",k)

kk=random.randint(20,200)
print("Zufallszahl 2 lautet:",kk)

for i in range(k):
    raute(kk)
    stift.right(360//k)

