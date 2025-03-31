# https://www.acmicpc.net/problem/1992
# Quadtree

def solution(N, y, x):
    val = board[y][x]

    for i in range(y, y+N):
        for j in range(x, x+N):
            if board[i][j] != val:
                n = N//2
                s1 = solution(n, y, x)
                s2 = solution(n, y, x + n)
                s3 = solution(n, y + n, x)
                s4 = solution(n, y + n, x + n)
                return f"({s1 + s2 + s3 + s4})"

    return str(val)

# input
N = int(input())
board = [[int(x) for x in input()] for _ in range(N)]

# solution
print(solution(N, 0, 0))
