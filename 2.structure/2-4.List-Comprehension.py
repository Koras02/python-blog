squares = [x**2 for x in range(20)] # 0부터 20까지의 제곱 리스트
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

# 중첩된 리스트 컴프리헨션
matrix = [[j for j in range(5)] for i in range(3)];
print(matrix)
# [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
