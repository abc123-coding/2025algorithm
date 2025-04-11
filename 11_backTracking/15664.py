# https://www.acmicpc.net/problem/15664

def solution(idx, ans):

    if len(ans) == M:
        result.add(tuple(ans))

    for i in range(idx, N):
        ans.append(num[i])
        solution(i+1, ans)
        ans.pop()

# input
N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))

# solution
result = set()
solution(0, [])
result = sorted(result)
print("\n".join(" ".join(map(str, ans)) for ans in result))