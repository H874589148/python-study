#特殊切片截取子串
str1="hello world"
print(str1[0:3])
print(str1[::2])
print(str1[1::2])

#使用split()获取子串
sentence="Bob said: 1, 2, 3, 4"
print("使用空格取子串：",sentence.split())
print("使用逗号取子串：",sentence.split(","))
print("使用两个逗号取子串：",sentence.split(",",2))