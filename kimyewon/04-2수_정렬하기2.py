import sys


n = int(input())

numbers = [int(sys.stdin.readline()) for _ in range(n)]

numbers.sort() # 시간복잡도 O(nlogn)

for i in numbers:
    print(i)
