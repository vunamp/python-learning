# BETA VERSION 1.0
# -*- coding: utf-8 -*-
print("Willkommen beim Chatbot")
print("Worüber würden Sie gerne heute sprechen?")
print("Zum beenden einfach 'bye' eintippen")
print("")
nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage/Antwort: ")
    print(nutzereingabe)
print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")



