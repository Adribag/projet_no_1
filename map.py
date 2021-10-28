# import random
import json
import variables as var
import function as func


def printRessources(y,x,list,icon):   
    for i in range(len(list)):
        Position = f"{var.prefix}{y};{x}{var.positionSuffix}"
        x += 1
        print(f"{Position}{icon}")       

def printBar(y,x,list,icon,color):
    for i in range(len(list)):
        Position = f"{var.prefix}{y};{x}{var.positionSuffix}"
        x += 1
        print(f"{Position}{var.prefix}{var.fgPrefix}{color}{var.styleSuffix}{icon}{var.prefix}{var.reset}{var.styleSuffix}")

def printBorderMap():
    for line in range (len(var.map)):
        if(line == 0 or line == 29):
            for i in range(len(var.map[line])):
                var.map[line][i] = var.borderMap
        else:
            var.map[line][0] = var.borderMap
            var.map[line][49] = var.borderMap

def printMount():
    """
        Affiche la montagne et le contour de la map -> mountIco
    """  
    for x in range(1,49):
        func.drawMap(var.map,1,x,var.mountIco)
    for x in range(1,19):
        func.drawMap(var.map,2,x,var.mountIco)
    for x in range(28,49):
        func.drawMap(var.map,2,x,var.mountIco)
    for y in range(3,29):
        func.drawMap(var.map,y,1,var.mountIco)
    for y in range(3,27):
        func.drawMap(var.map,y,48,var.mountIco)
    
    func.drawMap(var.map,3,2,var.mountIco)
    func.drawMap(var.map,4,2,var.mountIco)
    func.drawMap(var.map,3,3,var.mountIco)

    func.drawMap(var.map,3,47,var.mountIco)
    func.drawMap(var.map,4,47,var.mountIco)
    func.drawMap(var.map,3,46,var.mountIco)
    
def printSea():
    """
        Affiche la mer -> waterIco
    """
    for i in range(1,49):
        func.drawMap(var.map,28,i,var.waterIco)
        func.drawMap(var.map,27,i,var.waterIco)

def printRiver():
    """
        Affiche la rivière -> waterIco
    """
    for x in range(21,26):
        for y in range(20,27):
            func.drawMap(var.map,y,x,var.waterIco)
    for x in range(20,24):
        for y in range(14,20):
            func.drawMap(var.map,y,x,var.waterIco)
    for x in range(19,22):
        for y in range(8,14):
            func.drawMap(var.map,y,x,var.waterIco)
    for x in range(18,20):
        for y in range(5,8):
            func.drawMap(var.map,y,x,var.waterIco)
    for x in range(18,19):
        for y in range(1,5):
            func.drawMap(var.map,y,x,var.waterIco)

def printSand():
    """
        Affiche la plage -> sandIco
    """
    for i in range(1,49):
        func.drawMap(var.map,26,i,var.sandIco)
        func.drawMap(var.map,25,i,var.sandIco)
    for i in range(30,49):
        func.drawMap(var.map,24,i,var.sandIco)

def printQuests():
    """
        Affiche l'emplacement des quetes -> questIco
    """
    # Première quete
    func.drawMap(var.map,25,27,var.questIco)
    # Deuxieme quete
    func.drawMap(var.map,10,48,var.questIco)
    # Troisieme quete
    func.drawMap(var.map,20,10,var.questIco)
    # Porte finale
    func.drawMap(var.map,1,20,var.questIco)

def fondMap():
    """
        Affiche pour chaque emplacement de la matrice un emoticon -> florIco
    """
    for i in range(len(var.map)):
        for j in range(len(var.map[i])):
            var.map[i][j] = var.florIco

def affichageMap(map,poY = 0,poX = 0):
    """
        - map -> List
        - PoY & PoX -> position Y et X du curseur

        Affiche une matrice
    """
    for poY in range(len(map)):
        for poX in range(len(map[poY])):
            if(poX == 0):
                print()
            Position = f"{var.prefix}{poY};{poX}{var.positionSuffix}"
            print(f"{Position}{map[poY][poX]}")    

def printPos(Y,X,icon):
    Position = f"{var.prefix}{Y};{X}{var.positionSuffix}"
    print(f"{Position}{icon} ", end="")     

