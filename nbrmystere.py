import random

nbrMyst1 = random.randint(0,100)
nbrMyst2 = random.randint(0,100)
nbrMyst3 = random.randint(0,100)
print(nbrMyst1)
print(nbrMyst2)
print(nbrMyst3)
response = -1
countResponse = 0


def checkLose(countResponse,tryResponse):
    if(tryResponse == 5):

        print("Tu as perdu ! ")
        countResponse += 4
        
    else:
        tryResponse += 1
        print(f"Il te reste {5 - tryResponse} essais")
        takeResponse

while countResponse < 3:

    tryResponse = 0
    
    while nbrMyst1 != response:
    
        takeResponse = int(input("Trouve le premier nombre : "))

        if(nbrMyst1 == takeResponse):
            print("Bravo tu as trouvé le premier nombre")
            countResponse += 1
            break
        elif(nbrMyst1 > takeResponse):
            print("Le nombre est plus grand")           
            checkLose(countResponse,tryResponse)
            
        elif(nbrMyst1 < takeResponse):
            print("Le nombre est plus petit")
            checkLose(countResponse,tryResponse)

    while nbrMyst2 != response:
    
        takeResponse = int(input("Trouve le deuxieme nombre : "))

        if(nbrMyst2 == takeResponse):
            print("Bravo tu as trouvé le deuxieme nombre")
            countResponse += 1
            break
        elif(nbrMyst2 > takeResponse):
            print("Le nombre est plus grand")
            tryResponse += 1
            print(f"Il te reste {20 - tryResponse} essais")
            takeResponse
        elif(nbrMyst2 < takeResponse):
            print("Le nombre est plus petit")
            tryResponse += 1
            print(f"Il te reste {20 - tryResponse} essais")
            takeResponse

    while nbrMyst3 != response:
    
        takeResponse = int(input("Trouve le troisieme nombre : "))

        if(nbrMyst3 == takeResponse):
            print("Bravo tu as trouvé le troisieme nombre")
            countResponse += 1
            break
        elif(nbrMyst3 > takeResponse):
            print("Le nombre est plus grand")
            tryResponse += 1
            print(f"Il te reste {20 - tryResponse} essais")
            takeResponse
        elif(nbrMyst3 < takeResponse):
            print("Le nombre est plus petit")
            tryResponse += 1
            print(f"Il te reste {20 - tryResponse} essais")
            takeResponse

    print("Tu as gagné le premier défi !")
        