# 多重继承

class Animal(object):
  pass

# 大类
class Mammal(Animal):
  pass

class Bird(Animal):
  pass

# 各种动物
class Dog(Mammal):
  pass

class Bat(Mammal):
  pass

class Parrot(Bird):
  pass

class Ostrich(Bird):
  pass

# 定制类

class Student(object):
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return 'Student object (name: %s)' % self.name

print(Student('Michael'))
