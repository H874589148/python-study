#追加新的内容到文件
f = open("hello.txt","a+")
new_context = "goodbye\n"
f.write(new_context)
f.close()

#writelines 效率会更高