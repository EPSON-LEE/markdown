# class Student(object):
#   def get_score(self):
#     return self._score
  
#   def set_score(self, value):
#     if not isinstance(value, int)
#       raise ValueError('score must be an interger!')
#     if value < 0 or value > 100:
#       raise ValueError('score must between 0~100!')
#     self._score = value

  
# 既能检查参数又可以使用类似属性来访问类的变量 decorator

class Student(object):

  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 ~ 100')
    self._score = value

# 使用
s = Student()
s.score = 60 #OK 转化成s.set_score
s.score  # OK 转化成s.get_score

class Screen(object):

  @property
  def width(self):
    return self._width

  @width.setter
  def width(self, value):
    self._width = value

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, value):
    self._height = value

  @property
  def resolution(self):
    return self._height*self._width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')