def solution(name):
    alp = {'A':1,'B': 2,'C': 3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    
    answer = 0
    n = len(name)
    temp = n - 1
    
    for i in range(n):
        next_i = i+1
        while (next_i < n) and (name[next_i] == "A"):
            next_i += 1 
        temp = min(temp, 2* i + n - next_i, i + 2 *(n - next_i))
    answer += temp
    
    #문자 변경 횟수
    for i in range(0,len(name)):
        if alp[name[i]] - 1 > 13:
            answer += 27 - alp[name[i]]
        else:
            answer += alp[name[i]] - 1
    return answer