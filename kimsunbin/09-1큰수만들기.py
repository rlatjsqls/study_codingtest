def solution(number, k):
    answer = ''
    for i in range(len(number)-1):
        if number[i] == '9':
            answer += number[i]
            continue
        flag = 0
        for j in range(1,k+1):
            if number[i] < number[i+j]:
                flag = 1
                k -= 1
                if k == 0:
                    answer += number[i+j:]
                    return answer
                break
				#지정된 범위에서 그수가 가장 큰 경우
        if flag == 0:
            answer += number[i]
    return answer