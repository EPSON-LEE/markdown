## 使用slots

class Student(object):
  pass

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)

#给实例绑定一个方法：
def set_age(self ,age):
  self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

# 给一个实例绑定的方法 对另一个实例不起作用
s2 = Student()
# s2.set_age(25)

# 使用slots
class Student2(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

stu = Student2()
stu.name = 'Michael'
stu.age = 25
stu.score = 99