def printHud():
    """
        Print du Hud du jeu :
            - Titre
            - Barres de survie
            - Bordures
    """
    printPos(1,73,var.title)
    printPos(4,55,var.eat)
    printPos(8,55,var.energy)
    printPos(12,55,var.water)
    printPos(17,75,var.inventory)
    printPos(19,55,var.inventoWater)
    printPos(23,55,var.inventoFood)

    # with open("infos.json","r",encoding="utf-8") as readInfos:
    #     infoPlayer = json.load(readInfos)

    # var.eatingList = infoPlayer["eatingList"]
    # var.staminaList = infoPlayer["staminaList"]
    # var.drinkingList = infoPlayer["drinkingList"]

    printBar(5,56,var.eatingList,var.iconSurvie,var.red)
    printBar(9,56,var.staminaList,var.iconSurvie,var.green)
    printBar(13,56,var.drinkingList,var.iconSurvie,var.blue)

    printRessources(21,56,var.inventoryFoodBack,var.emptyIco)
    printRessources(21,56,var.inventoryWater,var.waterIco)
    printRessources(25,56,var.inventoryFoodBack,var.emptyIco)
    printRessources(25,56,var.inventoryFood,var.survieFoodIco)
    
    for i in range(51,110):
        printPos(3,i,var.barrehori)
    for i in range(51,110):
        printPos(16,i,var.barrehori)

    for i in range (1,30):             
        printPos(i,50,var.borderIco)

    for i in range (1,160):             
        printPos(30,i,var.borderIco)

    for i in range (31,35):
        printPos(i,23,var.barreverti) 
    for i in range (31,35):
        printPos(i,54,var.barreverti)  
    for i in range (31,35):
        printPos(i,94,var.barreverti)  
    for i in range (1,160):             
        printPos(34,i,var.barrehori)
    for i in range (1,160):             
        printPos(36,i,var.barrehori)

def delRessource():
    """
        Supprime de la liste de gestion des barres de survie un ou plusieurs index
    """
    del var.eatingList[-1]
    del var.drinkingList[-1]
    del var.staminaList[-1]
    del var.staminaList[-1]
    
