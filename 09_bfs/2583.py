# https://www.acmicpc.net/problem/2583
# 전형적인 BFS 문제

from collections import deque

def solution(M, N, board):

    areas = []
    queue = deque()
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(M):
        for j in range(N):
            if board[i][j]: # block or already visited
                continue

            queue.append((i, j)) # bfs start point
            board[i][j] = 1 # visit start point
            area = 1

            while queue: # bfs
                y, x = queue.popleft()

                for dx, dy in dir:
                    ny, nx = y + dy, x + dx

                    if 0 <= nx < N and 0 <= ny < M and board[ny][nx] == 0:
                        queue.append((ny, nx))
                        board[ny][nx] = 1  # visit next point
                        area += 1

            areas.append(area)

    areas.sort()
    return areas


# input
M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

# solution
areas = solution(M, N, board)
print(len(areas))
print(' '.join(map(str, areas)))
