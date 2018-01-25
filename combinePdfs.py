#! python3
# combinePdfs.py - combines all pdfs in cwd into a single pdf

import PyPDF2, os

pdfs = []
for file in os.listdir("."):
    if file.endswith(".pdf"):
        pdfs.append(file)

pdfs.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for pdf in pdfs:
    pdfReader = PyPDF2.PdfFileReader(open(pdf, "rb"))
    for pageNum in range(pdfReader.numPages):
        if pageNum == 0:
            continue
        else:
            pdfWriter.addPage(pdfReader.getPage(pageNum))


resultPdf = open("allminutes.pdf", "wb")
pdfWriter.write(resultPdf)
resultPdf.close()