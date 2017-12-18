# 面向对象

class Student(object):

  def __init__ (self, name, score):
    # 私有变量
    self.__name = name
    self.__score = score
  
  def set_name(self, score):
    if 0 <= score <= 100:
      self.__score = score
    else:
      raise ValueError('bad score')

  def get_name(self):
    return self.__name
  
  def get_score(self):
    return self.__score
    
  def print_score(self):
    print("%s: %s" %(self.name, self.__score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.__score = 10
print(bart.__score)

bart.print_score()
lisa.print_score()

# 继承和多态  polyphrism and inheritance

class Animal(object) {
  def run(self):
    print('Aniaml is running')
}

class Dog(Animal) {
  def run(self):
    print('Dog is running')

  def eat(self):
    print('Eating meat...')
}

