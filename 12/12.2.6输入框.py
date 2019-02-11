from tkinter import *
root = Tk()
root.title("Hawkeye")

# 定义框架
f1 = Frame(root)
Label(f1, text="标准输入框：").pack(side=LEFT, padx=5, pady=10)
# 定义输入框内容
e1 = StringVar()
# 基本的输入框
Entry(f1, width=50, textvariable=e1).pack(side=LEFT)
# 设置一般输入框默认内容
e1.set('请在这里输入Hawkeye最帅')
f1.pack()

# 定义框架
f2 = Frame(root)
e2 = StringVar()
Label(f2, text='禁用输入框：').pack(side=LEFT, padx=5, pady=10)
# 禁用的输入框
Entry(f2, width=50, textvariable=e2, state=DISABLED).pack(side=LEFT)
# 设置禁用的输入框内容
e2.set('Hawkeye最帅！')
f2.pack()

root.mainloop()