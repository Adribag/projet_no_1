import os, sys


borderHud = "⚪"
Prefix = "\x1b["
Position_Suffix = "H"
barreh = "─"
barrev = "│"
hg = "┌"
hd = "┐"
bg = "└"
bd = "┘"
def ClearConsole():
    """
        Clear the console depending on OS
    """

    if "win" in sys.platform.lower():
        # for windows
        os.system("cls")
    elif "linux" in sys.platform.lower():
        # for linux
        os.system("clear")



def printHudTop():
    # ClearConsole()

    # Contour
    # for i in range (1,161):
    #     printPos(1,i,barreh)
    
    # # for i in range (1,161):
    # #     printPos(51,i,barreh)

    # for i in range (1,36):
    #     printPos(i,1,barrev)
    
    # for i in range (1,51):
    #     printPos(i,161,barrev)

    # Rectangle verticale droit
    for i in range (1,100):
        printPos(1,i,borderHud)
    
    

    # printPos(2,40,hd)

    # printPos(30,2,bg)

    # printPos(30,40,bd)

    # for i in range (3,40):
    #     printPos(2,i,barreh)
    
    # for i in range (3,40):
    #     printPos(30,i,barreh)

    

    # Rectanlfe d'affochage de la map
    # printPos(2,51,hg)

    # printPos(30,51,bg)

    # printPos(2,200,hd)
    
    # printPos(50,200,bd)

    # for i in range (52,160):
    #     printPos(2,i,barreh)
    
    # for i in range (52,200):
    #     printPos(50,i,barreh)

    

    # for i in range (2,30):
    #     printPos(i,1,barrev)
    
    # for i in range(2,30):
    #     printPos(i,30,barrev)

    

    # for i in range (2,100):
    #     printPos(30,i,barreh)

def printHudSep():
    for i in range (1,34):
            printPos(i,55,barrev)


def printHudBot():
    for i in range (1,100):
            printPos(34,i,borderHud) 

    
def printPos(Y,X,icon):
     Position = f"{Prefix}{Y};{X}{Position_Suffix}"
     print(f"{Position}{icon}")


