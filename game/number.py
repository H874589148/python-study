import random

number = random.randint(0, 9)
inp_number = input("请输入你猜的数字（0-9）：")
if inp_number == number:
    print ("恭喜猜对了")
else :
    print ("抱歉猜错了，正确答案是%d"%number)