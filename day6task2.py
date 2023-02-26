found = False
with open('day6.txt') as file:
    lines = [line.rstrip() for line in file]

    
    for z in range(len(lines[0])-14):
        a = lines[0][z]
        b = lines[0][z+1]
        c = lines[0][z+2]
        d = lines[0][z+3]
        e = lines[0][z+4]
        f = lines[0][z+5]
        g = lines[0][z+6]
        h = lines[0][z+7] 
        i = lines[0][z+8]
        j = lines[0][z+9]
        k = lines[0][z+10]
        l = lines[0][z+11]
        m = lines[0][z+12]
        n = lines[0][z+13]
        if (a != b) & (a != c) & (a != d) & (a != e) & (a != f) & (a != g) & (a != h) & (a != i) & (a != j) & (a != k) & (a != l) & (a != m) & (a != n):
            if (b != c) & (b != d) & (b != e) & (b != f) & (b != g) & (b != h) & (b != i) & (b != j) & (b != k) & (b != l) & (b != m) & (b != n):        
                if (c != d) & (c != e) & (c != f) & (c != g) & (c != h) & (c != i) & (c != j) & (c != k) & (c != l) & (c != m) & (c != n):
                    if (d != e) & (d != f) & (d != g) & (d != h) & (d != i) & (d != j) & (d != k) & (d != l) & (d != m) & (d != n):
                        if (e != f) & (e != g) & (e != h) & (e != i) & (e != j) & (e != k) & (e != l) & (e != m) & (e != n):
                            if (f != g) & (f != h) & (f != i) & (f != j) & (f != k) & (f != l) & (f != m) & (f != n):
                                if (g != h) & (g != i) & (g != j) & (g != k) & (g != l) & (g != m) & (g != n):
                                    if (h != i) & (h != j) & (h != k) & (h != l) & (h != m) & (h != n):
                                        if (i != j) & (i != k) & (i != l) & (i != m) & (i != n):
                                            if (j != k) & (j != l) & (j != m) & (j != n):
                                                if (k != l) & (k != m) & (k != n):
                                                    if (l != m) & (l != n):
                                                        if (m != n):
                                                            print(z+14)
                                                            break
        # for j in range(14):
        #     a = listOf14[0]
        #     listOf14 = listOf14.replace(listOf14[0],'',1)
        #     if a not in listOf14:
        #         print(i+15)
        #         found = True
        #         break
        #     # else:
        #     listOf14 += a
        #         # break
                
        # if found:
        #     break