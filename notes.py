#!/usr/bin/python3

import os
import sys

NOTES_DIR = "/home/arthur/Documents/notes"

if __name__ == "__main__":
    try:
        if sys.argv[1] == "-l":
            for dirs in os.listdir(NOTES_DIR):
                print(dirs)
    except:
        print("notes -l             // Lists notes")
        print("notes -e <editfile>  // edits note")
        print("notes -s             // select note")
