#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for each county

import openpyxl, pprint
wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb.get_sheet_by_name("Population by Census Tract")

countiesData = {}

for row in range(2, sheet.max_row  + 1):
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value

    countiesData.setdefault(state, {})
    countiesData[state].setdefault(county, {"tracts": 0, "pop": 0})

    countiesData[state][county]["tracts"] += 1
    countiesData[state][county]["pop"] += int(pop)

resultFile = open("census2010.py", "w")
resultFile.write("alldata = " + pprint.pformat(countiesData))
resultFile.close()
