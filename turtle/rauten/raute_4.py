import turtle

turtle.bgcolor("white") #hintergrundfarbe

stift = turtle.Turtle() #gebe der schildkröte den Namen Stift

stift.speed(4) 

stift.shape('turtle')

stift.width(2) #liniendicke

stift.color("blue")


#ersetze die zahlen in den bewegeungen stift.forward(100) durch
#eine Variable, zB x und setze alles in die Funktion ein
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
    #drehe am ende 120grad damit wieder in anfangsrichtung geschaut wird
    #dann sind alle gradzahlen zusammengerechnet 360grad
    stift.right(120)

#führe die Funktion raute() mehrmals aus und drehe die raute um 30 grad nach rechts
for i in range(5):
    #führe die Funktion raute aus und gebe wert für x ein
    raute(50)
    stift.right(30)

