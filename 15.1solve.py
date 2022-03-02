def f(x, a):
    return(120%a == 0)and((x%70 == 0)and(x%30==0))<=(x%a==0)

for a in range(1,1000):
    flag=True
    for x in range(1,1000):
        if not (f(x, a)):
               flag=False
               break
    if flag:
        print(a)
#answer -- 30
