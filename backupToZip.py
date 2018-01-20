#! python3
# backuptoZip.py - copies an entire folder into a zip file and increments the filename

import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number += 1
    result = zipfile.ZipFile(zipFilename, "w")
    for folderName, subfolders, filenames in os.walk(folder):
        print("Adding files in %s..." % folderName)
        result.write(folderName)
        for f in filenames:
            base = os.path.basename(folder) + "_"
            if f.startswith(base) and f.endswith(".zip"):
                continue
            result.write(os.path.join(folderName, f))
    result.close()