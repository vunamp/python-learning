# MODULE 6 <=======================================================================================
# Kontrollstrukturen Einführung
# Die if-Anweisung ===============================================================================
# Die else-Anweisung
# Die elif-Anweisung
number = int(input("Bitte gebe eine Ganzzahl ein: "))
if number == 1:
    print("Die eingegebene Zahl ist die 1")
    # hier könnten nun noch beliebig viele weitere Anweisungen stehen
elif number == 2:
    print("Die eingegebene zahl ist die 2")
    # ...
elif number == 3:
    print("Die eingegebene zahl ist die 3")
    # ...
elif number == 4:
    print("Die eingegebene zahl ist die 4")
    # ...
elif number == 5:
    print("Die eingegebene zahl ist die 5")
    # ...
elif number == 6:
    print("Die eingegebene zahl ist die 6")
    # ...
elif number == 7:
    print("Die eingegebene zahl ist die 7")
    # ...
elif number == 8:
    print("Die eingegebene zahl ist die 8")
    # ...
elif number == 9:
    print("Die eingegebene zahl ist die 9")
    # ...
else:
    print("Die eingegebene Zahl ist entweder die 0 oder die 10 oder sie ist grösser als die 10 ")

print("Hier gehts weiter ....")
# ======================================================================================================
# while schleife
counter = 7
while counter < 10:
    print("Das ist eine ausgabe ....")
    counter += 1
