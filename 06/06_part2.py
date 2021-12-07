#!/usr/bin/python3

def format_file(rows):
    commands = []
    for row in rows:
        row = row.split(",")
        for command in row:
            fish = int(command)
            commands.append(fish)
    return commands


with open('input.txt') as f:
    rows = f.readlines()
    commands = format_file(rows)
    print(f"Commands : {commands}")
    sea = [0,0,0,0,0,0,0,0,0]

    for command in commands:
        sea[command] += 1

    print(f"Sea : {sea}")

    for day in range(256):
        newsea = [0,0,0,0,0,0,0,0,0]
        for index in range(9):
            if index == 8:
                newsea[8] = sea[0]
                newsea[6] += sea[0] 
            else:
                newsea[index] = sea[index+1]
        sea = newsea
        print(f"sea : {sea}")
    print(f"Result : {sum(sea)}")
