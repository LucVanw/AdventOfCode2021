#!/usr/bin/python3

class Board:
    matrix = []
    marked = []
  
    def __init__(self, matrix):
        self.matrix = matrix
        self.marked = [[0 for x in range(5)] for y in range(5)]

    def is_winner(self):

        for column in range(0,len(self.marked)):
            addition_line = 0
            addition_column = 0
            for line in range(0,len(self.marked[column])):
                if  self.marked[column][line] == 1:
                    addition_line +=1
                if  self.marked[line][column] == 1:
                    addition_column +=1
                
            if (addition_line == 5 or addition_column == 5):
                return True
        #print(f"Marked : {self.marked}")
        #print(f"Line : {addition_line}  | Column : {addition_column}")
        return False
    
    def sum_unmarked(self):
        sum_of_unmarked = 0
        for column in range(5):
            for line in range(5):
                if self.marked[column][line] == 0:
                    sum_of_unmarked += self.matrix[column][line]
        return sum_of_unmarked
        

        
    def mark(self, marked_number):
        for column in range(0,len(self.marked)):
            for line in range(0,len(self.marked[column])):
                if (self.matrix[column][line] == marked_number):
                    self.marked[column][line] = 1
        return self.marked


def file_to_matrices(data):

    matrices = []
    for line in range(2,len(rows),6):
        matrix = []
        for index in range(5):
            matrix.append(list(map(int, rows[line+index].split())))
        matrix = Board(matrix)
        matrices.append(matrix)
    return matrices


with open('input.txt') as f:
    rows = f.readlines()
    commands = rows[0].split(",")
    print(f"Commands : {commands}")
    matrices = file_to_matrices(rows)
    for command in commands:
        command = int(command)
        print(f"Command : {command}")
        for matrix in matrices:
            matrix.mark(command)
            if matrix.is_winner():
                 print(f"Matrice Gagnante : {matrix.matrix}")
                 print(f"Matrice Marked : {matrix.marked}")
                 print(f"Sum of Unmarked : {matrix.sum_unmarked()}")
                 print(f"Result : {matrix.sum_unmarked() * command}")
                 break;
        if matrix.is_winner():
            break;
