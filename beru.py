import os
import sys
from termcolor import colored

def arise():
    name = input(colored("Give me the name: ", "cyan", attrs=["bold"]))
    os.system(f"nvim ~/.beru/{name}")

def vanish():
    print(colored("[⚠] Removing a note...", "red", attrs=["bold"]))
    name = input(colored("Give me the name: ", "yellow", attrs=["bold"]))
    os.system(f"rm -rf ~/.beru/{name}")

def miseru():
    print(colored("[📜] Listing all notes...", "magenta", attrs=["bold"]))
    os.system("ls ~/.beru")

def hakaisuru():
    print(colored("[⚠] WARNING: Deleting ALL notes!", "red", attrs=["bold", "blink"]))
    os.system("rm -rf ~/.beru")
    print(colored("[✔] All notes deleted successfully!", "green", attrs=["bold"]))

def shadow():
    print(colored("[👤] Entering the shadow realm...", "dark_grey", attrs=["bold"]))
    os.system("cd ~/.berushadownigga")

def main():
    if len(sys.argv) != 2:
        print(colored("\nUsage:", "yellow", attrs=["bold"]))
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
        print(colored("[✖] Invalid keyword!", "red", attrs=["bold"]))

if __name__ == "__main__":
    main()
