# Funktionen ======================================================================================
# def
def greeting(name):
    print("Hallo " + name)
    print("Schön das du wieder da bist!")
    print("Ich wünsche dir viel Spaß beim Programmieren!")


greeting("VuNam")


# None & NoneType
def maximum(a, b):
    if a < b:
        return b
    else:
        return a


result = maximum(5, 3)
print(result)

# Optionale Parameter
for x in range(2, 5, 2):
    print(x)


def greeting(first_name, last_name, academic_title=""):
    if academic_title != "":
        academic_title += " "                           
    print("Hallo " + academic_title + first_name + " " + last_name)
    print("Schön das du da bist!")
"""
greeting("Vu Nam", "Phan", "Dr.")
greeting(first_name="Vu Nam", last_name="Phan", academic_title="Dr.")
greeting("Vu Nam", last_name="Phan", academic_title="Dr.")
"""


myInfoAboutMe = ("Vu Nam", "Phan", 12)
# first_name = myInfoAboutMe[0]
a , b , c = myInfoAboutMe



print(a)
print(b)
print(c)