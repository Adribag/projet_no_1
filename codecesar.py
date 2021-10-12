credo = "Beautiful is better than ugly\nExplicit is better than implicit\nSimple is better than complex"

test = "abcdefghijklmnopqrstuvwxyz"
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
list =[
    ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ]

# print(credo)

# choiceLetter = input("Choisi une lettre : ")
import random
encodeKey = random.randint(0,25)

# print(f"La clé est : {encodeKey} lettre {list[encodeKey]}")
print(encodeKey)
print(test[encodeKey])
newAlphabet = ""
for i in range(0,26):
    newLetter = alphabet[i + encodeKey]
    newAlphabet += newLetter
    print(alphabet[i + encodeKey], end ="")

print()
print(f"New Alphabet => {newAlphabet}")

def crypt(credo,newAlphabet):
    pass
    

# for letter in test:
#     encode = test.replace(letter, list[encodeKey])
#     print(encode)



def code(letter,letterEncode):
    pass