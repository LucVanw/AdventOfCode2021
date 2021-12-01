#!/usr/bin/python3
import csv
increased = 0
index = 0
last = 1000000
rows = 0
with open('input.txt') as f:
    cr = csv.reader(f)
    crlist = list(cr)
    for index in range(len(crlist)):
        if index < 2 :
            index += 1
        else :
            row3 = int(crlist[index][0])
            row2 = int(crlist[index-1][0])
            row1 = int(crlist[index-2][0])
            index += 1
            rows = row3 + row2 + row1
            if rows > last:
                increased += 1
                last = rows
            else:
                last = rows
        line = f"{index} : {rows} : {increased}"
        print(line)

final = f"Maximum :  {increased}"
print(final)
