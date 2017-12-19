# 一个简单的装饰器 面向切面的编程
def log(func):

  def wrapper():
    print("%s is running" % func.__name__)
    return func()
  return wrapper

def foo():
  print('i am a foo')

foo = log(foo)
foo()

# 语法糖

def slice1():

  def slice2(*argv, *kwargs):
    print('It's in slice 2')
