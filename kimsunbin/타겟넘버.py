def solution(numbers, target):
    answer = 0
    arr = [0]
    for i in numbers:
        tmp = []    
        for j in arr:   
            tmp.append(j + i)   
            tmp.append(j - i)   
        arr = tmp
    return arr.count(target)