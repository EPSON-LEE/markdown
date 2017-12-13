# 迭代 只要变量具有Iterable属性就都能迭代

#迭代一个dict
d = {
  'a' : 1,
  'b' : 2,
  'c' : 3
}

#默认情况下 迭代的是key
for key in d:
  print(key)

#如果要迭代values
for value in d.values():
  print(value)

# 同时迭代key和values
for k,v in d.items():
  print(k, v)

# 判断是否是一个Iterable 通过collections模块的Iterable来判断
from collections import Iterable
# 判断待检测字符串是否为Iterable对象
isinstance('abc', Iterable) #True
isinstance([1,2,3], Iterable) #True
isinstance(123, Iterable) #False

# 迭代两个变量
print('迭代两个变量')
for x,y in [(1,1), (2,4), (3,4), (5,6)]:
  print(x, y)

  def findMinAndMax(L):
    if len(L) == 0:
      return (None, None)
    if L is None:
      return (None, None)
    else:
      if(isinstance(L, Iterable)):
        max = L[0]
        min = L[0]
        for item in L:
          if item > max:
            max = item
          if item < min:
            min = item
        print(min ,max)
        return (min, max)
      else:
        print('输入的不是一个可迭代对象')
        
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


