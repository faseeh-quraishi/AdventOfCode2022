f = open("day3.txt",'r')
lines = f.readlines()
NoOfItems = 0
score = 0
for line in lines:
    NoOfItems = len(line)
    section = int(NoOfItems/2)
    for item in line[0:section]:
        if (item in line[section:NoOfItems]) and (123>ord(item)>96):
            score += (ord(item)-96)
            break
        elif (item in line[section:NoOfItems]) and (91>ord(item)>64):
            score += (ord(item)-(64)+26)
            break
        # else:
        #     pass
print(score)


f.close()
