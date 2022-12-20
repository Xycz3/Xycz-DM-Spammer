import time
import pyautogui as auto
from time import sleep 
import colorama
from colorama import Fore, Style
colorama.init()

print()
print('\033[37m' + '𝐌𝐚𝐝𝐞 𝐁𝐲 𝐗𝐲𝐜𝐳')
print("""__   ____   __ _____  ______
\ \ / /\ \ / //  __ \|___  /
 \ V /  \ V / | /  \/   / / 
 /   \   \ /  | |      / /  
/ /^\ \  | |  | \__/\./ /___
\/   \/  \_/   \____/\_____/
                            
                            """)

print()
print("Press {Enter} to write the message you wanna spam!")
input()
Sp = input("What you wanna spam?: ")
print()
Ac = input("PRESS {ENTER} TO SPAM")
print()
while True:
        auto.write(Sp)          
        auto.press('enter')
        sleep(0.001)  
