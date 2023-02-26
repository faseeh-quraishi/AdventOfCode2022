f = open('day5.txt')
lines = f.readlines()
StackNosLine = 8
Stacks = [[],[],[],[],[],[],[],[],[]]
Temp_List = []
for i in range(StackNosLine-1,-1,-1):
    if lines[i][0:3] != '   ':
        Stacks[0].append(lines[i][0:3])
    if lines[i][4:7] != '   ':
        Stacks[1].append(lines[i][4:7])
    if lines[i][8:11] != '   ':
        Stacks[2].append(lines[i][8:11])
    if lines[i][12:15] != '   ':
        Stacks[3].append(lines[i][12:15])
    if lines[i][16:19] != '   ':
        Stacks[4].append(lines[i][16:19])
    if lines[i][20:23] != '   ':
        Stacks[5].append(lines[i][20:23])
    if lines[i][24:27] != '   ':
        Stacks[6].append(lines[i][24:27])
    if lines[i][28:31] != '   ':
        Stacks[7].append(lines[i][28:31])
    if lines[i][32:35] != '   ':
        Stacks[8].append(lines[i][32:35])
    # if lines[i][36:39] != '   ':
    #     Stacks[8].append(lines[i][36:39])





for i in range(StackNosLine+1,len(lines)):
    if lines[i].strip():
        Temp_List = lines[i][:-1].split(' ')  
        for j in range(int(Temp_List[1])):
            popped_item = Stacks[int(Temp_List[3])-1].pop()
            Stacks[int(Temp_List[5])-1].append(popped_item) 

print(Stacks[0].pop(),Stacks[1].pop(),Stacks[2].pop(),Stacks[3].pop(),Stacks[4].pop(),Stacks[5].pop(),Stacks[6].pop(),Stacks[7].pop(),Stacks[8].pop())