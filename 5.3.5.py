#计算阶乘
def refunc(n):
    i=1
    if n>1:
        i=n
        n=n*refunc(n-1)
    print ("%d!="%i,n)
    return n

refunc(5)