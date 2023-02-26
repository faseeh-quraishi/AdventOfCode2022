with open('day6.txt') as file:
    lines = [line.rstrip() for line in file]

    for i in range(len(lines[0])-4):
        a = lines[0][i]
        b = lines[0][i+1]
        c = lines[0][i+2]
        d = lines[0][i+3]
        if (a != b) & (a != c) & (a != d) & (b != c) & (b != d) & (c != d):
            print(i+4)
            break
