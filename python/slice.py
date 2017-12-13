# 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#取前三个元素 L[startIndex, endIndex] 左闭右开
#方法一：
print([L[0], L[1], L[2]])
#方法二：
print(L[0:3])
#方法三：
print(L[:3])

# range(100)函数 使用list配合range(100)函数生成0-99的数列
K = list(range(100))
print(K)

#尾递归实现trim函数， 去掉头尾两边的空格
def trim(s):
    if s == '':
        return s
    elif s[0] == ' ':
      return trim(s[1:])
    elif s[-1] == ' ':
      return trim(s[0:-1])
    else:
      return s
print('          hello           ')
print(trim('      hello           '))