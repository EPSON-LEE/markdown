# 列表生成式

# 比如说生成一个list[1,2,3,4,5,6,7,8,9,10] 可以用list(range(1,11))
list(range(1, 11))

# 如果要生成[1*1, 2*2, 3*3, 4*4, 5*5, 6*6 ... 10*10]
L = []
for x in range(1, 11):
  L.append(x * x)
print(L)

# 可以把要生成的元素x * x放在前面，后面跟上for循环，循环后面还可以加上条件，就可以生成list
print([x * x for x in range(1, 11) if x % 2 == 0])
#双层循环
print([m +n for m in range(1,11) for n in range(12, 20)])

#练习
L = ['Hello', 'World', 18, 'Apple', None]
# for item in L:
#   if isinstance(item, str):
#     item.lower() 
# print(L)

def toLower(l):
  if len(l) >= 0:
    result = [item.lower() for item in L if isinstance(item, str)]
  return result

print([item.lower() for item in L if isinstance(item, str)])
print(toLower(L))