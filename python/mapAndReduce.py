# map/reduce

# map函数接受连个参数， 一个是函数， 一个是Iterator, map将传入的函数依次作用到序列的每个元素， 并把结果作为新的Iterator返回。
def f(x):
  return x * x
r = map(f, [1,2,3,4,5,6,7,8,9,10])
print(list(r))

# 把这个list中的所有数字转换为字符串
print(list(map(str, [1,2,3,4,5,6,7,8,9,10,11])))