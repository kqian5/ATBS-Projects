#! python3
# renameDates.py - Renames filenames from MM-DD-YYYY(American) to DD-MM-YYYY(European)

import re, os, shutil


aDates = re.compile(r'''^(.*?)((0|1)?\d)-((O|1|2|3)?\d)-((19|20)?\d\d)(.*?)$''')

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    for file in filenames:
        result = aDates.search(file)
        if result != None:
            european = str(group(1) + group(4) + "-" + group(2) + "-" + group(6) + group(8))
            pathname = os.path.abspath(".")
            amerFile = os.path.join(pathname, file)
            euroFile = os.path.join(pathname, european)
            shutil.move(amerFile, euroFile)


