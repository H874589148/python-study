from tkinter import *
root = Tk()
root.title("Hawkeye")
# 设定一个列表组件
l = Listbox(root, height=6, width=15)
# 定义滚动条，并绑定一个回调
scroll = Scrollbar(root, command=l.yview)
l.configure(yscrollcommand=scroll.set)
l.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
#for item in ['apple', 'orange', 'peach', 'banana', 'melon']:
for item in range(20):
    l.insert(END, item)
root.mainloop()