'''

[(1, 3), (2, 1), (3, 4), (4, 3), (5, 2)] => 누적 합의 시간이 걸리게 된다.

[2, 5, 1, 4, 3] 으로 서게 되면
(2, 1), (5, 2), (1, 3), (4, 3), (3, 4) 순이면 39분

걸리는 시간의 합이 최소가 되기 위해서는 최소 sort
[1, 2, 3, 3, 4]
-> 1 + (1+2) + (1+2+3) + (1+2+3+3) + (1+2+3+3+4)
'''

n = int(input())
priod = list(map(int, input().split()))

priod.sort()
sum_ = 0
for idx in range(len(priod)):

    sum_ += sum(priod[:idx+1])
print(sum_)
