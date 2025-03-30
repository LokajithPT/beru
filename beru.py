import getpass as gp
import os
import sys
import time
import random
from termcolor import colored

def type_out(text, color, delay=0.05, attrs=None):
    for char in text:
        print(colored(char, color, attrs=attrs), end='', flush=True)
        time.sleep(delay if char != ' ' else 0.02)
    print()

def arise():
    type_out("[👁] A name... GIVE ME A NAME...", "cyan", 0.1, ["bold"])
    name = input(colored("Give me the name: ", "cyan", attrs=["bold"]))
    os.system(f"nvim ~/.beru/{name}")

def vanish():
    type_out("[⚠] Do you understand what you are about to do...?", "red", 0.1, ["bold"])
    time.sleep(1)
    name = input(colored("Give me the name: ", "yellow", attrs=["bold"]))
    os.system(f"rm -rf ~/.beru/{name}")
    type_out("[✔] It is gone... but is it really?", "red", 0.05)

def miseru():
    type_out("[📜] Behold... the remnants of your mind...", "magenta", 0.08, ["bold"])
    os.system("ls ~/.beru")

def hakaisuru():
    type_out("[⚠] WARNING: THE VOID CONSUMES ALL...", "red", 0.08, ["bold", "blink"])
    time.sleep(1.5)
    os.system("rm -rf ~/.beru")
    type_out("[✔] They are gone... but the whispers remain.", "green", 0.06)

def shadow():
    type_out("[👤] The shadows call to you...", "dark_grey", 0.1, ["bold"])
    passw = gp.getpass(colored("First, enter your password... ", "red", attrs=["bold"]))
    
    if passw == "lokihehe":
        type_out("[✔] You are... one of us.", "green", 0.08, ["bold"])
    else:
        type_out("[✖] You don't belong here... leave. NOW.", "red", 0.1, ["bold"])
        sys.exit(1)
    
    type_out("[📂] Peering into the abyss...", "dark_grey", 0.08)
    os.system("ls ~/.berushadownigga")
    name = input(colored("\n Name of your file: ", "green"))
    os.system(f"nvim ~/.berushadownigga/{name}")

def main():
    try:
        if len(sys.argv) != 2:
            type_out("\nUsage:", "yellow", 0.1, ["bold"])
            time.sleep(0.5)
            print(colored("  beru arise", "cyan"))
            print(colored("  beru vanish", "red"))
            print(colored("  beru miseru", "magenta"))
            print(colored("  beru hakaisuru", "red", attrs=["bold"]))
            print(colored("  beru shadow", "dark_grey"))
            sys.exit(1)
        
        argv = sys.argv[1]
        
        if argv == "arise":
            arise()
        elif argv == "vanish":
            vanish()
        elif argv == "miseru":
            miseru()
        elif argv == "hakaisuru":
            hakaisuru()
        elif argv == "shadow":
            shadow()
        else:
            type_out("[✖] The command... it does not exist here.", "red", 0.08, ["bold"])
    
    except KeyboardInterrupt:
        type_out("\n[✖] You tried to escape... but it’s already too late.", "red", 0.1, ["bold"])
        sys.exit(1)

if __name__ == "__main__":
    main()

