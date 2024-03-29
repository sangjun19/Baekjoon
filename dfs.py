# N*N크기의 배열이 주어졌을때 1의 개수는 몇개인지 세어보기 dfs를 이용해서
# 하나의 시작 1로 부터 붙어져 있는 연속된 1의 개수 세어보기 => 2, 13이 답이 됨.
# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000
# 방향잡기(상,우,하,좌)
dr = [-1,0,1,0]
dc = [0,1,0,-1]
# 행과 열의 좌표가 들어옴
def DFS(r, c):
    global cnt
    # 해당 arr[r][c] 자리값이 1이므로 방문체크와 동시에 카운트를 1증가
    arr[r][c] = 0
    cnt += 1
    # 4방 탐색
    for i in range(4):
        # 새로운 좌표값을 활용
        nr = r + dr[i]
        nc = c + dc[i]

        # 새로운 좌표값을 활용한 범위검사
        # 범위를 벗어나면 다른 방향을 탐색
        # if 0<=nr<N and 0<=nc<N: 조건도 가능(파이썬에서만)
        if nr<0 or nr>= N or nc <0 or nc>=N:
            continue
        # 이미 방문을 했어도 종료(이것이 없으면 무한으로 방문)
        # 이 아래 조건을 위에 한꺼번에 쓸거면 단축평가 오른쪽엔 가능함 근데 이거 따로쓸거면 맵 제한조건보다 위에 두면 조짐. 
        if arr[nr][nc] == 0:
            continue
        # 걸러낼 조건을 모두 걸러내면 재귀가 가능
        DFS(nr, nc)  # 또 한 뎁스 들어가라!!

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]  # 행의 길이만큼 만들어준다

# 입력이 끝났으면 처음 시작 위치 찾기
for i in range(N):  # 행우선순회 하면서 전부다 보되
    for j in range(N):
        if arr[i][j] == 1:  # 그자리가 1이야?
            cnt = 0  # prep 하고
            DFS(i, j)  # dfs 해!
            print(cnt)