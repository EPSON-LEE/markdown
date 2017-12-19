file = open('./a.txt')
print(file.read())
# 文件使用完成必须关闭， 否则会占用系统资源
file.close()
