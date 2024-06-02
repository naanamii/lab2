n = 2 ** int(input("Enter the number of iterations: ")) 
assert n >= 2 
pascaltr = [[1]] 
previous = [1] 
for i in range(2, n+1): 
    current = [1] 
    for j in range(1, i-1): 
        current.append(previous[j-1] + previous[j]) 
    current.append(1) 
    previous = current 
    pascaltr.append(current) 
 
maxlen = len(pascaltr[-1]) * 2 
for i in range(n): 
    a = "" 
    for j in range(i+1): 
        a +="* " if pascaltr[i][j]%2 == 1 else "  " 
    print(" " * ((maxlen - len(a) + 1) // 2) + a)