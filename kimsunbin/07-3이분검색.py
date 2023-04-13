N, M = (map(int, input().split()))
arr = list(map(int, input().split()))

def solution(arr,M):
    arr.sort()
    start = 0
    end = N
    mid = (start + end) // 2
    while arr[mid] != M:
        if arr[mid] < M:
            start = mid
        else:
            end = mid
        mid = (start + end) // 2
    return mid + 1

print(solution(arr, M))