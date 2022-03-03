from itertools import product
p=product('ИГОРЬ', repeat=8)
k=0
for x in p:
    s=''.join(x)
    if (s[0]!='Ь') and (s.count('О')==1) and (s.count('Ь')==1):
        k+=1
print(k)
#answer -- 35721
