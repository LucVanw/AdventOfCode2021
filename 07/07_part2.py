#!/usr/bin/python3

def format_file(rows):
    commands = []
    for row in rows:
        row = row.split(",")
        for command in row:
            commands.append(int(command))
    return commands

def consumption(crabs, position):
    fuel = 0
    for crab in crabs:
        #We calculate the sim 1+2+...+x  of crabs movement
        fact=0
        for move in range(1,abs(position - crab)+1):
            fact += move 
        fuel += fact
    return fuel

with open('input.txt') as f:
    rows = f.readlines()
    crabs = format_file(rows)
    minimum_fuel = float('inf')
    
    for position in range(max(crabs)):
        fuel = consumption(crabs,position)
        if fuel < minimum_fuel and fuel != 0:
            minimum_fuel = fuel
        else:
            print(f"Resultat : {minimum_fuel}")
            break
        print(f"Position : {position}")
    
