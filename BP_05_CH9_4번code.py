import turtle                         # 라이브러리에서 turtle모듈을 불러온다
import random                         # 라이브러리에서 random모듈을 불러온다 
t = turtle.Turtle()                   # 변수 t에 turtle값을 저장한다
t.shape("turtle")                     # 커서의 모양을 turltle로 한다 
def draw_square(x, y, c):             # 사각형을 그리는 draw_square함수를 정의한다
    t.up()                            # 펜을 든다
    t.goto(x, y)                      # x,y로 이동시킨다
    t.down()                          # 펜을 내려 놓는다
    t.color("black",c)                
    t.begin_fill()                    # 색을 채우기 시작한다
    t.forward(100)                    # 거북이를 앞으로 100만큼 이동시킨다
    t.left(90)                        # 거북이를 왼쪽으로 90도 회전시킨다
    t.forward(100)                    # 거북이를 앞으로 100만큼 이동시킨다
    t.left(90)                        # 거북이를 왼쪽으로 90도 회전시킨다
    t.forward(100)                    # 거북이를 앞으로 100만큼 이동시킨다
    t.left(90)                        # 거북이를 왼쪽으로 90도 회전시킨다
    t.forward(100)                    # 거북이를 앞으로 100만큼 이동시킨다
    t.left(90)                        # 거북이를 왼쪽으로 90도 회전시킨다 
    t.end_fill()                      # 색채우기를 끝낸다
for c in ["yellow", "red", "purple", "blue"]: #노란색, 빨간색, 보라색, 파랑색 순으로 색을 칠한다
    x = random.randint(-100, 100)    # 랜덤하게 색을 채우는 범위를 가로 -100에서 100까지 
    y = random.randint(-100, 100)    # 랜덤하게 색을 채우는 y축의 범위를 -100에서 100까지 정한다
    draw_square(x, y, c)             # 사각형을 출력한다
