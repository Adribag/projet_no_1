# map = [
#     # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
#     [0,1,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,49],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,1,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,49]
#     ]

# import os, sys
# import tryHud as hud
import random

import variables as var
import function as func


borderIco = "🔳"
borderMap ="🟫"
mountIco = "🟫"
sandIco = "🟨"
waterIco = "🟦"
florIco = "🟩"
questIco = "🟪"
playIco = "🟧"
survieWaterIco = "⬜"
survieFoodIco = "🟥"
iconSurvie = "■"
barrehori = "═"
barreverti = "║"
# titre = "L'île au Python"
# eat = "Nourriture"
# energy = "Energie"
# water = "Soif"
# inventory = "Inventaire"

# inventoWater = "Réserve d'eau"
# inventoFood = "Réserve de nourriture"

positionSuffix = "H"
prefix = "\x1b["
styleSuffix = "m"
reset = "0"
red = "1"
green = "2"
blue = "4"
fgPrefix = "3"

eatingList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
staminaList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
drinkingList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

inventoryFood = [0,0]
inventoryFoodBack = [0,1,2,3,4,5,6,7,8,9]
inventoryWater = [0,0,0,0]

def printRessources(y,x,list,icon):   
    for i in range(len(list)):
        Position = f"{prefix}{y};{x}{positionSuffix}"
        x += 1
        print(f"{Position}{icon}")
    
        

def randomSurvie():
    for i in range(0,40):
        randY = random.randint(5,27)
        randX = random.randint(5,45)
        drawMap(randY,randX,survieFoodIco)
    for i in range(0,40):
        randY = random.randint(5,27)
        randX = random.randint(5,45)
        drawMap(randY,randX,waterIco)

def printBar(y,x,list,icon,color):
    for i in range(len(list)):
        # print(icon)
        Position = f"{prefix}{y};{x}{positionSuffix}"
        x += 1
        print(f"{Position}{prefix}{fgPrefix}{color}{styleSuffix}{icon}{prefix}{reset}{styleSuffix}")

def drawMap(posY,posX,symb):
    var.map[posY][posX] = symb

def printBorderMap():
    for line in range (len(var.map)):
        if(line == 0 or line == 29):
            for i in range(len(var.map[line])):
                var.map[line][i] = borderMap
        else:
            var.map[line][0] = borderMap
            var.map[line][49] = borderMap

def printMount():  
    for x in range(1,49):
        drawMap(1,x,mountIco)
    for x in range(1,19):
        drawMap(2,x,mountIco)
    for x in range(28,49):
        drawMap(2,x,mountIco)
    for y in range(3,29):
        drawMap(y,1,mountIco)
    for y in range(3,27):
        drawMap(y,48,mountIco)
    
    

    drawMap(3,2,mountIco)
    drawMap(4,2,mountIco)
    drawMap(3,3,mountIco)

    drawMap(3,47,mountIco)
    drawMap(4,47,mountIco)
    drawMap(3,46,mountIco)
    
def printSea():
    for i in range(1,49):
        drawMap(28,i,waterIco)
        drawMap(27,i,waterIco)

def printRiver():
    for x in range(21,26):
        for y in range(20,27):
            drawMap(y,x,waterIco)
    for x in range(20,24):
        for y in range(14,20):
            drawMap(y,x,waterIco)
    for x in range(19,22):
        for y in range(8,14):
            drawMap(y,x,waterIco)
    for x in range(18,20):
        for y in range(5,8):
            drawMap(y,x,waterIco)
    for x in range(18,19):
        for y in range(1,5):
            drawMap(y,x,waterIco)

def printSand():
    for i in range(1,49):
        drawMap(26,i,sandIco)
        drawMap(25,i,sandIco)
    for i in range(30,49):
        drawMap(24,i,sandIco)
    # drawMap(25,45,sandIco)

def printQuests():
    # Première quete
    drawMap(25,27,questIco)
    # Deuxieme quete
    drawMap(10,48,questIco)
    # Troisieme quete
    drawMap(20,10,questIco)
    # Porte finale
    drawMap(1,20,questIco)

def fondMap():
    for i in range(len(var.map)):
        for j in range(len(var.map[i])):
            var.map[i][j] = florIco


# Position = f"{Prefix}{Y};{X}{Position_Suffix}"
#      print(f"{Position}{icon} ", end="")

def affichageMap(map,poY = 0,poX = 0):
    
    for poY in range(len(map)):
        for poX in range(len(map[poY])):
            if(poX == 0):
                print()
            Position = f"{prefix}{poY};{poX}{positionSuffix}"
            print(f"{Position}{map[poY][poX]}")    

            # print(map[poY][poX], end ="")
            
                # print(f" valeur de remvove = {remove}")

def printPos(Y,X,icon):
    Position = f"{prefix}{Y};{X}{positionSuffix}"
    print(f"{Position}{icon} ", end="")     

