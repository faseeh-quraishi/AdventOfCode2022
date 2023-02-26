def greater_at_right(trees,index): 
    curr_tree = trees[index]
    for tree in trees[index+1:len(trees)]:
        if tree >= curr_tree:
            return 0  #tree not visible  
    return 1 #tree visible 

def greater_at_left(trees,index): 
    curr_tree = trees[index]
    for tree in trees[:index]:
        if tree >= curr_tree:
            return 0  #tree not visible  
    return 1 #tree visible 

f = open('day8input.txt')
lines = [line.strip() for line in f]
visible_trees_counter = ((len(lines)-1)*2)+((len(lines[0])-1)*2)
column_trees = []  # for making column into row temporarily

for column in range(1,len(lines[0])-1):
    column_trees = [] 
    
    for row in range(len(lines)):
        column_trees.append(lines[row][column])
    
    
    
    for row in range(1,len(lines)-1): 
        if greater_at_right(column_trees,row):
            visible_trees_counter +=1
            # break
        elif greater_at_left(column_trees,row):
            visible_trees_counter +=1
            # break
        elif greater_at_right(lines[row],column):
            visible_trees_counter +=1
        elif greater_at_left(lines[row],column):
            visible_trees_counter +=1
        
print(visible_trees_counter)