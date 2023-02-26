f = open('day1.txt','r')
max_sum = 0
curr_sum = 0
lines = f.readlines()
FirstHigh= 0
SecondHigh= 0
ThirdHigh= 0
for line in lines:
    # count +=1
    if line.strip():
        curr_sum = curr_sum + int(line)  
    else:
        if curr_sum >FirstHigh :
            ThirdHigh = SecondHigh
            SecondHigh = FirstHigh
            FirstHigh = curr_sum
        elif FirstHigh >= curr_sum>= SecondHigh:
            ThirdHigh = SecondHigh
            SecondHigh = curr_sum
        elif SecondHigh>= curr_sum >= ThirdHigh:
            ThirdHigh = curr_sum
        curr_sum = 0
max_sum = FirstHigh+SecondHigh+ThirdHigh 
print(max_sum,FirstHigh,SecondHigh,ThirdHigh)
f.close()