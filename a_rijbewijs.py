# Maak een selectie om na te gaan of iemand oud genoeg is voor een rijbewijs.
def check_rijbewijsleeftijd(leeftijd):
    rijbewijsleeftijd = 18


    # Schrijf hier jouw selectie!

# Vraag de leeftijd aan de gebruiker
input_leeftijd = int(input("Hoe oud ben je? "))
if input_leeftijd <=18:
    print("jij bent nog te jong!")
else:
    print("Jij bent oud genoeg!")



# Roep de functie aan om de leeftijd te controleren
check_rijbewijsleeftijd(input_leeftijd)