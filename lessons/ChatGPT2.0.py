# ALPHA VERSION 2.0
# -*- coding: utf-8 -*-
import random
zufallsantworten=["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ..."]
print("Willkommen beim Chatbot")
print("Worüber würden Sie gerne heute sprechen?")
print("Zum beenden einfach 'bye' eintippen")
print("")
nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage/Antwort: ")
    print(random.choice(zufallsantworten))
print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")
exit()