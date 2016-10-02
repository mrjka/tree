#!/usr/bin/env python3
import subprocess
import sys
import os

noOfFiles = 0
noOfFolders = 0


# Recursively print the tree
def tree(currDir, printOffset):
    global noOfFiles
    global noOfFolders

    dirContent = [cont for cont in os.listdir(currDir) if not cont.startswith('.')]
    dirContentSorted = sorted(dirContent, key=lambda s: s.lower())

    # Loop through the content
    i = 0
    for content in dirContentSorted:
        if(i < len(dirContentSorted) - 1):
            print(printOffset + "├── " + str(content))
        else:
            print(printOffset + "└── " + str(content))

        # If it's a file add the total
        if(os.path.isfile(os.path.join(currDir, content))):
            noOfFiles += 1

        # If it's a folder, then increase the number and recurse
        elif(os.path.isdir(os.path.join(currDir, content)) and i < len(dirContentSorted) - 1):
            noOfFolders += 1
            tree(os.path.join(currDir, content), printOffset + "│   ")

        i += 1

# Print the first line
lenArg = len(sys.argv)
if(lenArg == 1):
    rootDir = "."
else:
    rootDir = str(sys.argv[1])
print(rootDir)
tree(rootDir, "")
print()
print(str(noOfFolders) + " directories, " + str(noOfFiles) + " files")
