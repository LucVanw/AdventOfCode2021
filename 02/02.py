#!/usr/bin/python3
position = {'depth': 0, 'distance': 0}


def up(force):
    position['depth'] -= force
def down(force):
    position['depth'] += force
def forward(force):
    position['distance'] += force

options ={
'up': up,
'down': down,
'forward': forward,
}


with open('input.txt') as f:
    rows = f.readlines()
    for row in rows:
        row = row.split()
        command = row[0]
        force = int(row [1])
        options[command](force)
        print(f"Command : {row[0]} Number : {row[1]} Position : {position}")


print(f"Final Result : {position['depth']*position['distance']}")
