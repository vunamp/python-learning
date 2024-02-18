# DELTA VERSION 3.0
# -*- coding: utf-8 -*-
import random

zufallsantworten = ["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ...", "AHA ...,"]

reaktionsantworten = {"Hallo": "aber Hallo",
                      "hallo": "aber Hallo",
                      "Restaurant": "MacDonalds, KFC, BurgerKing, Dominos Pizza, und noch mehr ...",
                      "restaurant": "MacDonalds, KFC, BurgerKing, Dominos Pizza, und noch mehr ...",
                      "Spielzeug": "Beyblade, Hotweels, Barbie, LOL, Lego, Nerf und noch mehr ...",
                      "spielzeug": "Beyblade, Hotweels, Barbie, LOL, Lego, Nerf und noch mehr ...",
                      "Fussbal": "Championsleague, Premierleague, Worldcup, UEFA, Europeleague, und noch mehr ...",
                      "fussbal": "Championsleague, Premierleague, Worldcup, UEFA, Europeleague, und noch mehr ...",
                      "Fußbal": "Championsleague, Premierleague, Worldcup, UEFA, Europeleague, und noch mehr ...",
                      "fußbal": "Championsleague, Premierleague, Worldcup, UEFA, Europeleague, und noch mehr ...",
                      "Länder": "Es gibt 194"
                      }
print("Willkommen beim Chatbot")
print("Worüber würden Sie gerne heute sprechen?")
print("Zum beenden einfach 'bye' eintippen")
print("Schreibe nur ein wort rein(Nur Nomen)")
print("")

nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage/Antwort: ")

    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()

    intelligenteAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))

    print("")

print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")