#! python3
# pw.py - An insecure password locker program

import sys, pyperclip

PASSWORDS = {"facebook": "Kqiangaritina5!",
             "email": "garitina5",
             "luggage": "12345"}

if len(sys.argv) < 2:
    print("Usage: py pw.py[account] - copy account password")
    sys.exit()


account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("Invalid account")