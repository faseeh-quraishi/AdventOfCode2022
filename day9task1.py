f = open('day9sample.txt')
lines = f.readlines()

row_H = 0
column_H = 0
row_T = 0
column_T = 0
distance_covered_by_t = 0

for line in lines:
    line = line.split()
    direction = line[0]
    movement = int(line[1])
    
    # For Right
    if direction == 'R':
        old_row_H = row_H
        old_column_H = column_H
        if movement>1:
            
            column_H += movement
            # if H and T are at same position.
            if row_T == old_row_H and column_T == old_column_H:
                column_T += (movement - 1)
                distance_covered_by_t += movement - 1
            # if T is on left side of H.
            elif row_T == old_row_H and column_T == old_column_H-1:
                column_T += movement
                distance_covered_by_t += movement
            #  if T is on downside of H. 
            elif row_T == old_row_H-1 and column_T == old_column_H:
                column_T += movement-1
                row_T += 1
                distance_covered_by_t += movement-1
            # if T is on upside of H.
            elif row_T == old_row_H+1 and column_T == old_column_H:
                column_T += movement-1
                row_T -= 1
                distance_covered_by_t += movement-1
            # if T is on rightside of H.
            elif row_T == old_row_H and column_T == old_column_H+1:
                if movement>2:
                    column_T += movement-2
                    distance_covered_by_t += movement-2
            
            
            # if T is on upper left of H.
            elif row_T == old_row_H+1 and column_T == old_column_H-1:
                row_T -= 1
                column_T += movement
                distance_covered_by_t += movement
            # if T is on lower left of H.
            elif row_T == old_row_H-1 and column_T == old_column_H-1:
                row_T+=1
                column_T += movement
                distance_covered_by_t += movement
            # if T is on upper right of H.
            elif row_T == old_row_H+1 and column_T == old_column_H+1:
                if movement>2:
                    row_T-=1
                    column_T += movement-2
                    distance_covered_by_t += movement-2
            # if T is lower right of H.
            elif row_T == old_row_H-1 and column_T == old_column_H+1:
                if movement>2:
                    row_T+=1
                    column_T += movement-2
                    distance_covered_by_t += movement-2
        
        else:
            
            # if T is on left side of H.
            if row_T == old_row_H and column_T == old_column_H-1:
                column_T += movement
                distance_covered_by_t += movement
            # if T is on upper left of H.
            elif row_T == old_row_H+1 and column_T == old_column_H-1:
                row_T -= 1
                column_T += movement
                distance_covered_by_t += movement
             # if T is on lower left of H.
            elif row_T == old_row_H-1 and column_T == old_column_H-1:
                row_T+=1
                column_T += movement
                distance_covered_by_t += movement
            column_H += movement
    
    # For Left 
    elif direction == 'L':
        old_row_H = row_H
        old_column_H = column_H
        if movement>1:
            
            column_H -= movement
            # if H and T are at same position.
            if row_T == old_row_H and column_T == old_column_H:
                column_T -= (movement - 1)
                distance_covered_by_t += movement - 1
            # if T is on left side of H.
            elif row_T == old_row_H and column_T == old_column_H-1:
                if movement>2:
                    column_T -= movement-2
                    distance_covered_by_t += movement-2
            #  if T is on downside of H. 
            elif row_T == old_row_H-1 and column_T == old_column_H:
                column_T -= movement-1
                row_T += 1
                distance_covered_by_t += movement-1
            # if T is on upside of H.
            elif row_T == old_row_H+1 and column_T == old_column_H:
                column_T -= movement-1
                row_T -= 1
                distance_covered_by_t += movement-1
            # if T is on rightside of H.
            elif row_T == old_row_H and column_T == old_column_H+1:
                column_T += movement
                distance_covered_by_t += movement
            
            # if T is on upper left of H.
            elif row_T == old_row_H+1 and column_T == old_column_H-1:
                if movement>2:
                    row_T -= 1
                    column_T -= movement-2
                    distance_covered_by_t += movement-2
            # if T is on lower left of H.
            elif row_T == old_row_H-1 and column_T == old_column_H-1:
                if movement>2:
                    row_T += 1
                    column_T -= movement-2
                    distance_covered_by_t += movement-2
            # if T is on upper right of H.
            elif row_T == old_row_H+1 and column_T == old_column_H+1:
                
                    row_T-=1
                    column_T -= movement
                    distance_covered_by_t += movement
            # if T is lower right of H.
            elif row_T == old_row_H-1 and column_T == old_column_H+1:
                
                    row_T+=1
                    column_T -= movement
                    distance_covered_by_t += movement

        else:
            
            # if T is on rightside of H.
            if row_T == old_row_H and column_T == old_column_H+1:
                column_T += movement
                distance_covered_by_t += movement
            # if T is lower right of H.
            elif row_T == old_row_H-1 and column_T == old_column_H+1:
                
                    row_T+=1
                    column_T -= movement
                    distance_covered_by_t += movement
            # if T is on upper right of H.
            elif row_T == old_row_H+1 and column_T == old_column_H+1:
                
                    row_T-=1
                    column_T -= movement
                    distance_covered_by_t += movement
            column_H -= movement
    
    # For Up
    elif direction == 'U':
        old_row_H = row_H
        old_column_H = column_H
        if movement>1:
            
            row_H += movement
            # if H and T are at same position.
            if row_T == old_row_H and column_T == old_column_H:
                row_T += (movement - 1)
                distance_covered_by_t += movement - 1
            # if T is on left side of H.
            elif row_T == old_row_H and column_T == old_column_H-1:
                row_T += movement-1
                column_T += 1
                distance_covered_by_t += (movement-1)
            #  if T is on downside of H. 
            elif row_T == old_row_H-1 and column_T == old_column_H:
                row_T += movement
                distance_covered_by_t += movement
            # if T is on upside of H.
            elif row_T == old_row_H+1 and column_T == old_column_H:
                if movement>2:
                    row_T += movement-2
                    distance_covered_by_t += movement-2
            # if T is on rightside of H.
            elif row_T == old_row_H and column_T == old_column_H+1:
                column_T += movement-1
                row_T-=1
                distance_covered_by_t += movement-1

            # if T is on upper left of H.
            elif row_T == old_row_H+1 and column_T == old_column_H-1:
                if movement > 2:
                    row_T += movement-2
                    column_T += 1
                    distance_covered_by_t += movement-2
            # if T is on lower left of H.
            elif row_T == old_row_H-1 and column_T == old_column_H-1:
                row_T+= movement
                column_T += 1
                distance_covered_by_t += movement
            # if T is on upper right of H.
            elif row_T == old_row_H+1 and column_T == old_column_H+1:
                if movement>2:
                    row_T-= movement-2
                    column_T -= 1
                    distance_covered_by_t += movement-2
            # if T is lower right of H.
            elif row_T == old_row_H-1 and column_T == old_column_H+1:
                
                    row_T += movement
                    column_T -= 1
                    distance_covered_by_t += movement
        


        else:
            
            #  if T is on downside of H. 
            if row_T == old_row_H-1 and column_T == old_column_H:
                row_T += movement
                distance_covered_by_t += movement
            # if T is lower right of H.
            elif row_T == old_row_H-1 and column_T == old_column_H+1:
                
                    row_T += movement
                    column_T -= 1
                    distance_covered_by_t += movement
            # if T is on lower left of H.
            elif row_T == old_row_H-1 and column_T == old_column_H-1:
                row_T+= movement
                column_T += 1
                distance_covered_by_t += movement
            row_H += movement


   
    elif direction == 'D':
        old_row_H = row_H
        old_column_H = column_H
        if movement>1:
            
            row_H -= movement
            # if H and T are at same position.
            if row_T == old_row_H and column_T == old_column_H:
                row_T -= (movement - 1)
                distance_covered_by_t += movement - 1
            # if T is on left side of H.
            elif row_T == old_row_H and column_T == old_column_H-1:
                row_T -= movement-1
                column_T += 1
                distance_covered_by_t += movement-1
            #  if T is on downside of H. 
            elif row_T == old_row_H-1 and column_T == old_column_H:
                if movement>2:
                    row_T -= movement-2
                    distance_covered_by_t += movement-2
            # if T is on upside of H.
            elif row_T == old_row_H+1 and column_T == old_column_H:
                row_T += movement
                distance_covered_by_t += movement
            # if T is on rightside of H.
            elif row_T == old_row_H and column_T == old_column_H+1:
                column_T -= movement-1
                row_T-=1
                distance_covered_by_t += movement-1
           
            # if T is on upper left of H.
            elif row_T == old_row_H+1 and column_T == old_column_H-1:
                
                    row_T -= movement
                    column_T += 1
                    distance_covered_by_t += movement
            # if T is on lower left of H.
            elif row_T == old_row_H-1 and column_T == old_column_H-1:
                if movement>2:
                    row_T-= movement-2
                    column_T += 1
                    distance_covered_by_t += movement-2
            # if T is on upper right of H.
            elif row_T == old_row_H+1 and column_T == old_column_H+1:
                
                    row_T-= movement
                    column_T -= 1
                    distance_covered_by_t += movement
            # if T is lower right of H.
            elif row_T == old_row_H-1 and column_T == old_column_H+1:
                if movement>2:
                    row_T -= movement-2
                    column_T -= 1
                    distance_covered_by_t += movement-2
        
        else:
            
            
            # if T is on upside of H.
            if row_T == old_row_H+1 and column_T == old_column_H:
                row_T += movement
                distance_covered_by_t += movement
            
            # if T is on upper right of H.
            elif row_T == old_row_H+1 and column_T == old_column_H+1:
                
                    row_T-= movement
                    column_T -= 1
                    distance_covered_by_t += movement
            
             # if T is on upper left of H.
            elif row_T == old_row_H+1 and column_T == old_column_H-1:
                
                    row_T -= movement
                    column_T += 1
                    distance_covered_by_t += movement
            row_H -= movement




print(f'Tail:({row_T},{column_T})\nHead:({row_H},{column_H})\nTotal movement:{distance_covered_by_t}')