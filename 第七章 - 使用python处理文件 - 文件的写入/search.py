#文件的查找
import re

f1 = open("hello.txt","r")
count = 0
for s in f1.readlines():
    li = re.findall("good",s)
    if len(li)>0:
        count=count+li.count("good")
print("查找到"+str(count)+"个good")
f1.close()