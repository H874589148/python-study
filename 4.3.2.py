#字典的遍历
dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
print(dict)
for k in dict:
    print ("dict[%s] =" %k,dict[k])

print (dict.items())

#输出key的列表
print (dict.keys())
#输出value的列表
print (dict.values())

print(dict.get("c","apple"))
print(dict.get("e","apple"))