# 函数参数

## 计算开方数
def power(x,n=2):
  s = 1
  while n > 0:
    s = s * x
    n = n - 1
  print(s)
  return s  

power(5) #25
power(5,3) #125

def add_end(l=[]):
  l.append('END')
  print(l)
  return l

# 接连调用两次，不给传入参数
add_end() # ['EMD']
add_end() # ['END', 'END']
# 改进方案
def add_end_with_judge(l=[]):
  if l is None:
    l = []
  l.append('END')
  print(l)
  return l
# 函数调用
add_end_with_judge() # ['END']
add_end_with_judge() # ['END', 'END']

### 原因：
### 定义默认参数必须要牢记一点: 默认参数必须指向不变对象， 函数在定义的时候， 默认参数的值就被计算出来了

# 可变参数 传入的参数的个数是可变的， 可以是1个2个或者任意个
print('------普通函数模拟可变参数--------------')
def calc_unChangeAble(number):
  sum = 0
  for n in number:
    sum = sum + n
  print(sum)
  return sum

calc_unChangeAble([1, 2, 3]) #6
calc_unChangeAble([6,7,8,9,10,11,12,13,14,15,16,17]) #138

# 使用普通参数的定义形式，如果需要传入多种参数需要把参数变换为list或者tuple
# 可变参数应运而生
print('--------------使用可变参数--------------')
def calc(*number):
  sum = 0
  for item in number:
    sum = sum + item
  print(sum)
  return sum

calc(1,2,3) #6
calc(6,7,8,9,10,11,12,13,14,15,16,17) #138
# 分析：定义可变参数仅仅在参数前加了一个*号， 函数内部却接受到的是一个tuple


# 关键字参数 关键字参数允许你传入0个或任意个参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 对于关键字参数， 函数可以传入任意不受限制的关键字参数。 至于传入多少参数，需要在函数内部进行检查

# 关键字参数
def person(name, age, **kw):
  #对关键字进行检查
  if 'city' in kw:
    print(kw)
  if 'name' in kw:
    print(kw)
  if 'address' in kw:
    print(kw)
  print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30, city='BeiJing', zipcode=710025, sex="1") # name:Michael age:30 other:(city:'BeiJing', zipcode:"710025", sex:"1")

# 命名关键字参数
# 只接受*后面的city和job作为关键字参数
def targetPerson(name, age, *, city= "XI'AN", job):
  print('name:', name, 'age:', age, 'other:', 'city:', city, 'job:',job)
# 正常调用
targetPerson('Jack', 24, city='BeiJing', job='Engineer') # name: Jack age:30 other: { 'city': 'BeiJing', 'job': 'Engineer' }
# 参数缺省值使用
targetPerson('Jack', 18, job='student') # name: Jack  age: 30 

# 参数组合
def f1(a, b, c = 0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'args =', args, 'kw =', kw)
def f2(a, b, *, d, **kw):
    print('a =', a, 'b = ', b, 'c = ', c, 'd =', d, 'kw =', kw)

f1(1,2) # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c = 3) # a =1 b = 2 args = () kw = {}
f1(1,2,3,'a','b') # a = 1 b = 2 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99) # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)  # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。