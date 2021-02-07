import time
import random
from colorama import init, Fore
import string
import ctypes

init(convert=True)
ctypes.windll.kernel32.SetConsoleTitleW("Amazon Gift Card Generator By NEWE")
text = '''
 ▄▄▄       ███▄ ▄███▓ ▄▄▄      ▒███████▒ ▒█████   ███▄    █   ▄████ ▓█████  ███▄    █ 
▒████▄    ▓██▒▀█▀ ██▒▒████▄    ▒ ▒ ▒ ▄▀░▒██▒  ██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒██  ▀█▄  ▓██    ▓██░▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██░  ██▒▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
░██▄▄▄▄██ ▒██    ▒██ ░██▄▄▄▄██   ▄▀▒   ░▒██   ██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
 ▓█   ▓██▒▒██▒   ░██▒ ▓█   ▓██▒▒███████▒░ ████▓▒░▒██░   ▓██░░▒▓███▀▒░▒████▒▒██░   ▓██░
 ▒▒   ▓▒█░░ ▒░   ░  ░ ▒▒   ▓▒█░░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
  ▒   ▒▒ ░░  ░      ░  ▒   ▒▒ ░░░▒ ▒ ░ ▒  ░ ▒ ▒░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░░ ░░   ░ ▒░
  ░   ▒   ░      ░     ░   ▒   ░ ░ ░ ░ ░░ ░ ░ ▒     ░   ░ ░ ░ ░   ░    ░      ░   ░ ░ 
      ░  ░       ░         ░  ░  ░ ░        ░ ░           ░       ░    ░  ░         ░ 
                               ░                                                      
'''

def gen(fix, amount):
    while fix <= amount:
        code = ('').join(random.choices(string.ascii_letters.upper() + string.digits.upper(), k=13))
        f.write(code.upper() + '\n')
        print(Fore.GREEN + code.upper())
        fix += 1
        ctypes.windll.kernel32.SetConsoleTitleW("Generated Codes: " + str(fix) + "/" + str(amount))

print(Fore.RED + text + Fore.WHITE)
f = open('amazon_codes.txt', 'a')
print()
print(Fore.RED + 'Enter amount of codes to generate: ')
amount = int(input())
gen(1, amount)
time.sleep(2)
