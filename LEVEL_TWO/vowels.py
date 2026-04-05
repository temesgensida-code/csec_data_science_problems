def vowels(s):
    vowels="AEIOU"
    ss=s.upper()
    counter=0
    for i in ss:
        if i in vowels:
            counter+=1
    return counter

print(vowels("werAty"))