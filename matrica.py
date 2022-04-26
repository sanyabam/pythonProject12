# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and sea


# матрица 5*5. Найти строку с максимальной суммой и вывести её номер.
import random

N = 5
M = 5
A = [[0] * M for i in range(N)]
b = []
c = 0
max_number = []
for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(10, 90)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end = ' ')
    print()
for i in range(1, len(A)):
    b.append((sum(A[i])))
    max_number = max(b)
    if sum(A[i]) > sum(A[i-1]):
        c = i
print(c)
print(b)
print(max_number)
руддщ

