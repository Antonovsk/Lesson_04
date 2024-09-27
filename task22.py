n = int(input("Введите количество элементов множества n: "))

number1 = []

for i in range(n):
  c = int(input(f"Введите элементы множества n: "))
  number1.append(c)
  
m = int(input("Введите количество элементов множества m: "))

number2 = []

for i in range(m):
  c = int(input(f"Введите элементы множества m: "))
  number2.append(c)

set1 = set(number1)
set2 = set(number2)

union_set = set1 | set2  

union_list = list(union_set)

print(f"Объединенное множество: {union_list}")