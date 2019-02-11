from tkinter import *
root = Tk()
root.title("Hawkeye")
# 设定按钮的值
l = [('red', 1, NORMAL), ('green', 2, NORMAL), ('black', 3, DISABLED), ('blue', 4, NORMAL), ('yellow', 5, DISABLED)]
for text, value, status in l:
    foo = IntVar()
    c = Checkbutton(root, text=text, variable=foo, state=status)
    c.pack(anchor = W)
root.mainloop()