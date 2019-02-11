from tkinter import *
root = Tk()
root.title("Hawkeye")

# 定义变量
foo = IntVar()
for text,value in [('red',1),('green',2),('black',3),('blue',4),('yellow',5)]:
    r = Radiobutton(root, text=text, value=value, variable=foo)
    r.pack(anchor=W)
# 设定默认选项
foo.set(2)

if __name__ == '__main__':
    root.mainloop()
