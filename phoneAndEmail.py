#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re


phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                  # area code
(\s|-|\.)                           # separator
(\d{3})                             # first 3 digits
(\s|-|\.)                           # separator 
(\d{4})                             # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
)''', re.VERBOSE)

emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2-4}')

text = pyperclip.paste()
result = []
for phoneNum in phoneRegex.findall(text):
    formatted = "-".join([phoneNum[1], phoneNum[3], phoneNum[5]])
    if phoneNum[8] != "":
        formatted += " x" + phoneNum[8]
    result.append(formatted)
for email in emailRegex.findall(text):
    result.append(email)



if len(result) > 0:
    pyperclip.copy("\n".join(result))
else:
    print("No matches found")

