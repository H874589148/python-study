from tkinter import *
root = Tk()
root.title("Hawkeye")
# 使用state参数来设定按钮的状态
Button(root, text="禁用", state=DISABLED).pack(side=LEFT)
Button(root, text="取消",).pack(side=LEFT)
Button(root, text="文件",).pack(side=LEFT)
Button(root, text="工具",).pack(side=LEFT)
Button(root, text="窗口",).pack(side=LEFT)
Button(root, text="帮助",).pack(side=LEFT)
Button(root, text="确定",).pack(side=LEFT)
# 绑定了退出的回调
Button(root, text="退出", command=root.quit).pack(side=RIGHT)
root.mainloop()