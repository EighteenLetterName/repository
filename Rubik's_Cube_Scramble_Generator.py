import random

moves = ["R", "L", "U", "D", "F", "B",
         "R'", "L'", "U'", "D'", "F'", "B'",
         "R2", "L2", "U2", "D2", "F2", "B2"]

len_scramble = 20

def shadow(move):
    if move[0] == "R":
        return "L"
    if move[0] == "L":
        return "R"
    if move[0] == "U":
        return "D"
    if move[0] == "D":
        return "U"
    if move[0] == "F":
        return "B"
    if move[0] == "B":
        return "F"

def scramble():
    scramble = []
    scramble.append(random.choice(moves)) 
    for i in range(len_scramble - 1):
        if scramble[i-1][0] == shadow(scramble[i]):
            scramble.append(random.choice([move for move in moves if (move[0] != scramble[i-1][0] and move[0] != scramble[i][0])]))
        else:
            scramble.append(random.choice([move for move in moves if move[0] != scramble[i][0]]))
    return ' '.join(scramble)
print(scramble())
