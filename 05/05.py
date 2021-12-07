#!/usr/bin/python3


def format_file(rows):
    commands = []
    for row in rows:
        row = row.split("->")
        move = []
        for coordinate in row:
            coordinate=coordinate.strip()
            coordinate=coordinate.split(",")
            move.append(list(map(int,coordinate)))
        commands.append(move)
    return commands

class Board:
    matrix = []
  
    def __init__(self):
        self.matrix = [[0 for x in range(1000)] for y in range(1000)]

    def mark(self, command):
        if command[0][0] == command[1][0]:
            x = command[0][0]
            start = min([command[0][1],command[1][1]])
            end = max([command[0][1],command[1][1]])
            for y in range (start,end+1):
                self.matrix[x][y] += 1
        elif command[0][1] == command[1][1]:
            y = command[0][1]
            start = min([command[0][0],command[1][0]])
            end = max([command[0][0],command[1][0]])
            for x in range (start,end+1):
                self.matrix[x][y] += 1
        else:
            print(f"Line Not Horiz or Vert : {command}")
        return self.matrix

    def overlap(self):
        result=0
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix)):
                if self.matrix[x][y] > 1 :
                    result += 1
        return result


with open('input.txt') as f:
    rows = f.readlines()
    commands = format_file(rows)
    print(f"Commands : {commands}")
    board = Board()
    for command in commands:
        board.mark(command)
    print(f"Result : {board.overlap()}")
