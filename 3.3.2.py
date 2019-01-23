x = float(input("输入x的值："))
i = 0
while(x !=0):
    if(x > 0):
        x -=1
    else:
        x +=1
    i=i+1
    print( "第%d次循环：" %(i, x))
else:
    print( "x等于0:",x)