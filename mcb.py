#! python3
# mcb.py - Saves and loads pieces of text to clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.


import sys, pyperclip, shelve

shelfFile = shelve.open("mcb")

if sys.argv[1] == "save":
    content = pyperclip.paste()
    shelfFile[sys.argv[2]] = content
elif sys.argv[1] == "list":
    pyperclip.copy(str(list(shelfFile.keys())))
else:
    pyperclip.copy(shelfFile[sys.argv[1]])

selfFile.close()