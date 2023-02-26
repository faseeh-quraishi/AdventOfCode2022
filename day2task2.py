f = open('day2.txt','r')
lines = f.readlines()
score = 0
rock= 1
paper = 2
scissor = 3
Win = 6
Draw = 3
Lose = 0
for line in lines:
    if line[0] == 'A':
        if line[2] == 'X':
            score +=  (scissor + Lose)
        elif line[2] == 'Y':
            score += (rock + Draw)
        elif line[2] == 'Z':
            score += (paper + Win)


    elif line[0] == 'B':
        if line[2] == 'X':
            score += (rock + Lose)
        elif line[2] == 'Y':
            score += (paper + Draw)
        elif line[2] == 'Z':
            score += (scissor + Win)


    elif line[0] == 'C':
        if line[2] == 'X':
            score += (paper + Lose)
        elif line[2] == 'Y':
            score += (scissor + Draw)
        elif line[2] == 'Z': 
            score += (rock + Win)
print(score)
f.close()