#!/usr/bin/python3

def criteria(data, column, mode):
    addition = 0    
    for row in data:
        row=row.strip()
        if (row[column] == '0'):
            addition += 0
        else:
            addition += 1

    if mode == 'oxygen':
        if (addition == len(rows)/2):
            criteria=1
        elif (addition > len(rows)/2):
            criteria=1
        else:
            criteria=0
    elif mode == 'co2':
        if (addition == len(rows)/2):
            criteria=0
        elif (addition < len(rows)/2):
            criteria=1
        else:
            criteria=0
    else:
        return "error"
    return criteria

def remove_lines(data, column, bit_criteria):
    result = []
    for row in data: 
        if (int(row[column]) == bit_criteria):
            result.append(row)
        else:
            continue
    return result



with open('input.txt') as f:
    rows = f.readlines()
    for column in range(12):
        if (len(rows) == 1):
            print((f"Rows : {rows}"))
            break
        else:
            bit_criteria = criteria(rows, column, 'oxygen') 
            rows=remove_lines(rows, column, bit_criteria)
    oxygen = int(rows[0],2)
    
with open('input.txt') as f:
    rows = f.readlines()
    for column in range(12):
        if (len(rows) == 1):
            print((f"Rows : {rows}"))
            break
        else:
            bit_criteria = criteria(rows, column, 'co2') 
            rows=remove_lines(rows, column, bit_criteria)
    c02 = int(rows[0],2)
    print((f"Oxygen : {oxygen}"))
    print((f"CO2 : {c02}"))
    print((f"Result = {c02*oxygen}"))
