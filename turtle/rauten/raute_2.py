import turtle

turtle.bgcolor("white") #hintergrundfarbe

stift = turtle.Turtle() #gebe der schildkröte den Namen Stift

stift.speed(4) 

stift.shape('turtle')

stift.width(2) #liniendicke

stift.color("blue")


def raute():
    """
    packe raute in Funktion (= Bauplan)
    alles danach muss 4 leerzeichen nach rechts verschoben werden
    """
    stift.forward(100)
    stift.right(60)
    stift.forward(100)
    stift.right(120)
    stift.forward(100)
    stift.right(60)
    stift.forward(100)
    #drehe am ende 120grad damit wieder in anfangsrichtung geschaut wird
    #dann sind alle gradzahlen zusammengerechnet 360grad
    stift.right(120)

#führe die Funktion raute aus
raute()
