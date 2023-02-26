f = open('day7input.txt')
lines = f.readlines()

directories_list=[]
directories_sum = {}
total_space =70000000
needed_space = 30000000
space_to_be_deleted = total_space

for line in lines:
    
    line = line[:-1].split(' ')
    
    if line[0] == '$': 
        if line[1] == 'cd':
            if line[2] == '/':
                directories_list = ['/']
            
            elif line[2] == '..':
                directories_list.pop()
            
            else:
                directories_list.append(line[2])
    
    else:
        
        if line[0] != 'dir' :
            size = int(line[0])
            
            for i in range(len(directories_list)):     
                
                if i <=1:
                    key = directories_list[i]
                else:
                    key = '/'.join(directories_list[i-1:i+1])
                
                
                if key in directories_sum:
                    directories_sum[key] += size
                else:
                    directories_sum[key] = size


for key in directories_sum.keys():
    remaining_space = total_space - directories_sum['/']
    if remaining_space+directories_sum[key] >= needed_space:
        if directories_sum[key]<space_to_be_deleted:
            space_to_be_deleted = directories_sum[key]
print(space_to_be_deleted)
    