def printHud():
    printPos(1,73,var.title)
    printPos(4,55,var.eat)
    printPos(8,55,var.energy)
    printPos(12,55,var.water)
    printPos(17,75,var.inventory)
    printPos(19,55,var.inventoWater)
    printPos(23,55,var.inventoFood)

    printBar(5,56,eatingList,iconSurvie,red)
    printBar(9,56,staminaList,iconSurvie,green)
    printBar(13,56,drinkingList,iconSurvie,blue)

    printRessources(21,56,inventoryFoodBack,survieWaterIco)
    printRessources(21,56,inventoryWater,waterIco)
    printRessources(25,56,inventoryFoodBack,survieWaterIco)
    printRessources(25,56,inventoryFood,survieFoodIco)
    


    for i in range(51,110):
        printPos(3,i,barrehori)
    for i in range(51,110):
        printPos(16,i,barrehori)


    for i in range (1,30):             
        printPos(i,50,borderIco)
    # for i in range(50,110):
    #     printPos(1,i,borderIco)
    # for i in range(50,110):
    #     printPos(29,i,borderIco)
    # for i in range (1,30):             
    #     printPos(i,110,borderIco)

    for i in range (1,160):             
        printPos(30,i,borderIco)
    # for i in range (31,36):             
    #     printPos(i,1,borderIco) 
    # for i in range (31,36):             
    #     printPos(i,159,borderIco)

    for i in range (31,35):
        printPos(i,23,barreverti) 
    for i in range (31,35):
        printPos(i,54,barreverti)  
    for i in range (31,35):
        printPos(i,94,barreverti)  
    for i in range (1,160):             
        printPos(34,i,barrehori)
    for i in range (1,160):             
        printPos(36,i,barrehori)

def delRessource():
    del eatingList[-1]
    del drinkingList[-1]
    del staminaList[-1]
    del staminaList[-1]
    
def spleeping():
    pass  


