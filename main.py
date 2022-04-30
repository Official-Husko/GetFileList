import os
from click import argument
from termcolor import colored
from datetime import datetime
from time import sleep
import sys
from ctypes import windll

now = datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M:%S")
dtds = now.strftime("%d-%m-%Y %H-%M-%S")
version = "1.0.0"
folder = os.listdir()
files_list = []
dirs_list = []

seperator = "==================================\n"

if os.name == "nt":
    os.system('cls')
    windll.kernel32.SetConsoleTitleW("Husko's GetFileList | v" + version)
else:
    os.system('clear') 
print(colored("======================================================================================================================", "red"))
print(colored("|                                                                                                                    |", "red"))
print(colored("|     " + colored("Product: GetFileList", "white") + colored("                                                                                           |", "red"), "red"))
print(colored("|     " + colored("Version: ", "white") + version + colored("                                                                                                 |", "red"), "red"))
print(colored("|     " + colored("Description: Get all files & folders from a directory fast", "white") + colored("                                                     |", "red"), "red"))
print(colored("|                                                                                                                    |", "red"))
print(colored("======================================================================================================================", "red"))
print("")
print("Please enter the path to target folder.")
target = input(">> ")
if not os.path.join(target):
    print(colored("Invalid Path Provided!", "red"))
    sleep(2)
folder = os.listdir(target)
with open("GetFileList Report - " + dtds + ".log", "w") as file:
    for files in folder:
        if os.path.isfile(files):
            filepath = os.path.join(files)
            files_list.append(filepath)
        elif os.path.isdir(files):
            filepath = os.path.join(files)
            dirs_list.append(filepath)
        else:
            print(files)
    print("Files: " + str(files_list))
    print("Folders: " + str(dirs_list))
    """
    file.write(seperator)
    file.write("Generated using GetFileList by Husko ~ The right way to get & share a file list.\n")
    file.write("Source: https://github.com/Official-Husko/GetFileList\n")
    file.write("This report was generated at: " + dt + "\n")
    file.write(seperator)
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write(seperator)
    file.write("General Information\n")
    file.write(seperator)
    file.write("Directory Name: " + os.path.basename(target) + "\n")
    file.write("Directory Path: " + target + "\n")
    file.write("File Count: " + str(len(files_list)) + "\n")
    file.write("Directory Count: " + str(len(dirs_list)) + "\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write(seperator)
    file.write("Present Directories\n")
    file.write(seperator)
    for folder in dirs_list:
        file.write("[FOLDER] " + folder + "\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write(seperator)
    file.write("Present Files\n")
    file.write(seperator)
    for ffile in files_list:
        file.write("[FILE] " + ffile + "\n")
print(colored("Done!", "green"))
sleep(3)"""
sys.exit(0)

# TODO : add arguments like -help -json -path -recursive -crc32
# TODO : fix this broken shit