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

M = list(range(10))
# 前十个数, 每两个取一个：
print(M[:10:2]) # [0,2,4,6,8]
# 所有数，每5个数取一个
print(M[::5])
# 复制一个list
print(M[:])

#字符串也可以看做是一种list, 每个元素就是字符。结果仍然是字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

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