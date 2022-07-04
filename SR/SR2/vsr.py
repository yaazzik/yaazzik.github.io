import itertools

def fibonacci(n):
  Flist = []
  for i in itertools.count(0, 1):
    if i == 0:
      Flist += [0]
    if i == 1:
      Flist += [1]
    if i > 1:
      Flist += [Flist[-1] + Flist[-2]]
    if i == n - 1:
      break
  return Flist

num = int(input("Введи количество элементов ряда Фибоначчи "))
print(fibonacci(num))
