import os;import sys
def clear():
    OS = sys.platform

    if OS == "windows" or OS == "win32":
        os.system("cls")
    else:
        os.system("clear")