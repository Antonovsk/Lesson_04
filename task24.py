def max_berries(n, a):
 
  max_sum = 0
  for i in range(n):
    current_sum = a[i] + a[(i + 1) % n] + a[(i - 1) % n]  
    if current_sum > max_sum:
      max_sum = current_sum
  return max_sum

n = int(input("Введите количество кустов: "))
a = list(map(int, input("Введите количество ягод на каждом кусте через пробел: ").split()))

max_berries_collected = max_berries(n, a)
print(f"Максимальное количество ягод, которое можно собрать за один заход: {max_berries_collected}")