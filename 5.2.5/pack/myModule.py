def func():
    print ("pack.myModule.func()")

if __name__=='__main__':
    print('myModule作为主程序运行')
else:
    print('myModule被另外一个模块调用')