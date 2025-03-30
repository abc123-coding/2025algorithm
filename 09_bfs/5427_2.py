from collections import deque

def solution(w, h, board):
    
    def find_initial_position(whose):

        time = [[-1] * w for _ in range(h)]

        if whose == 'person':
            for i in range(h):
                for j in range(w):
                    if board[i][j] == '@':
                        time[i][j] = 0
                        return deque([(i, j)]), time
                    
        else : # fire
            fire_position = deque()
            for i in range(h):
                for j in range(w):
                    if board[i][j] == '*':
                        time[i][j] = 0
                        fire_position.append((i, j))

            return fire_position, time

    def bfs(queue, time):

        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            y, x = queue.popleft()

            for dir in direction:
                ny, nx = y + dir[0], x + dir[1]

                if 0 <= nx < w and 0 <= ny < h and board[ny][nx] != '#' and time[ny][nx] < 0:
                    time[ny][nx] = time[y][x] + 1
                    queue.append((ny, nx))

        return time

    def cmp_time(person_time, fire_time):

        min_time = float("inf")

        for i in range(h):
            for j in [0, w-1]:
                if 0 <= person_time[i][j] < fire_time[i][j] or (person_time[i][j] >= 0 and fire_time[i][j] < 0):
                    min_time = min(min_time, person_time[i][j])

        for i in [0, h-1]:
            for j in range(w):
                if 0 <= person_time[i][j] < fire_time[i][j] or (person_time[i][j] >= 0 and fire_time[i][j] < 0):
                    min_time = min(min_time, person_time[i][j])

        return min_time + 1 if min_time < float("inf") else "IMPOSSIBLE"

    person_queue, person_time = find_initial_position('person')
    fire_queue, fire_time = find_initial_position('fire')

    person_time = bfs(person_queue, person_time)
    fire_time = bfs(fire_queue, fire_time)

    return cmp_time(person_time, fire_time)


# input 
N = int(input())

output = []

for _ in range(N):

    w, h = map(int, input().split())
    board = [input() for _ in range(h)]

    # output
    output.append(solution(w, h, board))

print('\n'.join(map(str, output)))