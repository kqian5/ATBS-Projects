#! python3
# removeCsvHeader.py - removes the heading or first row from all csv files in the cwd

import csv, os

csvFiles = []

os.makedirs("headerRemoved", exist_ok=True)

for file in os.listdir("."):
    if file.endswith(".csv"):
        csvFiles.append(file)

for csvFileName in csvFiles:
    csvFile = open(csvFileName)
    reader = csv.reader(csvFile)
    csvRows = []
    for row in reader:
        if reader.line_num == 1:
            continue
        else:
            csvRows.append(row)

    resultFile = open(os.path.join("headerRemoved", csvFileName), "w", newline="")
    writer = csv.writer(resultFile)
    for row in csvRows:
        writer.writerow(row)
    csvFile.close()
    resultFile.close()
