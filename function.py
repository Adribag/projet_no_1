import os, sys
import random


def clearConsole():
    """
        Clear the console depending on OS
    """

    if "win" in sys.platform.lower():
        # for windows
        os.system("cls")
    elif "linux" in sys.platform.lower():
        # for linux
        os.system("clear")


def randomSurvie(map,food,water):
    """
        Affiche sur la map des emplacements de nourriture et d'eau
        - map -> La map sur laquelle il faut dessiner
        - food -> Icone de nourriture
        - water -> Icone d'eau
    """
    for i in range(0,80):
        randY = random.randint(3,27)
        randX = random.randint(3,45)
        drawMap(map,randY,randX,food)
    for i in range(0,80):
        randY = random.randint(3,27)
        randX = random.randint(3,45)
        drawMap(map,randY,randX,water)


def drawMap(map,posY,posX,symb):
    """
        Dessine sur une case donnée de la map
        - map -> La map sur laquelle il faut dessiner
        - posY -> La position en Y
        - posX -> La position en X
        - symb -> Le symbole a dessiner sur la map
    """
    map[posY][posX] = symb