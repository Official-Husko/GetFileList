import os
from termcolor import colored
from datetime import datetime
from time import sleep
from sys import exit
from ctypes import windll
import argparse
import zlib
import json

now = datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M:%S")
dtds = now.strftime("%d-%m-%Y %H-%M-%S")
version = "1.0.0"
files_list = []
dirs_list = []
hash_list = []

parser = argparse.ArgumentParser(prog="GetFileList.exe", usage='%(prog)s [options]')
parser.add_argument('-p', '--path',
                    dest='path_to_target',
                    default="simple",
                    help='Path to Target',
                    type=str
                    )
parser.add_argument('-f', '--format',
                    dest='file_format',
                    default="plain",
                    help='output format. plain & json supported',
                    type=str
                    )
parser.add_argument('-hf', '--hash',
                    dest='calculate_hashes',
                    default="False",
                    help='calculate the hashes for all files. CRC32 only currently',
                    type=str
                    )
parser.add_argument('-ext', '--extention',
                    dest='file_ending',
                    default="log",
                    help='choose a prefered output extension e.g. log, txt',
                    type=str
                    )
args = parser.parse_args()

seperator = "==================================\n"

if os.name == "nt":
    os.system('cls')
    windll.kernel32.SetConsoleTitleW("Husko's GetFileList | v" + version)
print(colored("======================================================================================================================", "red"))
print(colored("|                                                                                                                    |", "red"))
print(colored("|     " + colored("Product: ", "white") + colored("GetFileList","green") + colored("                                                                                           |", "red"), "red"))
print(colored("|     " + colored("Version: ", "white") + colored(version,"green") + colored("                                                                                                 |", "red"), "red"))
print(colored("|     " + colored("Description: ", "white") + colored("Get all files & folders from a directory fast","green") + colored("                                                     |", "red"), "red"))
print(colored("|                                                                                                                    |", "red"))
print(colored("======================================================================================================================", "red"))
print("")
if args.path_to_target == "simple":
    print("Please enter the path to target folder.")
    target = input(">> ")
else: 
    target = args.path_to_target
if not os.path.join(target):
    print(colored("Invalid Path Provided!", "red"))
    sleep(2)
folder = os.listdir(target)
for files in folder:
    if os.path.isfile(target + "/" + files):
        if args.calculate_hashes == "CRC32":
            prev = 0
            for eachLine in open(target + "/" + files,"rb"):
                prev = zlib.crc32(eachLine, prev)
            hash = "%X"%(prev & 0xFFFFFFFF)
            hash_list.append(hash)
        files_list.append(files)
    elif os.path.isdir(target + "/" + files):
        dirs_list.append(files)
if args.file_format != "json":
    with open("GetFileList Report - " + dtds + f".{args.file_ending}", "w") as file:
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
        if args.calculate_hashes != "False":
            for ffile, hashes in zip(files_list, hash_list):
                file.write("[FILE] " + ffile + " " + str(hashes) + "\n")
        else:
            for ffile in files_list:
                file.write("[FILE] " + ffile + "\n")
else:
    if args.calculate_hashes != "False":
        json_scheme = {
            "info": {
                "Disclaimer": "Generated using GetFileList by Husko ~ The right way to get & share a file list.",
                "Source": "https://github.com/Official-Husko/GetFileList",
                "This report was generated at": dt,
            },
            "General Information": {
                "Directory Name": os.path.basename(target),
                "Directory Path": target,
                "File Count": str(len(files_list)),
                "Directory Count": str(len(dirs_list))
            },
            "Present Directories": dirs_list,
            "Present Files": {}
        }
        for ffile, hashes in zip(files_list, hash_list):
            json_scheme["Present Files"][ffile] = hashes
    else:
        json_scheme = {
            "info": {
                "Disclaimer": "Generated using GetFileList by Husko ~ The right way to get & share a file list.",
                "Source": "https://github.com/Official-Husko/GetFileList",
                "This report was generated at": dt,
            },
            "General Information": {
                "Directory Name": os.path.basename(target),
                "Directory Path": target,
                "File Count": str(len(files_list)),
                "Directory Count": str(len(dirs_list))
            },
            "Present Directories": dirs_list,
            "Present Files": files_list
        }
    with open("GetFileList Report - " + dtds + f".json", "w") as file:
        json.dump(json_scheme, file, indent = 6)
print(colored("Done!", "green"))
sleep(3)
exit(0)
