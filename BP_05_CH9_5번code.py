import turtle               # turtle 모듈을 가져온다
import random               # random 모듈을 가져온다

t = turtle.Turtle()         # 변수 t에 turtle값을 저장한다
s = turtle.Screen()         # 변수 s에 screen값을 저장한다

def draw_shape(t, c, length, sides, x, y):  # draw_shape라는 함수를 정의내린다
    t.up()              # 펜을 들어올린다
    t.goto(x, y)        # 거북이를x,y 좌표로 이동시킨다
    t.down()            # 펜을 내린다
    t.fillcolor(c)      # c로 거북이의 색을 정한다 
    angle = 360.0 / sides  # angle이라는 변수를 360를 sides로 나눈 값으로 정한다
    t.begin_fill()      # 색을 채우기 시작한다 
    for dist in range(sides):  # 간격을 다루는 함수
        t.forward(length)    # length 만큼 앞으로 이동한다
        t.left(angle)        # angle만큼 왼쪽으로 회전한다
    t.end_fill()        # 색채우기를 끝낸다 

for i in range(10):        #아래의 문장을 10번 반복한다
    color = random.choice([ 'white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ])      # 지정한 색깔들을 랜덤하게 출력한다
    side_length = random.randint(10, 100) #10에서 100사이의 수 중 한 수를 랜덤하게 출력한다
    sides = random.randint(3, 10)
    x = random.randint(-200, 200)     #-200에서 200사이의 수 중 한 수를 랜덤하게 출력한다 
    y = random.randint(-200, 200)
    draw_shape(t, color, side_length, sides, x, y)
