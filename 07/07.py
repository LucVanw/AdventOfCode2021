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
        fuel += abs(position - crab)
    return fuel

with open('input.txt') as f:
    rows = f.readlines()
    crabs = format_file(rows)
    minimum_fuel = 10000000000000000
    
    for position in range(max(crabs)):
        fuel = consumption(crabs,position)
        if fuel < minimum_fuel and fuel != 0:
            minimum_fuel = fuel
        print(f"Fuel : {fuel}")
    
    print(f"Resultat : {minimum_fuel}")
