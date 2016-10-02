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
        # If it's a file and not the last one, just print it with the offset
        if(os.path.isfile(os.path.join(currDir, content))):
            if(i < len(dirContentSorted) - 1):
                print(printOffset + "├── " + str(content))
            else:
                print(printOffset + "└── " + str(content))
            noOfFiles += 1

        # If it's a folder, then print the name of the folder with offset, and then recurse
        elif(os.path.isdir(os.path.join(currDir, content)) and i < len(dirContentSorted) - 1):
            if(i < len(dirContentSorted) - 1):
                print(printOffset + "├── " + str(content))
            else:
                print(printOffset + "└── " + str(content))
            noOfFolders += 1
            tree(os.path.join(currDir, content), printOffset + "│   ")

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
