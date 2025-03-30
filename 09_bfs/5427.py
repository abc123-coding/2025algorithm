# https://www.acmicpc.net/problem/5427
# bfs로 불 확산, 상근이 이동 구현
from collections import deque

def solution(w, h, board):
    def pos(w, h, board):
        for i in range(h):
            for j in range(w):
                if board[i][j] == '@':
                    return (i, j)  # (y, x), (h, w), (row, col)

    def pos_fire(w, h, board):
        fire = []
        for i in range(h):
            for j in range(w):
                if board[i][j] == '*':
                    fire.append((i, j))  # (y, x), (h, w), (row, col)
        return fire

    def bfs(w, h, board, queue, visited, queue_fire):

        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        time = [[-1 for _ in range(w)] for _ in range(h)]
        time[queue[0][0]][queue[0][1]] = 0  # 초기 상근이 위치 표시

        while queue:
            # 불 먼저 확산
            for _ in range(len(queue_fire)):
                row_f, col_f = queue_fire.popleft()

                for dr, dc in dir:
                    row, col = row_f + dr, col_f + dc

                    if 0 <= col < w and 0 <= row < h and board[row][col] == '.':
                        queue_fire.append((row, col))
                        board[row][col] = '*'

            # 상근이 이동
            for _ in range(len(queue)):
                row_s, col_s = queue.popleft()  # 상근이 현재 위치

                for dr, dc in dir:
                    row, col = row_s + dr, col_s + dc

                    if 0 <= col < w and 0 <= row < h:
                        if (row, col) not in visited and board[row][col] == '.':
                            queue.append((row, col))
                            visited.add((row, col))
                            time[row][col] = time[row_s][col_s] + 1

                    else:
                        return str(time[row_s][col_s] + 1)

        return "IMPOSSIBLE"

    # 상근의 초기 위치 저장
    visited = set()
    pos = pos(w, h, board)
    queue = deque([pos])
    visited.add(pos)

    # 불의 초기 위치 저장
    pos_fire = pos_fire(w, h, board)
    queue_fire = deque(pos_fire)

    return bfs(w, h, board, queue, visited, queue_fire)


# input
N = int(input())
results = []

for _ in range(N):
    w, h = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]
    results.append(solution(w, h, board))

print("\n".join(results))