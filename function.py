import os, sys

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