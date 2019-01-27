#函数的默认参数
def arithemetic(x=1,y=1,operator="+"):
    result = {
        "+":x+y,
        "-":x-y,
        "*":x*y,
        "/":x/y
    }
    return result.get(operator)

print(arithemetic(1,2))
print(arithemetic(1,2,"-"))
print(arithemetic(y=3,operator="-"))
print(arithemetic(x=4,operator="-"))
print(arithemetic(y=3,x=4,operator="-"))