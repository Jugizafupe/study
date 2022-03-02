def f(x, a1, a2):
    return(not(a1<=x<=a2)and((20<=x<=30)or(35<=x<=60)))
s=[]
for a1 in range(-100,100):
    for a2 in range(-100,100):
        flag=True
        for x in range(-100,100):
            if f(x, a1, a2):
                flag=False
                break
        if flag:
            s.append(a2-a1)
print(min(s))
#answer -- 40