quest = "start"
def moveplayer():

    startPosY = 25
    startPosX = 45
    currentPos = sandIco
    moveCounter = 0
    func.clearConsole()
    
    drawMap(startPosY,startPosX,playIco)
    drawMap(26,46,survieFoodIco)
    drawMap(22,40,waterIco)
    drawMap(20,45,mountIco)
    affichageMap(var.map)
    printHud()

    # affichePlayer(startPosY,startPosX)
    
    while quest != "end":

        moving = input("Que faire ? : ").upper()
        print()
        print(moving) 

        if moving == "Z":  
            if len(staminaList) < 5:
                print("Tu dois te reposer !")
            elif len(eatingList) < 2:
                print("Tu dois manger !")
            elif len(drinkingList) < 2:
                print("Tu dois boire !")
            else:
                
                oldIco = var.map[startPosY-1][startPosX]
                startPosY -= 1 
                moveCounter += 1
                func.clearConsole()
                # hud.printHudTop()
                
                drawMap(startPosY +1,startPosX,currentPos)  
                drawMap(startPosY,startPosX,playIco)
                affichageMap(var.map)
                delRessource() 
                if(moveCounter%2 == 0):
                    del staminaList[-1]
                afficheDep = f"Nombre de déplacements : {moveCounter}"
                printPos(32,26,afficheDep)
                posXY = f"X = {startPosX} | Y = {startPosY}"
                printPos(32,5,posXY)

                printHud()
                currentPos = oldIco
                oncase = f"Tu es sur la case {currentPos}"
                printPos(35,135,oncase)

            

        if moving == "S":
            if len(staminaList) < 5:
                print("Tu dois te reposer !")
            elif len(eatingList) < 2:
                print("Tu dois manger !")
            elif len(drinkingList) < 2:
                print("Tu dois boire !")
            else:
                oldIco = var.map[startPosY+1][startPosX]
                startPosY += 1 
                moveCounter +=1
                func.clearConsole()
                drawMap(startPosY -1,startPosX,currentPos)  
                drawMap(startPosY,startPosX,playIco)
                affichageMap(var.map) 
                delRessource() 
                if(moveCounter%2 == 0):
                    del staminaList[-1]
                afficheDep = f"Nombre de déplacements : {moveCounter}"
                printPos(32,26,afficheDep)
                posXY = f"X = {startPosX} | Y = {startPosY}"
                printPos(32,5,posXY)

                printHud()
                currentPos = oldIco
                oncase = f"Tu es sur la case {currentPos}"
                printPos(35,135,oncase)

        if moving == "Q":
            if len(staminaList) < 5:
                print("Tu dois te reposer !")
            elif len(eatingList) < 2:
                print("Tu dois manger !")
            elif len(drinkingList) < 2:
                print("Tu dois boire !")
            else:
                oldIco = var.map[startPosY][startPosX-1]
                startPosX -= 1 
                moveCounter +=1
                func.clearConsole()
                drawMap(startPosY,startPosX +1,currentPos)  
                drawMap(startPosY,startPosX,playIco)
                affichageMap(var.map) 
                delRessource() 
                if(moveCounter%2 == 0):
                    del staminaList[-1]
                afficheDep = f"Nombre de déplacements : {moveCounter}"
                printPos(32,26,afficheDep)
                posXY = f"X = {startPosX} | Y = {startPosY}"
                printPos(32,5,posXY)

                printHud()
                currentPos = oldIco
                oncase = f"Tu es sur la case {currentPos}"
                printPos(35,135,oncase)

        if moving == "D":
            if len(staminaList) < 5:
                print("Tu dois te reposer !")
            elif len(eatingList) < 2:
                print("Tu dois manger !")
            elif len(drinkingList) < 2:
                print("Tu dois boire !")
            else:
                oldIco = var.map[startPosY][startPosX+1]
                startPosX += 1 
                moveCounter +=1
                func.clearConsole()
                drawMap(startPosY,startPosX -1,currentPos)  
                drawMap(startPosY,startPosX,playIco)
                affichageMap(var.map) 
                delRessource() 
                if(moveCounter%2 == 0):
                    del staminaList[-1]
                afficheDep = f"Nombre de déplacements : {moveCounter}"
                printPos(32,26,afficheDep)
                posXY = f"X = {startPosX} | Y = {startPosY}"
                printPos(32,5,posXY)

                printHud()
                currentPos = oldIco
                oncase = f"Tu es sur la case {currentPos}"
                printPos(35,135,oncase)

        if moving == "E":           
            if currentPos == survieFoodIco:
                if len(inventoryFood) > 9:
                    print("Tu n'as plus de places pour cette nourriture")
                else:
                    func.clearConsole()
                    print("Tu ramasse de la nourriture !")
                    inventoryFood.extend([0])               
                     
                    currentPos = survieWaterIco
                    affichageMap(var.map)
                    printPos(32,5,posXY)
                    printPos(32,26,afficheDep)
                    printPos(35,135,oncase)
                    printHud()
            elif currentPos == waterIco:
                if len(inventoryWater) > 9:
                    print("Tu n'as plus de places pour cette eau")
                else:
                    func.clearConsole()
                    print("Tu prends de l'eau !")
                    inventoryWater.extend([0])
                    
                    currentPos = survieWaterIco
                    affichageMap(var.map)
                    printHud()
            else:
                print("Il n'y a rien à ramasser...")

        if moving == "C":
            print("Tu te repose...")
            lenStamina = len(staminaList)
            reloadStamina = 50 - lenStamina
            countStam = 0
            
            for i in range(reloadStamina):
                countStam += 1 
                
                if countStam % 6 == 0:
                    print(countStam)
                    del drinkingList[-1]
                    del drinkingList[-1]
                    del eatingList[-1]
                    func.clearConsole()
                    affichageMap(var.map)
                if len(eatingList) < 2:
                    
                    affichageMap(var.map)
                    printHud()
                    print("Tu dois manger !")
                    break
                elif len(drinkingList) < 2:
                    affichageMap(var.map)
                    printHud()
                    print("Tu dois boire !")
                    break
                       
                staminaList.extend([0])
                
                printHud()
             
                

        if moving == "B":
            if inventoryWater == []:
                print("Tu ne peux pas boire")
            else:
                if len(drinkingList) > 45:
                    print("Tu n'as pas soif...")
                else:
                    del inventoryWater[-1]
                    drinkingList.extend([0,0,0,0,0])
                    printHud() 
                    print("Tu bois !")

        if moving == "M":
            # print("Tu manges !")
            if inventoryFood == []:
                print("Tu ne peux pas manger")
            else:
                if len(eatingList) > 45:
                    print("Tu n'as pas faim...")
                else:
                    del inventoryFood[-1]
                    eatingList.extend([0,0,0,0,0])
                    printHud() 
                    print("Tu manges !")

        if(startPosY == 25 and startPosX == 27):
            print()
            print("Tu es sur la première quete")
            question = input("Veux tu lancer la quete O -> Oui | N -> Non : ").upper()
            if(question == "O"):
                print("Tu lance la quete")
                import nbrmystere as nbrM
                nbrM.nbrMyst()
            else:
                print("Passe ton chemin")

        


        commande = f"Déplacement -> Z Q S D ; Rammasser -> E ; Dormir -> C ; Boire -> B ; Manger -> M"
        printPos(35,2,commande)
        cursor = ""
        printPos(37,2,cursor)
        

# def ClearConsole():
#     """
#         Clear the console depending on OS
#     """

#     if "win" in sys.platform.lower():
#         # for windows
#         os.system("cls")
#     elif "linux" in sys.platform.lower():
#         # for linux
#         os.system("clear")



# affichePlayer(posY = 25,posX = 45)

# affichageMap(map)
fondMap()
randomSurvie()
printSea()
printSand()
printMount()
printRiver()
printQuests()
printBorderMap()

moveplayer()
# printHud()