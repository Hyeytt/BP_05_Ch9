import turtle                      # turtle 모듈을 불러온다
import random                      # random 모듈을 불러온다
t = turtle.Turtle()                # 변수 t에 turtle 함수를 부여한다
s = turtle.Screen()                # 변수 s에 screen 함수를 부여한다
s.bgcolor("black")                 # 배경색은 검은색으로 한다
def draw_star(aturtle, colour, side_length, x, y): # draw_star함수를 정의한다
    aturtle.color(colour)        # aturtle의 색을 colour값으로 정한다
    aturtle.begin_fill()         # aturtle의 색을 채우기 시작한다
    aturtle.penup()              # 펜을 들어올린다
    aturtle.goto(x, y)           # x,y 좌표로 이동시킨다
    aturtle.pendown()            # 펜을 내린다
    for i in range(5):           # 아래의 문장들을 5번 반복한다
        aturtle.forward(side_length) # side_length만큼 앞으로 이동시킨다
        aturtle.right(144)       # 오른쪽으로 144만큼 회전시킨다
        aturtle.forward(side_length)  #  side_length만큼 앞으로 이동시킨다
    aturtle.end_fill()           # turtle의 색을 채우기를 끝낸다
for i in range(20):              # 아래의 문장들을 20번 반복한다.
    color = random.choice([ 'white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ])                      # 적어놓은 색의 순서로 색을 채운다
    side_length = random.randint(10, 100)   # side_length는 10에서 100까지의 수 중에서 랜덤으로 한다
    x = random.randint(-200, 200)   # x는 -200에서 200까지의 수 중에서 랜덤으로 한다
    y = random.randint(-200, 200)   # y는 -200에서 200까지의 수 중에서 랜덤으로 한다
    draw_star(t, color, side_length, x, y) 
