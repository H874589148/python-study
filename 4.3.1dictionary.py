dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
print(dict)
print(dict["a"])

dict["w"]="watermelon"    #添加
print("添加之后")
print(dict)
del(dict["a"])             #删除
print("删除之后")
print(dict)
dict["g"]="grapefruit"    #修改
print("修改之后")
print(dict)
print(dict.pop("b"))
print("弹出之后")
print(dict)
dict.clear()
print("清除字典中所有元素之后")
print(dict)