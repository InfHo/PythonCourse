import turtle
import random

turtle.bgcolor("white")

#neuer Farbmodus. Anstatt "blue" etc. können jetzt r,g,b farben benutzt werden
turtle.colormode(255)

stift = turtle.Turtle() 

stift.speed(9) 

stift.shape('turtle')

stift.width(2)

#die drei werte stehen für r=rot, g=grün, b=blau und sollen zwischen 0-255 liegen
stift.color(0, 0, 255)

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

k=random.randint(13,80)
print("Zufallszahl lautet:",k)

kk=random.randint(20,200)
print("Zufallszahl 2 lautet:",kk)

#kleiner zahlen trick um den kreis bei hohen zahlen zu schliessen
#wenn zb k=57 -> 360//57 = 6, aber 6*57 = 342
#das // ist ein teiler mit abrunden. 360/57=3,42, der stift.right() befehl
#akzeptiert aber nur ganze zahlen
z = (360//(360//k))
k=z
print(z)
for i in range(k):
    #hier werden jetzt die farben durchgezält
    stift.color((255*(i+1))//k, i, 255-((255*(i+1))//k))
    print("RGB Werte:",(255*(i+1))//k, i, 255-((255*(i+1))//k))
    raute(kk)
    stift.right(360//k)

