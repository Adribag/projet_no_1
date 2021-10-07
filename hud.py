import os, sys
emojiBorder = ""
borderHud = "🔲"


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

    printHudLineTop(1,1,borderHud)

    printHudLineBottom(35,1,borderHud)

    printHudLineBottom(25,1,borderHud)

    for i in range(35):
        printHudCol(i,1,borderHud) 
    
    for i in range(25):
        printHudCol(i,20,borderHud) 
          
    for i in range(25):
        printHudCol(i,120,borderHud)
    for i in range(35):
        printHudCol(i,155,borderHud)
    
    for i in range(105,145):
        printHudCol(12,i,borderHud)
    

    print()

def printHudLineTop(y = None, x = None, afficheVar = None):
    position = f"{prefix}{y};{x}{positionSuffix}"
    print(f"{position}{afficheVar*75}")
    # print("\x1b[0H")

def printHudLineBottom(y = None, x = None, afficheVar = None):
    position = f"{prefix}{y};{x}{positionSuffix}"
    print(f"{position}{afficheVar*76}")
    # print("\x1b[0H")

def printHudCol(y = None, x = None, afficheVar = None):
    position = f"{prefix}{y};{x}{positionSuffix}"
    print(f"{position}{afficheVar}")
    # print("\x1b[0H")
def firstSeparator(y = None, x = None, afficheVar = None):
    position = f"{prefix}{y};{x}{positionSuffix}"
    print(f"{position}{afficheVar}")
# Code starts here
if __name__ == "__main__":
    main()