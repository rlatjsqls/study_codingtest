def solution(op):
    answer = []
    for i in op:
        #빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.
        if len(answer) == 0 and i[0] == 'D':
            continue
            
        #빈 큐에 데이터 입력하는 경우 / int(i[2:]) - 숫자부분
        elif len(answer) == 0 and i[0] == 'I':
            max_q = int(i[2:])
            min_q = int(i[2:])
            answer.append(int(i[2:]))
        
        # 비어있지 않은 큐에 데이터를 입력하는 경우
        elif i[0] == 'I':
            if int(i[2:]) > max_q:
                max_q = int(i[2:])
            if int(i[2:]) < min_q:
                min_q = int(i[2:])
            answer.append(int(i[2:]))
            
        # 큐에서 최댓값을 삭제하는 경우
        elif i[0] == 'D' and int(i[2:]) == 1:
            answer.remove(max_q)
            if len(answer):
                max_q = max(answer)
                
        # 큐에서 최솟값을 삭제하는 경우
        elif i[0] == 'D' and int(i[2:]) == -1:
            answer.remove(min_q)
            if len(answer):
                min_q = min(answer)
    
    # 모든 연산후 큐가 비어있는 경우
    if len(answer) == 0:
        return [0,0]
    
    return [max_q,min_q]