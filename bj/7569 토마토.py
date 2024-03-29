import sys
from collections import deque

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
##M,N 상자크기 H 높이
M, N, H = map(int, sys.stdin.readline().split())
box = [[[0] * (M) for _ in range(N)] for _ in range(H)]
for h in range(H):
    for j in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        box[h][j] = line

print(*box[0], sep="\n")

# 1 익었다 0 익지않았다 -1 없다
vx = (0, 0, -1, 1)
vy = (-1, 1, 0, 0)


def bfs(x, y, step):
    cnt = 0  ##depth 일수를 세는 변수
    queue = deque()
    queue.append([x, y])
    l = []
    l.append([x, y])

    while queue:
        # print(cnt)
        x, y = queue.popleft()
        ##위, 아래, 왼, 오 x(0,0,-1,1) y(-1,1,0,0)
        for j in range(4):
            xx = x + vx[j]
            yy = y + vy[j]
            if yy >= 0 and yy < N and xx >= 0 and xx < M:
                if step[y + vy[j]][x + vx[j]] == 0:
                    step[y + vy[j]][x + vx[j]] = 1
                    l.append([x, y])
                    cnt += 1

    return cnt


# for i in range(N): ##y
#     for j in range(M): ##x
#         if box[0][i][j]==1:
#             cnt2=bfs2(j,i,box[0])
#             print(cnt2)

cnt2 = bfs2(3, 1, box[0])

print("==============")
print(*box[0], sep="\n")

print(cnt2)
