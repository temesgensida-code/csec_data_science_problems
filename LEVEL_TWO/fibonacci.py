def fibonacci(n):
    k=[]
    i1=0
    i2=1
    for i in range(n):
        if i == 0 or i == 1:
            k.append(i)
        else:
            k.append(k[i1] + k[i2])
            i1+=1
            i2+=1
    return k

print(fibonacci(7))