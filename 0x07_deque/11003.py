# https://www.acmicpc.net/problem/11003
# 배열로 풀면 시간 초과 O(N^2)
# sliding window - deque O(N)

from collections import deque

def solution(N, L, num):

    min_num = []
    dq = deque() # i - L + 1 ~ i index 저장

    for i in range(N):
        
        if dq and dq[0] < i - L + 1: # front index 범위 확인
            dq.popleft()
        
        while dq and num[dq[-1]] > num[i]: # deque내 앞 쪽 value (num의 index)에 해당하는 argumentValue가 더 작은지 계속 확인
            dq.pop()

        dq.append(i)
        min_num.append(num[dq[0]])


    ans = " ".join(map(str, min_num))
    return ans

# input
N, L = map(int, input().split())
num = list(map(int, input().split()))

# solution
ans = solution(N, L, num)
print(ans)