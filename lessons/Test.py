print("Where are you from?")

myCountry = input("I come from: ")


def greeting(country):
    if country == "china":
        return "ni hao"
    elif country == "viet nam":
        return "xin chao"
    elif country.lower() == "germany":
        return "moin"
    else:
        return "hello"


greeting_text = greeting(myCountry)

print(greeting_text)