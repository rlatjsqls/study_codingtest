from heapq import heappop, heapify, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a + b*2)
        answer += 1
    return answer