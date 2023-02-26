f = open('day5.txt')
lines = f.readlines()
StackNosLine = 3
Stacks = [[],[],[]]
Temp_List = []

for i in range(StackNosLine-1,-1,-1):
    if lines[i][0:3] != '   ':
        Stacks[0].append(lines[i][0:3])
    if lines[i][4:7] != '   ':
        Stacks[1].append(lines[i][4:7])
    if lines[i][8:11] != '   ':
        Stacks[2].append(lines[i][8:11])



for i in range(StackNosLine+1,len(lines)):
    if lines[i].strip():
        Temp_List = lines[i][:-1].split(' ')
        # for j in range(int(Temp_List[1])):    #For Task1: comment 21,22
        start = len(Stacks[int(Temp_List[3])-1])  - int(Temp_List[1])
        for j in range(start , len(Stacks[int(Temp_List[3])-1]) , 1):
            popped_item = Stacks[int(Temp_List[3])-1].pop(start)
            Stacks[int(Temp_List[5])-1].append(popped_item) 

print(Stacks[0].pop(),Stacks[1].pop(),Stacks[2].pop())