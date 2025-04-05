# https://www.acmicpc.net/problem/15657

def solution(start_idx, result):

    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(start_idx, N):
        result.append(num[i])
        solution(i, result)
        result.pop()

# input
N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

# solution
solution(0,  [])