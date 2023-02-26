f = open('day9input.txt')
lines = f.readlines()

Head = [0,0]
Tail = [0,0]
# Old_Head = Head
total_distance = 0

for line in lines:
    line = line[:-1].split(' ')
    direction = line[0]
    movement = int(line[1])

    if direction == 'R':
        # if movement > 1:
            for i  in range(movement):
                # Head[0] += 1
                # If T is on left of H.
                if Tail[0] == Head[0]-1 and Tail[1] == Head[1]:
                    Head[0] += 1
                    Tail[0] += 1
                    total_distance +=1
                # If T is on right of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]:
                    Head[0] +=1
                # If T is is below H.
                elif Tail[0] == Head[0] and Tail[1] == Head[1]-1:
                    Head[0]+=1
                # If T is above H.
                elif Tail[0] == Head[0] and Tail[1] == Head[1]+1:
                    Head[0]+=1
                # If T is on upper left diagonal of H.
                elif Tail[0] == Head[0]-1 and Tail[1] == Head[1]+1:
                    Head[0]+=1
                    Tail[0]+=1
                    Tail[1]-=1
                    total_distance +=1
                # If T is on upper right diagonal of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]+1:
                    Head[0]+=1
                # If T is on lowerleft diagonal of H.
                elif Tail[0] == Head[0]-1 and Tail[1] == Head[1]-1:
                    Head[0]+=1
                    Tail[0]+=1
                    Tail[1]+=1
                    total_distance +=1
                # If T is on lowerright diagonal of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]-1:
                    Head[0] += 1
                # If H and T at same position
                elif  Tail[0] == Head[0] and Tail[1] == Head[1]:
                    Head[0] +=1 
    elif direction == 'L':
        # if movement > 1:
            for i  in range(movement):
                # Head[0] += 1
                # If T is on left of H.
                if Tail[0] == Head[0]-1 and Tail[1] == Head[1]:
                    Head[0] -= 1
                # If T is on right of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]:
                    Head[0] -=1
                    Tail[0] -=1
                    total_distance+=1
                # If T is is below H.
                elif Tail[0] == Head[0] and Tail[1] == Head[1]-1:
                    Head[0]-=1
                # If T is above H.
                elif Tail[0] == Head[0] and Tail[1] == Head[1]+1:
                    Head[0]-=1
                # If T is on upper left diagonal of H.
                elif Tail[0] == Head[0]-1 and Tail[1] == Head[1]+1:
                    Head[0]-=1
                # If T is on upper right diagonal of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]+1:
                    Head[0]-=1
                    Tail[0]-=1
                    Tail[1]-=1
                    total_distance+=1
                # If T is on lowerleft diagonal of H.
                elif Tail[0] == Head[0]-1 and Tail[1] == Head[1]-1:
                    Head[0]-=1
                # If T is on lowerright diagonal of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]-1:
                    Head[0] -= 1
                    Tail[0] -= 1
                    Tail[1] += 1
                    total_distance += 1
                # If H and T at same position
                elif  Tail[0] == Head[0] and Tail[1] == Head[1]:
                    Head[0] -=1 
    elif direction == 'U':
        # if movement > 1:
            for i  in range(movement):
                # Head[0] += 1
                # If T is on left of H.
                if Tail[0] == Head[0]-1 and Tail[1] == Head[1]:
                    Head[1] += 1
                # If T is on right of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]:
                    Head[1] +=1
                # If T is is below H.
                elif Tail[0] == Head[0] and Tail[1] == Head[1]-1:
                    Head[1]+=1
                    Tail[1]+=1
                    total_distance +=1
                # If T is above H.
                elif Tail[0] == Head[0] and Tail[1] == Head[1]+1:
                    Head[1]+=1
                # If T is on upper left diagonal of H.
                elif Tail[0] == Head[0]-1 and Tail[1] == Head[1]+1:
                    Head[1]+=1
                # If T is on upper right diagonal of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]+1:
                    Head[1]+=1
                # If T is on lowerleft diagonal of H.
                elif Tail[0] == Head[0]-1 and Tail[1] == Head[1]-1:
                    Head[1]+=1
                    Tail[1]+=1
                    Tail[0]+=1
                    total_distance+=1
                # If T is on lowerright diagonal of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]-1:
                    Head[1] += 1
                    Tail[0] -= 1
                    Tail[1] += 1
                    total_distance += 1
                # If H and T at same position
                elif  Tail[0] == Head[0] and Tail[1] == Head[1]:
                    Head[1] +=1
    elif direction == 'D':
        # if movement > 1:
            for i  in range(movement):
                # Head[0] += 1
                # If T is on left of H.
                if Tail[0] == Head[0]-1 and Tail[1] == Head[1]:
                    Head[1] -= 1
                # If T is on right of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]:
                    Head[1] -=1
                # If T is is below H.
                elif Tail[0] == Head[0] and Tail[1] == Head[1]-1:
                    Head[1]-=1
                # If T is above H.
                elif Tail[0] == Head[0] and Tail[1] == Head[1]+1:
                    Head[1]-=1
                    Tail[1]-=1
                    total_distance+=1
                # If T is on upper left diagonal of H.
                elif Tail[0] == Head[0]-1 and Tail[1] == Head[1]+1:
                    Head[1]-=1
                    Tail[0]+=1
                    Tail[1]-=1
                    total_distance+=1
                # If T is on upper right diagonal of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]+1:
                    Head[1]-=1
                    Tail[0]-=1
                    Tail[1]-=1
                    total_distance+=1
                # If T is on lowerleft diagonal of H.
                elif Tail[0] == Head[0]-1 and Tail[1] == Head[1]-1:
                    Head[1]-=1
                # If T is on lowerright diagonal of H.
                elif Tail[0] == Head[0]+1 and Tail[1] == Head[1]-1:
                    Head[1] -= 1
                # If H and T at same position
                elif  Tail[0] == Head[0] and Tail[1] == Head[1]:
                    Head[1] -=1 
    
    

    
    
    
            # Old_Head = Head
print(f'{total_distance}-->Head:{Head}--->Tail:{Tail}')