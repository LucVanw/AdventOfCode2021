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
        start_x = command[0][0]
        end_x = command[1][0]
        start_y = command[0][1]
        end_y = command[1][1]


        if start_y < end_y :
            step_y = 1
        else:
            step_y= -1

        if start_x < end_x :
            step_x = 1
        else:
            step_x= -1

        if start_x == end_x:
            x = start_x
            print(f"Line Horiz: {command}")
            for y in range (start_y,end_y+step_y,step_y):
                self.matrix[x][y] += 1
        elif start_y == end_y:
            print(f"Line Vert: {command}")
            y = start_y
            for x in range (start_x,end_x+step_x,step_x):
                self.matrix[x][y] += 1
        elif abs(end_y - start_y) == abs(end_x - start_x):
            print(f"Line Diag: {command}")
            for x in range (start_x,end_x+step_x,step_x):
                y= start_y + step_x*step_y*(x-start_x)
                self.matrix[x][y] += 1
        else:
            print(f"Line Not Horiz nor Vert nor Diag: {command}")
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
