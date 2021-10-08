credo = "Beautiful is better than ugly\nExplicit is better than implicit\nSimple is better than complex"
test = "abcdefghijklmnopqrstuvwxyz"
list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
    ]

# print(credo)

# choiceLetter = input("Choisi une lettre : ")
import random
encodeKey = random.randint(0,25)
print(f"La clé est : {encodeKey} lettre {list[encodeKey]}")
for index, value in enumerate(test):
    print(test[index + encodeKey])


for letter in test:
    encode = test.replace(letter, list[encodeKey])
    print(encode)



def code(letter,letterEncode):
    pass