def moveplayer():
    quest = "start"

    with open("infos.json","r",encoding="utf-8") as readInfos:
        infoPlayer = json.load(readInfos)

    startPosY = infoPlayer["startY"]
    startPosX = infoPlayer["startX"]
    moveCounter = infoPlayer["moveCounter"]
    currentPos = infoPlayer["currentPos"]
    # currentPos = var.sandIco
    
    func.clearConsole()
    
    func.drawMap(var.map,startPosY,startPosX,var.playIco)
    # func.drawMap(var.map,26,46,var.survieFoodIco)
    # func.drawMap(var.map,22,40,var.waterIco)
    # func.drawMap(var.map,20,45,var.mountIco)
    affichageMap(var.map)
    printHud()
    
    while quest != "end":

        moving = input("Que faire ? : ").upper()
        print()
        print(moving) 

        if moving == "Z":  
            # Vérification de la survie du joueur
            if len(var.staminaList) < 5:
                print("Tu dois te reposer !")
            elif len(var.eatingList) < 2:
                print("Tu dois manger !")
            elif len(var.drinkingList) < 2:
                print("Tu dois boire !")
            else:
            # Si il a assez d'énergie, de faim et soif on continue    
                # On récupère la case sur laquelle le joueur est positionné
                oldIco = var.map[startPosY-1][startPosX]
                # On déplace le joueur d'une case vers le haut
                startPosY -= 1 
                # On ajoute + 1 au compteur de déplacements
                moveCounter += 1
                # On affiche la map avec la nouvelle positon du joueur
                func.clearConsole()                
                func.drawMap(var.map,startPosY +1,startPosX,currentPos)  
                func.drawMap(var.map,startPosY,startPosX,var.playIco)
                affichageMap(var.map)
                # On surpprime des barres de survie les ressources necessaire au déplacement
                delRessource() 
                if(moveCounter%2 == 0):
                    del var.staminaList[-1]
                # On met à jour le compteur de déplacements
                afficheDep = f"Nombre de déplacements : {moveCounter}"
                printPos(32,26,afficheDep)
                # On affiche en X et Y la position du joueur
                posXY = f"X = {startPosX} | Y = {startPosY}"
                printPos(32,5,posXY)
                # Affichage du HUD du jeu avec les barres de survie mise à jour
                printHud()
                # On affiche la case sur laquelle le joueur est
                currentPos = oldIco
                oncase = f"Tu es sur la case {currentPos}"
                printPos(35,135,oncase)          

        if moving == "S":
            if len(var.staminaList) < 5:
                print("Tu dois te reposer !")
            elif len(var.eatingList) < 2:
                print("Tu dois manger !")
            elif len(var.drinkingList) < 2:
                print("Tu dois boire !")
            else:
                oldIco = var.map[startPosY+1][startPosX]
                startPosY += 1 
                moveCounter +=1
                func.clearConsole()
                func.drawMap(var.map,startPosY -1,startPosX,currentPos)  
                func.drawMap(var.map,startPosY,startPosX,var.playIco)
                affichageMap(var.map) 
                delRessource() 
                if(moveCounter%2 == 0):
                    del var.staminaList[-1]
                afficheDep = f"Nombre de déplacements : {moveCounter}"
                printPos(32,26,afficheDep)
                posXY = f"X = {startPosX} | Y = {startPosY}"
                printPos(32,5,posXY)

                printHud()
                currentPos = oldIco
                oncase = f"Tu es sur la case {currentPos}"
                printPos(35,135,oncase)

        if moving == "Q":
            if len(var.staminaList) < 5:
                print("Tu dois te reposer !")
            elif len(var.eatingList) < 2:
                print("Tu dois manger !")
            elif len(var.drinkingList) < 2:
                print("Tu dois boire !")
            else:
                oldIco = var.map[startPosY][startPosX-1]
                startPosX -= 1 
                moveCounter +=1
                func.clearConsole()
                func.drawMap(var.map,startPosY,startPosX +1,currentPos)  
                func.drawMap(var.map,startPosY,startPosX,var.playIco)
                affichageMap(var.map) 
                delRessource() 
                if(moveCounter%2 == 0):
                    del var.staminaList[-1]
                afficheDep = f"Nombre de déplacements : {moveCounter}"
                printPos(32,26,afficheDep)
                posXY = f"X = {startPosX} | Y = {startPosY}"
                printPos(32,5,posXY)

                printHud()
                currentPos = oldIco
                oncase = f"Tu es sur la case {currentPos}"
                printPos(35,135,oncase)

        if moving == "D":
            if len(var.staminaList) < 5:
                print("Tu dois te reposer !")
            elif len(var.eatingList) < 2:
                print("Tu dois manger !")
            elif len(var.drinkingList) < 2:
                print("Tu dois boire !")
            else:
                oldIco = var.map[startPosY][startPosX+1]
                startPosX += 1 
                moveCounter +=1
                func.clearConsole()
                func.drawMap(var.map,startPosY,startPosX -1,currentPos)  
                func.drawMap(var.map,startPosY,startPosX,var.playIco)
                affichageMap(var.map) 
                delRessource() 
                if(moveCounter%2 == 0):
                    del var.staminaList[-1]
                afficheDep = f"Nombre de déplacements : {moveCounter}"
                printPos(32,26,afficheDep)
                posXY = f"X = {startPosX} | Y = {startPosY}"
                printPos(32,5,posXY)

                printHud()
                currentPos = oldIco
                oncase = f"Tu es sur la case {currentPos}"
                printPos(35,135,oncase)

        if moving == "E":           
            if currentPos == var.survieFoodIco:
                if len(var.inventoryFood) > 9:
                    print("Tu n'as plus de place pour cette nourriture")
                else:
                    func.clearConsole()
                    print("Tu ramasse de la nourriture !")
                    var.inventoryFood.extend([0])               
                     
                    currentPos = var.emptyIco
                    affichageMap(var.map)
                    printPos(32,5,posXY)
                    printPos(32,26,afficheDep)
                    printPos(35,135,oncase)
                    printHud()
            elif currentPos == var.waterIco:
                if len(var.inventoryWater) > 9:
                    print("Tu n'as plus de place pour cette eau")
                else:
                    func.clearConsole()
                    print("Tu prends de l'eau !")
                    var.inventoryWater.extend([0])
                    
                    currentPos = var.emptyIco
                    affichageMap(var.map)
                    printHud()
            else:
                print("Il n'y a rien à ramasser...")

        if moving == "C":
            print("Tu te repose...")
            lenStamina = len(var.staminaList)
            reloadStamina = 50 - lenStamina
            countStam = 0
            
            for i in range(reloadStamina):
                countStam += 1 
                
                if countStam % 6 == 0:
                    print(countStam)
                    del var.drinkingList[-1]
                    del var.drinkingList[-1]
                    del var.eatingList[-1]
                    func.clearConsole()
                    affichageMap(var.map)
                    printPos(32,5,posXY)
                    printPos(32,26,afficheDep)
                    printPos(35,135,oncase)
                if len(var.eatingList) < 2:
                    
                    affichageMap(var.map)
                    printHud()
                    print("Tu dois manger !")
                    break
                elif len(var.drinkingList) < 2:
                    affichageMap(var.map)
                    printHud()
                    print("Tu dois boire !")
                    break
                       
                var.staminaList.extend([0])
                
                printHud()              

        if moving == "B":
            if var.inventoryWater == []:
                print("Tu ne peux pas boire")
            else:
                if len(var.drinkingList) > 40:
                    print("Tu n'as pas soif...")
                else:
                    del var.inventoryWater[-1]
                    var.drinkingList.extend([0,0,0,0,0,0,0,0,0,0])
                    func.clearConsole()
                    affichageMap(var.map)
                    printHud() 
                    print("Tu bois !")

        if moving == "M":
            # print("Tu manges !")
            if var.inventoryFood == []:
                print("Tu ne peux pas manger")
            else:
                if len(var.eatingList) > 40:
                    print("Tu n'as pas faim...")
                else:
                    del var.inventoryFood[-1]
                    var.eatingList.extend([0,0,0,0,0,0,0,0,0,0])
                    func.clearConsole()
                    affichageMap(var.map)
                    printHud() 
                    print("Tu manges !")

        if(startPosY == 25 and startPosX == 27 and var.keyOne == False):
            print()
            print("Tu es sur la première quete")
            question = input("Veux tu lancer la quete O -> Oui | N -> Non : ").upper()
            if(question == "O"):
                print("Tu lance la quete")
                import nbrmystere as nbrM
                nbrM.nbrMyst()
            else:
                print("Passe ton chemin")

        if(startPosY == 10 and startPosX == 48 and var.keyTwo == False):
            print()
            print("Tu es sur la deuxième quete")
            question = input("Veux tu lancer la quete O -> Oui | N -> Non : ").upper()
            if(question == "O"):
                print("Tu lance la quete")
                import codecesar as cesar
                cesar.startCodeCesar()
                # var.KeyTwo = True
            else:
                print("Passe ton chemin")

        if(startPosY == 20 and startPosX == 10 and var.keyThree == False):
            print()
            print("Tu es sur la troisième quete")
            question = input("Veux tu lancer la quete O -> Oui | N -> Non : ").upper()
            if(question == "O"):
                print("Tu lance la quete")
                import fizzbuzz as fizz
                fizz.startFizzBuzz()
            else:
                print("Passe ton chemin")

        if(startPosY == 1 and startPosX == 20):
            print()
            print()
            print()
            print("Te voila à la fin du jeu... As-tu toutes les clés ?")
            if(var.keyOne == True and var.keyTwo == True and var.keyThree == True):
                print()
                print()
                print("Félicitations tu as remporté les trois défis... Tu as fini le jeu !")
            else:
                print()
                print("Reviens me voir quand tu auras les trois clés en ta possession...")

        if moving == "V":

            with open("infos.json","r",encoding="utf-8") as readInfos:
                infoPlayer = json.load(readInfos)

            infoPlayer["name"] = var.thePlayerName
            infoPlayer["startY"] = startPosY
            infoPlayer["startX"] = startPosX
            infoPlayer["moveCounter"] = moveCounter
            infoPlayer["currentPos"] = currentPos
            infoPlayer["keyOne"] = var.keyOne
            infoPlayer["keyTwo"] = var.keyTwo
            infoPlayer["keyThree"] = var.keyThree
            infoPlayer["eatingList"] = var.eatingList
            infoPlayer["staminaList"] = var.staminaList
            infoPlayer["drinkingList"] = var.drinkingList
            infoPlayer["inventoryFood"] = var.inventoryFood
            infoPlayer["inventoryWater"] = var.inventoryWater

            with open("infos.json","w",encoding="utf-8") as uploadInfos:
                json.dump(infoPlayer,uploadInfos,indent=4)

            print("Partie sauvegardé")


        commande = f"Déplacement -> Z Q S D ; Rammasser -> E ; Dormir -> C ; Boire -> B ; Manger -> M ; Sauvegarder -> V"
        printPos(35,2,commande)
        cursor = ""
        printPos(37,2,cursor)
        
