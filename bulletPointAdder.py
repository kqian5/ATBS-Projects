#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

list = text.split("\n")
result = ""
for line in list:
    result = result + "* " + line + "\n"

pyperclip.copy(result)