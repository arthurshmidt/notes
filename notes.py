#!/usr/bin/python3

import os
import sys

NOTES_DIR = "/home/arthur/Documents/notes"

def add_dot_notes(file_name):
    return file_name+".notes" 

def remove_dot_notes(file_name):
    words = file_name.split('.')
    return words[0]

def print_help():
    print("notes <no arguments>         // list notes")
    print("notes -l                     // Lists notes")
    print("notes -d <note>              // delete note")
    print("notes -e <editfile>          // edits note")
    print("notes -s                     // select note")
    print("notes -h                     // list help")

if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            counter = 0
            for files in os.listdir(NOTES_DIR):
                counter = counter + 1
                print(str(counter)+". " + remove_dot_notes(files))
        elif sys.argv[1] == "-l":
            counter = 0
            for files in os.listdir(NOTES_DIR):
                counter = counter + 1
                print(str(counter) + ". " + remove_dot_notes(files))
        elif sys.argv[1] == "-e":
            os.system("vim "+ NOTES_DIR + "/" + add_dot_notes(sys.argv[2]))
        elif sys.argv[1] == "-h":
            print_help()
        elif sys.argv[1] == "-d":
            try:
                os.system("rm -f "+NOTES_DIR+"/"+add_dot_notes(sys.argv[2]))
            except:
                print("File does not exist.")
        elif add_dot_notes(sys.argv[1]) in os.listdir(NOTES_DIR):
            os.system("cat "+ NOTES_DIR + "/" + add_dot_notes(sys.argv[1]))
        elif add_dot_notes(sys.argv[1]) not in os.listdir(NOTES_DIR):
            if input("Create file "+add_dot_notes(sys.argv[1])+" (y/n): ") == "y":
                os.system("vim "+ NOTES_DIR + "/" + add_dot_notes(sys.argv[1]))
    except:
        print_help()
