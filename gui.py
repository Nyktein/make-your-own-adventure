import os
from typing import Any
def create_screen(title= str, options= []):
    var = ""
    for i in range(len(title)):
        var+="#"
    print("##" + var + "##")
    print("# " + title + " #")
    print("##" + var + "##")

    if options == []:
        pass
    else:
        if type(options[0]) == int:
            n= 1
            while options[0] >= n:
                print("- " + options[n])
                n+=1

def sum(a, b):
    print(a + b)
def check_election(then= str, par= Any):
    o67ption = input("Your election: ")

    if then == "print-text-clear":
        os.system("cls") #clear()
        print(par)
    elif then == "print-text-no-clear":
        print(par)
    elif then == "continue-game":
        par



create_screen("Foto Culo", [2, "Happy meal", "Kiero k seas mi nobio bb"])
