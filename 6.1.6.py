#循环输出反转的字符串
def reverse(s):
    out = ""
    li = list(s)
    for i in range (len(li),0,-1):
        out+="".join(li[i-1])
    return out

print (reverse("hello"))