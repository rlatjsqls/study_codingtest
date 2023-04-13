def func(t, times):
    result = 0
    for i in times:
        result += t // i
    return result
    
def solution(n, times):
    end = max(times) * n
    start = 0
    while start < end:
        mid = (start + end) // 2
        if func(mid,times) >= n:
            end = mid
        else:
            start = mid + 1
        print(start,end)
    return end