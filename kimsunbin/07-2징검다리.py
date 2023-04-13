def solution(distance, rocks, n):
    rocks.sort()
    start = 0
    end = distance
    cnt = 0
    result = 0
    
    # 모든 돌을 치우는 경우
    if len(rocks) - n == 0:
        return distance
    
    while start<end:
        cnt = 0     #지정 거리가 넘어가면 세우는 돌의 개수
        mid = (start + end) // 2
        x = 0       #거리
        flag = 0    #마지막돌부터 도착 지점까지의 거리를 확인후 거기도 통과가 되면 result값을 비교
        
        #출발지점부터 첫돌까지 거리
        x += rocks[0]
        if x >= mid:
            cnt += 1
            x = 0
        
        #돌들 사이의 거리
        for i in range(0,len(rocks)-1):
            x += rocks[i+1] - rocks[i]
            if x >= mid:
                cnt += 1
                x = 0
        
        #마지막 돌부터 도착지점까지의 거리
        x += distance - rocks[-1]
        if x < mid:
            flag = 1
        
        # 세운돌이 더 적을 경우에 지금 길이가 이전 최대값보다 크면 최대값변경
        if cnt == len(rocks) - n and flag == 0:
            if result < mid:
                result = mid
        
        #세운 돌이 더 적은 경우 지정 길이를 줄임
        if cnt < len(rocks) - n:
            end = mid
        
        #세운 돌이 더 많으면 지정 길이를 늘림
        elif cnt >= len(rocks) - n:
            start = mid+1
    return result