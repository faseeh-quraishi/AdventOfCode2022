f = open('day4.txt')
lines = f.readlines()
# sections = []
counter = 0
top_left = 0
top_right = 0
bottom_left = 0
bottom_right = 0
for line in lines:
    sections = line[:-1].split(',')
    for i in range(len(sections)):
        sections[i] = sections[i].split('-')
    top_left = int(sections[0][0])
    top_right = int(sections[0][1])
    bottom_left = int(sections[1][0])
    bottom_right = int(sections[1][1])
    if (top_left <= bottom_left) and (top_right >= bottom_left):
        counter +=1
    elif (bottom_right >= top_left) and (bottom_left <= top_left):
        counter +=1
    elif (top_left >= bottom_left) and (top_right <= bottom_right ):
        counter +=1
    elif (bottom_left >= top_left) and (bottom_right <= top_right ):
        counter +=1
    
print(counter)





#   for i in range(int(sections[0][0]),int(sections[0][1])+1):
    #     temp_list1.append(i)
       
    # for i in range(int(sections[1][0]),int(sections[1][1])+1):
    #     temp_list1.append(i)

    # for number in temp_list1:
    #     if number in temp_list2:
    #         counter +=1