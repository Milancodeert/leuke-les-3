# Maak een programma dat de gebruiker in staat stelt een vorm te kiezen (vierkant, driehoek of cirkel)
# en de gekozen vorm op het scherm te tekenen.
#
# Als de gebruiker een ongeldige vorm invoert, moet het programma een foutmelding weergeven.
import turtle

input_welkvorm = input("welke vorm wil je maken? Je kunt kiezen uit: vierkant, driehoek, cirkel of ster ")
if input_welkvorm == "vierkant":
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.done()
if input_welkvorm == "driehoek":
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.done()
if input_welkvorm == "cirkel":
    for _ in range(160):
        turtle.forward(14)
        turtle.left(6)
    turtle.done()
else:
    print("deze vorm kan ik niet maken, of je hebt een vorm die ik wel kan maken fout gespeld!")
