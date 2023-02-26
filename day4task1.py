f = open('day4.txt')
lines = f.readlines()
# sections = []
counter = 0
for line in lines:
    sections = line[:-1].split(',')
    for i in range(len(sections)):
        sections[i] = sections[i].split('-')

    if (int(sections[0][0]) <= int(sections[1][0])) and (int(sections[0][-1]) >= int(sections[1][-1])):
        counter +=1
    elif (int(sections[1][0]) <= int(sections[0][0])) and (int(sections[1][-1]) >= int(sections[0][-1])):
        counter +=1
print(counter)

f.close()