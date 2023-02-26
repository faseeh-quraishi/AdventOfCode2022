def Find_Common(Rucksacks_List):
    for item in Rucksacks_List[0]:
        if item in Rucksacks_List[1] :
            if item in Rucksacks_List[2]:
                print(Rucksacks_List[1],Rucksacks_List[2])
                return item

f = open('day3.txt')
lines = f.readlines()
Temp_List = []
Total = 0
Line_count = 0
for i in range(int(len(lines)/3)):
    for LineNo in range(3):
        Temp_List.append(lines[Line_count][:-1])
        Line_count+=1
    common = Find_Common(Temp_List)
    if (123>ord(common)>96):
        Total += (ord(common)-96)
    elif (91>ord(common)>64):
        Total += (ord(common)-(64)+26)
    Temp_List = []
print(Total)
f.close()
# print(Find_Common([lines[297][:-1],lines[298][:-1],lines[299][:-1]]))