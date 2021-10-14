import json
import random
import time

with open("infos.json","r",encoding="utf-8") as playerInfos:
    player = json.load(playerInfos)
    playerName = player["playerName"]

with open("singes.json","r",encoding="utf-8") as singesFile:
    singes = json.load(singesFile)
    # for singe in range(len(singes)):
    #     print(singes[singe]["name"])
    




fizz = "Fizz !"
buzz = "Buzz !"
fizzBuzz = "FizzBuzz !"

gameStart = True

while gameStart:
    
    listPlayers = []

    for singe in range(len(singes)):
        listPlayers.append(singes[singe]["name"])

    listPlayers.append(playerName)
    print(listPlayers)


    starter = random.randint(0,len(listPlayers)-1)
    print(f"Le premier joueur est {listPlayers[starter]}")

    gameRound = True
    countStart = 1

        
    print(f"{listPlayers[starter]} dit : {countStart}")
    

    gameTurn = True
    while gameTurn:
        
        if starter >= len(listPlayers)-1:
            starter = 0
        else:
            starter += 1

        countStart += 1

        probaSinge = random.randint(singes[singe]["minChance"],singes[singe]["maxChance"])
        probaChef = random.randint(singes[0]["minChance"],singes[0]["maxChance"])
        probaPlayer = random.randint(player["minChance"],player["maxChance"])
        chance = random.randint(0,100)
        
        if len(listPlayers) > 1 :

            if listPlayers[starter] == singes[0]["name"]:
                if probaChef < chance:
                    print(f"{listPlayers[starter]} a perdu !")
                    listPlayers.pop(starter)
                else:
                    if countStart%3 == 0 and countStart%5 == 0:
                        print(f"{listPlayers[starter]} dit : {fizzBuzz}")
                    elif countStart%3 == 0:
                        print(f"{listPlayers[starter]} dit : {fizz}")
                    elif countStart%5 == 0:
                        print(f"{listPlayers[starter]} dit : {buzz}")
                    else:
                        print(f"{listPlayers[starter]} dit : {countStart}")

            elif listPlayers[starter] == playerName:
                if probaPlayer < chance:
                    print(f"{listPlayers[starter]} a perdu !")
                    print(f"Vous avez perdu le FizzBuzz...")
                    listPlayers.pop(starter)
                    # break
                else:
                    if countStart%3 == 0 and countStart%5 == 0:
                        print(f"{listPlayers[starter]} dit : {fizzBuzz}")
                    elif countStart%3 == 0:
                        print(f"{listPlayers[starter]} dit : {fizz}")
                    elif countStart%5 == 0:
                        print(f"{listPlayers[starter]} dit : {buzz}")
                    else:
                        print(f"{listPlayers[starter]} dit : {countStart}")

            else:
                if probaSinge < chance:
                    print(f"{listPlayers[starter]} a perdu !")
                    listPlayers.pop(starter)
                else:
                    if countStart%3 == 0 and countStart%5 == 0:
                        print(f"{listPlayers[starter]} dit : {fizzBuzz}")
                    elif countStart%3 == 0:
                        print(f"{listPlayers[starter]} dit : {fizz}")
                    elif countStart%5 == 0:
                        print(f"{listPlayers[starter]} dit : {buzz}")
                    else:
                        print(f"{listPlayers[starter]} dit : {countStart}")
            
            print(listPlayers)

        else:
            print(f"Le gagnant est {listPlayers[starter]}")
            break

        time.sleep(0.5)

    restart = input("Voulez-vous rejouez au FizzBuzz ? O -> Oui ; N -> Non : ").upper()
    if restart == "O":
        gameStart = True
    else:
        gameStart = False