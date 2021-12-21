import sys, time
import colorama; from colorama import Fore; colorama.init()

GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
RESET = Fore.WHITE

GREEN2 = Fore.LIGHTGREEN_EX
RED2 = Fore.LIGHTRED_EX
BLUE2 = Fore.LIGHTBLUE_EX
CYAN = Fore.LIGHTCYAN_EX
YELLOW2 = Fore.LIGHTYELLOW_EX
MAGENTA2 = Fore.LIGHTMAGENTA_EX
RESET = Fore.LIGHTWHITE_EX

def write_color(arg= str ,color = Fore.WHITE, new_line = True, speed= 0.04):
    """*Narrating function*"""
    arg = f"{color}{arg}"
    if new_line:
        arg += f"\n{Fore.WHITE}"
    for char in arg:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()


def write_chars(name= str, arg = str, color= [False, None]):
    if name.lower().startswith("ansi"):
        color[0] = True
        color[1] = GREEN2
    if color[0] is True:
        arg = f"{color[1]}{arg}"
    write_color(f"{name.title()}: ", new_line= False)
    write_color(f"{Fore.WHITE}{arg}")


def write_narrator(arg= str, new_line= True, speed = 0.03):
    arg = f"{Fore.BLUE}{arg}"
    if new_line:
        arg += f"\n{Fore.WHITE}"
    for char in arg:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()
    

    

def point_loop(times= int, color= Fore.LIGHTBLACK_EX):
    for i in range(times):
        sys.stdout.write(f"{color}·\n{Fore.WHITE}")
        time.sleep(0.5)
