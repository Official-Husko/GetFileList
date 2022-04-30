import os
from termcolor import colored
from datetime import date
from time import sleep
import sys
import random
import string

today = str(date.today())
version = "1.0.0"
folder = os.listdir()
id = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(4))

os.system('cls')
print(colored("======================================================================================================================", "red"))
print(colored("|                                                                                                                    |", "red"))
print(colored("|     " + colored("Product: GetFileList", "white") + colored("                                                                                    |", "red"), "red"))
print(colored("|     " + colored("Version: ", "white") + version + colored("                                                                                                 |", "red"), "red"))
print(colored("|     " + colored("Description: Get all files from a directory fast", "white") + colored("                                                               |", "red"), "red"))
print(colored("|                                                                                                                    |", "red"))
print(colored("======================================================================================================================", "red"))
print("")
print("Found " + colored(len([name for name in os.listdir('.') if os.path.isfile(name)]), "green") + " file in the current directory.")
print("")
print("Writing all found filenames to the text file. Filename: " + id + " - " + today + ".txt")
print("")
with open(id + " - " + today + ".txt", "w") as file:
    for files in folder:
        file.write(files + "\n")
    file.close()
print(colored("Done!", "green"))
sleep(10)
sys.exit(0)