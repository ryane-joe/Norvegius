import colorama
from colorama import Fore
import os
import subprocess
def cls():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')

def rainbow_text(text):
    """
    lopps throught all characters in the given prompt then return it with color 
    """
    colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN, colorama.Fore.CYAN, colorama.Fore.BLUE, colorama.Fore.MAGENTA]
    rainbow_text = ""

    color_index = 0
    for char in text:
        if char != " " and char != "\n":
            rainbow_text += colors[color_index] + char
            color_index = (color_index + 1) % len(colors)
        else:
            rainbow_text += char

    return rainbow_text + colorama.Style.RESET_ALL

def banner():
    """
    returns the banner with the rainbow color
    """

    return rainbow_text(r"""
    ▐ ▄       ▄▄▄   ▌ ▐·▄▄▄ . ▄▄ • ▪   ▄▄· ▄• ▄▌.▄▄ ·       __             _,-"~^"-.
    •█▌▐█▪     ▀▄ █·▪█·█▌▀▄.▀·▐█ ▀ ▪██ ▐█ ▌▪█▪██▌▐█ ▀.     _// )      _,-"~`         `.
    ▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█▐█•▐▀▀▪▄▄█ ▀█▄▐█·██ ▄▄█▌▐█▌▄▀▀▀█▄   ." ( /`"-,-"`                 ;
    ██▐█▌▐█▌.▐▌▐█•█▌ ███ ▐█▄▄▌▐█▄▪▐█▐█▌▐███▌▐█▄█▌▐█▄▪▐█  / 6                             ;
    ▀▀ █▪ ▀█▄▀▪.▀  ▀. ▀   ▀▀▀ ·▀▀▀▀ ▀▀▀·▀▀▀  ▀▀▀  ▀▀▀▀  /           ,             ,-"     ;
        Written By @vertion#1796 & @glych#0018      (,__.--.      \           /        ;
                                                        //'   /`-.\   |          |        `._________
                                                        _.-'_/`  )  )--...,,,___\     \-----------,)
                                                    ((("~` _.-'.-'           __`-.   )         //
                                                        ((("`             (((---~"`         //
    """)


def menu():
    """
    prints th banner plus the menu with the rain bow color effect
    """
    
    print(f"""{banner()}\n{rainbow_text('''
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃1. Password extraction             ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃2. Start Keylogger                 ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃3. Message Box                     ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃4. Webcam pic                      ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃5. Admin check                     ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃6. GeoLocate                       ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃7. Block Input                     ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃8. Unblock Input                   ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃9. PANIC!                          ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃10. Shell access                   ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃11. Maintain Access                ┃
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
    ┃12. Home                           ┃
    ┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙''')}""")
