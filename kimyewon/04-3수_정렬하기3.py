import sys

n = int(input())

numbers = [0]*10001

for _ in range(n):
    idx = int(sys.stdin.readline())
    numbers[idx] += 1

for idx, num in enumerate(numbers):
    if num != 0:
        for _ in range(num):
            print(idx)
