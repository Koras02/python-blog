

''' for i in range(5):
     print(i) '''
# 0
# 1
# 2
# 3
# 4

a = list(range(5,10))
print(a)
# [5,6,7,8,9]

b = list(range(0, 10, 3))
print(b)
# [0, 3, 6, 9]

c = list(range(-5, -60, -20))
print(c)
# [-5, -25, -45]

d = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(d)):
    print(i, d[i])
'''
0 Mary
1 had
2 a
3 little
4 lamb
'''

print(range(10))
# range(0,10)

print(sum(range(4))) # 0 + 1 + 2 + 3 = 6
print(sum(range(5))) # 1 + 2 + 3 + 4 = 10
print(sum(range(6))) # 1 + 2 + 3 + 4 + 5 = 15
print(sum(range(7))) # 1 + 2 + 3 + 4 + 5 + 6 = 21


for n in range(2, 10):
    for x in range(2, n):
          if n % x == 0:
              print(f"{n} equals {x} * {n//x}")
'''
4 equals 2 * 2
6 equals 2 * 3
6 equals 3 * 2
8 equals 2 * 4
8 equals 4 * 2
9 equals 3 * 3
'''

for num in range(2, 10):
      if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
        print(f"Found an odd number {num}")


