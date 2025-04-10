# https://www.acmicpc.net/problem/15663

def solution(arr, visited):

    if len(arr) == M:
        result.add(tuple(arr))
        return

    for i in range(N):
        if i in visited:
            continue

        visited.add(i)
        solution(arr + [num[i]], visited)
        visited.remove(i)

# input
N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))

# solution
result = set()
solution([], set())
result = sorted(result)
print("\n".join(" ".join(map(str, ans)) for ans in result))