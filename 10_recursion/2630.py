# https://www.acmicpc.net/problem/2630
def solution(N, w, h):

    # board 의 width : w ~ w + N, height: h ~ h + N 범위 내 타일 모두 동일 타일인지 확인
    val = board[h][w]

    for i in range(h, h + N):
        for j in range(w, w + N):
            # 동일 타일이 아니면, 가로세로 이등분하여 동일 타일 재확인
            if board[i][j] != val:
                n = N//2
                w1, b1 = solution(n, w, h)
                w2, b2 = solution(n, w+n, h)
                w3, b3 = solution(n, w, h+n)
                w4, b4 = solution(n, w+n, h+n)
                return (w1+w2+w3+w4, b1+b2+b3+b4)

    return (0, 1) if val else (1, 0)


# input
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# solution
white_cnt, blue_cnt = solution(N, 0, 0)
print(white_cnt)
print(blue_cnt)