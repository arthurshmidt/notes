#!/usr/bin/python3

import os
import sys

NOTES_DIR = "/home/arthur/Documents/notes"

def print_help():
    print("notes <no arguments> // list notes")
    print("notes -l             // Lists notes")
    print("notes -e <editfile>  // edits note")
    print("notes -s             // select note")
    print("notes -h             // list help")

if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            for dirs in os.listdir(NOTES_DIR):
                print(dirs)
        elif sys.argv[1] == "-l":
            for dirs in os.listdir(NOTES_DIR):
                print(dirs)
        elif sys.argv[1] == "-e":
            os.system("vim "+ NOTES_DIR + "/" + sys.argv[2])
        elif sys.argv[1] == "-h":
            print_help()
        elif sys.argv[1] in os.listdir(NOTES_DIR):
            os.system("cat "+ NOTES_DIR + "/" + sys.argv[1])
    except:
        print_help()
