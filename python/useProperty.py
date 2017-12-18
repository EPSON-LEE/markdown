class Student(object):
  def get_score(self):
    return self._score
  
  def set_score(self, value):
    if not isinstance(value, int)
      raise ValueError('score must be an interger!')
    if value < 0 or value > 100:
      raise ValueError('score must between 0~100!')
    self._score = value

  
# 既能检查参数又可以使用类似属性来访问类的变量 decorator