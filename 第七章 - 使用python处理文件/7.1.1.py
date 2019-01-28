#创建文件
context = '''hello world'''

f = open('hello.txt','w')
f.write(context)
f.close()