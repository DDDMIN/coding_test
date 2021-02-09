#4.4 n * m 크기의 직사각형 좌표에서 캐릭터가 움직이는 문제.
#1. 왼쪽에 안가본 칸이 있으면 왼쪽으로 회전 후 한 칸 전진
#2. 왼쪽이 가본 칸이면 왼쪽 회전만
#3. 네 방향 모두 가본칸이거나 바다면 방향 유지한채로 한칸 뒤로간다. 뒤가 바다면 멈춘다
#4. 방문한 칸의 숫자는?

#입력예시
# 4 4   # 4*4맵 생성
# 1 1 0  # 1, 1에 북쪽(0)을 바라보는 캐릭터
# 1 1 1 1   #첫 줄은 모두 바다
# 1 0 0 1   #둘째 줄은 바다/육지/육지/바다
# 1 1 0 1   #셋째 줄은 바다/바다/육지/바다
# 1 1 1 1   #넷째 줄은 모두 바다
#정답 : 3


n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화[1]
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 x y 좌표, 방향 입력받기
x, y, direction = map(int, input().split())
#현재 좌표 방문으로 표기[2]
d[x][y] = 1

#전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북 동 남 서 방향 정의하기
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

#왼쪽으로 회전 정의 direction 북(0) 동(1) 남(2) 서(3)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1 #[3]방문한 칸을 세는 문제니깐 처음 위치도 카운트 포함해아한다
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전 한 이후 가보지 않은 칸이고 바다가 아니면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue #turn left로 간다
    #회전 한 이후 가본 칸이거나 바다일경우
    else:
        turn_time += 1  #turn left로 간다
    #네번 회전한 경우 온 방향으로 한칸 되돌아간다
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤가 바다가 아니면 되돌아 간다
        if array[nx][ny] == 0: #[4]
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우 멈춘다
        else:
            break
        turn_time = 0

#정답 출력
print(count)

            



#각주

#방향과 dx dy 설정이 중요
#map 함수를 써서 가본 위치와 육지인지 바다인지 정보를 설정해야한다
#
  
#[1]방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# n, m = map(int, input().split())
# d = [[0] * m for in _ range(n)]
# 4 4
# d = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

#[1-1] range의 범위
# range(n) = 0, 1, 2, 3, ...., n-1

#[2]현재 좌표 방문으로 표기
# d[x][y] = 1
# d = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

#[3]방문한 칸을 세는 문제니깐 처음 위치도 카운트 포함해아한다
#count = 1
#[4] 바다인지 아닌지 체크해야하니깐 array를 써야한다
#if array[nx][ny] == 0: 
