import os, sys
# import map 
emojiBorder = ""
borderHud = "⚪"


prefix = "\x1b["
positionSuffix = "H"

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


def main():
    os.system("")
    ClearConsole()
    
    printHudLineHeader(5,5,30,borderHud)

    printHudLineTop(1,1,borderHud)

    printHudLineBottom(40,1,borderHud)


    

    for i in range(40):
        printHudCol(i,1,borderHud) 
    
    # for i in range(25):
    #     printHudCol(i,20,borderHud) 
          
    # for i in range(25):
    #     printHudCol(i,120,borderHud)

    for i in range(40):
        printHudCol(i,70,borderHud)
    
    # for i in range(105,145):
    #     printHudCol(12,i,borderHud)

    # printPosMap(5,5)
        

    

def printHudLineTop(y = None, x = None, afficheVar = None):
    position = f"{prefix}{y};{x}{positionSuffix}"
    print(f"{position}{afficheVar*99}")
    # print("\x1b[0H")

def printHudLineBottom(y = None, x = None, afficheVar = None):
    position = f"{prefix}{y};{x}{positionSuffix}"
    print(f"{position}{afficheVar*100}")
    # print("\x1b[0H")
def printHudLineHeader(y = None, x = None,number = None, afficheVar = None):
    position = f"{prefix}{y};{x}{positionSuffix}"
    print(f"{position}{afficheVar*number}")

def printHudCol(y = None, x = None, afficheVar = None):
    position = f"{prefix}{y};{x}{positionSuffix}"
    print(f"{position}{afficheVar}")

# def printPosMap(y = None, x = None):
#     position = f"{prefix}{y};{x}{positionSuffix}"
   
    # map.moveplayer()
    # print("\x1b[0H")
# def firstSeparator(y = None, x = None, afficheVar = None):
#     position = f"{prefix}{y};{x}{positionSuffix}"
#     print(f"{position}{afficheVar}")
# Code starts here
if __name__ == "__main__":
    main()
    print()