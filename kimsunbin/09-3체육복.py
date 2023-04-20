def solution(n, lost, arr):
    reserve = []
    for i in arr:
        if i in lost:
            lost.remove(i)
        else:
            reserve.append(i)
    reserve.sort()
    lost.sort()
    while reserve:
        x = reserve.pop(0)
        if x - 1 in lost:
            lost.remove(x - 1)
        elif x + 1 in lost:
            lost.remove(x + 1)
    return n -len(lost)