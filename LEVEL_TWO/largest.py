def largest(list):
    n=len(list)
    max=0
    for i in list:
        if i>max:
            max=i
    return max

print(largest([1,2,3,4,5]))
