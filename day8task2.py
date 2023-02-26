def score_at_right(trees,index): 
    curr_tree = trees[index]
    tree_count = 0
    for tree in trees[index+1:len(trees)]:
        tree_count += 1 
        if tree >= curr_tree:
              break
    return tree_count 



def score_at_left(trees,index): 
    curr_tree = trees[index]
    tree_count = 0
    for tree in trees[index-1::-1]:
        tree_count += 1 
        if tree >= curr_tree:
            break  #tree not visible  
    return tree_count #tree visible 

f = open('day8input.txt')
lines = [line.strip() for line in f]
# visible_trees_counter = ((len(lines)-1)*2)+((len(lines[0])-1)*2)
score = 0
column_trees = []  # for making column into row temporarily
# print(score_at_left([3,5,3,5,3],3))

for column in range(1,len(lines[0])-1):
    column_trees = [] 
    
    for row in range(len(lines)):
        column_trees.append(lines[row][column])
    
    
    
    for row in range(1,len(lines)-1): 
        a = score_at_right(column_trees,row)
        b = score_at_left(column_trees,row)
        c = score_at_right(lines[row],column)
        d = score_at_left(lines[row],column)
        curr_score = a*b*c*d
        if curr_score >= score:
            score = curr_score

        
print(score)