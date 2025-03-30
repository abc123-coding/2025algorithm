# https://www.acmicpc.net/problem/17298
# 오큰수 문제
def solution(N, A):

    stack = [] # 오큰수를 찾지 못한 인덱스를 저장
    NGE = [-1] * N

    for i in range(N):

        while stack and A[stack[-1]] < A[i]:
            NGE[stack.pop()] = A[i]

        stack.append(i)

    return ' '.join(map(str, NGE))

# input
N = int(input())
A = list(map(int, input().split()))

# solution
print(solution(N, A))