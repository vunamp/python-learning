# password = "240888"
# user_input = ""
# counter = 0
# print("ACHTUNG!DU HAST NUR DREI VERSUCHE")
# while user_input != password and counter < 3:
#    user_input = input("Bitte gebe das korrekte passwort ein: ")
#   counter += 1
#    if user_input != password and counter == 3:
#        print("Falsch versuche es in 10 jahre ")
#    if user_input == password:
#        print("Das passwort wurde erfolgreich eingegeben")

# Pick up person :  Tuan
userName = 'Tuan'
password = '123321'

userName_Input = ''
password_Input = ''
counter = 0


while True:
    userName_Input = input("Please enter your userName: ")
    if userName_Input != userName:
        print("You are not Tuan, thank you, BYE!!")
        continue
    while password_Input != password:
        if counter == 3:
            print("I'm so sorry, but you are not my bodyGuard!!!!!")
            break

        password_Input = input("Please enter your password: ")
        counter += 1

        if password_Input != password:
            print("Your password is incorrect, please give it a try: ")
    print("Welcome to your Homeland Vietnam Mr.VuNam")
    break














