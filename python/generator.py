# 生成器

# 你可以通过列表生成式生成一个元素数量达到百万个的list，但是如果你只使用到了前面的几个元素而没有用到已经生成的数百万个元素那么就会造成存储空间的大大浪费。
# 所以如果元素可以按照某种算法推算出来，那么我们可以一边循环一边生成list元素，这种循环机制就叫做生成器：generator。

# 创建generator的方法：
L = [x * x for x in range(10)]
print(L) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 第一种方式：
g = (x * x for x in range(10))
print(g) # <generator object <genexpr> at 0x00558F60>
print(next(g)) #0
print(next(g)) #1
# 如果没有元素的时候会抛出StopIteration的错误

# 正确使用generator的姿势
# 在创建了一个generator之后，基本永远不会调用next()， 而是通过for循环来迭代他
g = ( x + 1 for x in range(1,100))
for n in g:
  print(n)

# 生成斐波那契数列
def fib(max):
  n, a, b = 0, 1, 1
  while n < max:
    print(b)
    a, b = b, a+b
    n = n + 1
  return 'done'

#输出斐波那契数列前6个元素
fib(6)

# 创建generator的第二种方法
#使用generator生成斐波那契
def fib_generator(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n = n + 1
  return 'done' 
f = fib_generator(10)
print(next(f))
print(next(f))
print(next(f))

#作业： 杨辉三角
def triangles(max):
  L = [1]
  N = 0
  while N < max:
    yield L
    L = [L[i] + L[i + 1] for i in range(len(L)-1)]
    L.insert(0,1)
    L.append(1)
    n = n + 1