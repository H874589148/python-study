#递归遍历目录
import os
def VisitDir(path):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path,p)
        if not os.path.isfile(pathname):
            VisitDir(pathname)
        else:
            print(pathname)

if __name__=="__main__":
    path=r"F:\github_repository\python-study\第七章 - 使用python处理文件 - 文件的写入"
    VisitDir(path)