def startGame():
    loading = input("Voulez vous charger la dernière sauvegarde ? : O -> oui ; N -> Non : ").upper()
    if loading == "O":
        print("Chargement de la partie !")


    else:
        namePlayer = input("Quel est ton nom ?")

        var.thePlayerName = namePlayer

        with open("infos.json","r",encoding="utf-8") as readInfos:
            infoPlayer = json.load(readInfos)
        
        infoPlayer["name"] = namePlayer
        infoPlayer["startY"] = 25
        infoPlayer["startX"] = 38
        infoPlayer["moveCounter"] = 0
        infoPlayer["currentPos"] = "🟨"
        infoPlayer["keyOne"] = False
        infoPlayer["keyTwo"] = False
        infoPlayer["keyThree"] = False
        infoPlayer["eatingList"] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        infoPlayer["staminaList"] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        infoPlayer["drinkingList"] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        infoPlayer["inventoryFood"] = [0,0,0,0,0]
        infoPlayer["inventoryWater"] = [0,0,0,0,0,0,0]

        with open("infos.json","w",encoding="utf-8") as uploadInfos:
            json.dump(infoPlayer,uploadInfos,indent=4)
    #test
    func.clearConsole()
    fondMap()
    func.randomSurvie(var.map,var.survieFoodIco,var.waterIco)
    printSea()
    printSand()
    printMount()
    printRiver()
    printQuests()
    printBorderMap()

    moveplayer()

startGame()