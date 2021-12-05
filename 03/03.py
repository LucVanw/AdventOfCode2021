#!/usr/bin/python3
addition =[0,0,0,0,0,0,0,0,0,0,0,0]

with open('input.txt') as f:
    rows = f.readlines()
    for row in rows:
        index = 0
        for bit in row:
            if (bit == '0'):
                index += 1
            elif (bit == '1'):
                addition[index] += 1
                index += 1
            else : 
                pass
        print((f"Row : {row} Addition : {addition}"))
    
    gamma = ""
    epsilon = ""
    
    index = 0
    for bit in addition:
        if bit > len(rows)/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

print((f"Gamma : {gamma} Epsilon : {epsilon}"))

gamma_base10 = int(gamma,2)
epsilon_base10 = int(epsilon,2)

print((f"Gamma : {gamma_base10} Epsilon : {epsilon_base10}"))
print((f"Resultat : {gamma_base10*epsilon_base10}"))
