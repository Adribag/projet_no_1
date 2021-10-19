def startCodeCesar():
    credo = "beautiful is better than ugly explicit is better than implicit simple is better than complex"

    listAlphabet =[
        ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
        ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        ]

    import random

    encodeKey = random.randint(0,25)
    encodeLetter = listAlphabet[0][encodeKey]
    def encode():
        
        # print(encodeKey)
        # print(listAlphabet[0][encodeKey])

        newCredo = ""
        for letter in credo:
            if letter == " ":
                newCredo += " "
            for index, listLetter in enumerate(listAlphabet[0]):
                if letter == listLetter:
                    newLetter = index + encodeKey
                    newCredo += listAlphabet[1][newLetter]
        print(credo)
        print(newCredo)
        return newCredo

    newCredo = encode()

    def decode():
        decrypt = True
        while decrypt:
            result = input("Entre la bonne lettre pour décrypter le message... : ")    
            if result == "":        
                print(newCredo)
            elif result == encodeLetter:
                print(credo)
                print("Bravo tu as trouvé la clé de cryptage")
                decrypt = False
            else:
                print("Mauvaise Réponse !")
                print(newCredo)

    decode()
    
startCodeCesar()