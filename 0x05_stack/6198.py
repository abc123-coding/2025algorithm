# https://www.acmicpc.net/problem/6198
# 배열로 풀면 시간 초과

def solution(heights):

    cnt = 0
    stack = [] # 스택에 지금까지 탐색 한 중 높은 빌딩만 넣자

    for h in heights:
        while stack and stack[-1] <= h: # 더 높은 빌딩 발견
            stack.pop()

        cnt += len(stack)
        stack.append(h)

    return cnt

# input
N = int(input())
heights = [int(input()) for _ in range(N)] # Pythonic expression

# solution
cnt = solution(heights)
print(cnt)




