import math
import threading
import time
import turtle
from tkinter import *
from tkinter import font
from mazeGenerator import *

mazeSize = 10  # the size of maze array is (mazeSize * mazeSize)
boxSize = 560 / mazeSize  # determining visual area made by turtle

def mazeDrawer(arr, mazeSize, boxSize):  # the size of maze array is (mazeSize * mazeSize)
    if mazeSize % 2 == 0:  # 필요해보임 걍 (mazeGenerator 코드 참고) 아니 걍 없으면 오류날거가틈 !!!!
        mazeSize -= 1
    boxSize = math.floor(boxSize + 0.5)
    if boxSize % 2 != 0:  # 2로 나누어서 0 0 좌표를 조정하다보니 boxSize가 홀수면 이게 뭔가 안맞음
        boxSize -= 1
    global ARR
    ARR = arr
    global BOXSIZE
    BOXSIZE = boxSize
    global MAZESIZE
    MAZESIZE = mazeSize

    global myTurtle
    myTurtle = turtle.Turtle()  # turtle 객체 선언

    global screen
    screen = myTurtle.getscreen()
    turtle.tracer(0, 0)  # inhances the speed of drawing

    myTurtle.up()  # initiating location
    myTurtle.goto(-mazeSize * boxSize / 2, mazeSize * boxSize / 2)  # coordinating (0, 0)
    myTurtle.seth(0)
    myTurtle.down()

    for i in range(mazeSize):
        for j in range(mazeSize):
            if arr[i, j] == 0:
                rect()
            myTurtle.up()
            myTurtle.fd(boxSize)
            myTurtle.down()
        myTurtle.up()
        myTurtle.goto(-mazeSize * boxSize / 2, mazeSize * boxSize / 2 - boxSize * (i + 1))
        myTurtle.seth(0)
        myTurtle.down()
    # 미로 마지막에 골인지점 만들기
    myTurtle.up()
    myTurtle.goto(-mazeSize * boxSize / 2 + boxSize * (mazeSize - 2), mazeSize * boxSize / 2 - boxSize * (i - 1))
    myTurtle.pen(fillcolor="red", pencolor="red")
    myTurtle.down()
    rect()

    myTurtle.up()
    myTurtle.goto(-mazeSize * boxSize / 2 + boxSize * 3 / 2, mazeSize * boxSize / 2 - boxSize * 3 / 2)  # (1,1) 출발점으로 가기
    screen.update()
    screen.tracer(True)


def rect():  # drawing a rectangular
    myTurtle.begin_fill()
    for i in range(4):
        myTurtle.fd(BOXSIZE)
        myTurtle.rt(90)
    myTurtle.end_fill()


# Implemented by YEOUNHYEOK

row, col = 1, 1  # player의 배열에서의 초기 위치


def mazePlayer():
    global myTurtle
    global screen
    myTurtle.color("#FFBB00")  # 색깔 정하기 with RGB
    myTurtle.speed(0)  # 속도는 숫자가 작을수록 빠름
    myTurtle.shape("square")
    myTurtle.shapesize(BOXSIZE / 21)
    myTurtle.penup()  # 펜 들기 == 그림 그리지 않는 상태
    screen.listen()  # 프로그램 활성화
    screen.onkeypress(left, "Left")
    screen.onkeypress(right, "Right")
    screen.onkeypress(up, "Up")
    screen.onkeypress(down, "Down")
    screen.onkeypress(startGame, "p")
    global movement_thread
    movement_thread = threading.Thread(target=handle_movement)  # 플레이어 조작 스레드
    movement_thread.start()
    screen.update()
    screen.mainloop()  # 프로그램이 계속 동작하는 상태를 유지하겠다!




# 플레이어 조작 함수
def handle_movement():
    while True:
        # 터틀 모듈의 onkeypress 함수를 사용하여 이동키 입력을 처리


        screen.tracer(0, 0)
        screen.update()
        # 오류발생 ---------------------- 도착지에 터틀이 들어가지 못하는 경우가 있음
        if col == MAZESIZE - 2 and row == MAZESIZE - 2:  # 목적지에 다다를 경우 endGame()함수 실행
            global exit_flag
            exit_flag = True
            break
    print("조작스레드 종료")


def left():
    global row
    global col
    if ARR[row, col - 1] == 1:  # 미로배열에서 행과 열을 움직여 값이 1인 배열의 위치만 갈 수 있게 조건절을 만듬
        myTurtle.seth(180)
        myTurtle.forward(BOXSIZE)
        col = col - 1


def right():
    global row
    global col
    if ARR[row, col + 1] == 1:
        myTurtle.seth(0)
        myTurtle.forward(BOXSIZE)
        col = col + 1


def up():
    global row
    global col
    if ARR[row - 1, col] == 1:
        myTurtle.seth(90)
        myTurtle.forward(BOXSIZE)
        row = row - 1


def down():
    global row
    global col
    if ARR[row + 1, col] == 1:
        myTurtle.seth(270)
        myTurtle.forward(BOXSIZE)
        row = row + 1


# onkeypress(함수명, 키보드버튼명) :
# 어떤 버튼을 눌렀을 때, 이 함수가 동작하도록 하겠다!

# 타이머의 시간을 update 해주는 함수
def update_clock():
    global myTimer
    myTimer.clear()
    elapsed_time = time.time() - start_time
    if not exit_flag:  # flag가 False이면 계속 타이머 시간을 update
        myTimer.write("시간: {:.0f}".format(elapsed_time), align="center", font=("Courier", 24, "normal"))
        screen.tracer(0, 0)
        screen.update()
        screen.ontimer(update_clock, 1000)  # 1초쉬고 다시 update_clock함수를 호출
    else:
        global end_time
        end_time = elapsed_time-1  # elapsed_time - 1이 더 정확함
        myTimer.write("시간: {:.0f}".format(end_time), align="center", font=("Courier", 24, "normal"))
        print(end_time)
        endGame()

    print("타이머스레드 종료")





def timer():
    global myTimer
    myTimer = turtle.Turtle()
    myTimer.ht()
    myTimer.up()
    myTimer.goto(0, MAZESIZE * BOXSIZE / 2)
    # exit_flag가 False면 계속 반복 True면 종료
    global exit_flag
    exit_flag = False
    # 타이머 스레드
    global timer_thread
    timer_thread = threading.Thread(target=update_clock)
    timer_thread.start()
    global start_time
    start_time = time.time()

restart = True
# 게임 종료
# tkinter 창 띄우기
def endGame():
    def reset():
        global exit_flag
        global row, col
        global screen, restart
        exit_flag = False
        row,col = 1,1 # 초기위치 설정
        if entry.get() == "INSERT YOUR NAME" or entry.get() == '':
            myName = "NONAME"
        else:
            myName = entry.get() # 이름
        print(myName)
        rank(end_time, myName) # 종료시간이랑 이름을 매개변수로하고 그 안에서 순위 정하는 연산이 있음

        w.destroy()
        print("TK인터 종료")
        screen.resetscreen()
        screen.bye()
        turtle.TurtleScreen._RUNNING = True  # 구글링하다가 좋아보이는거 넣은거
        print("터틀 종료")
        if restart :
            startGame()
        restart = True

    def on_entry_click(event):
        if entry.get() == "INSERT YOUR NAME":
            entry.delete(0, END)  # 힌트 삭제
            entry.config(fg='black') # 글자 색상 변경

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, "INSERT YOUR NAME")  # 힌트 추가
            entry.config(fg='gray')  # 글자 색상 변경
    def quit():
        global life, restart
        life = 0
        restart = False
        reset()
        print("게임 종료")

    global end_time
    end_time = round(end_time,2)
    print("endGame")
    time.sleep(1)  # 1초쉬기, 이 코드가 없으면 update_clock에서 end_time값을 받아올 시간이 없음
    w = Tk()
    w.title("결과")
    w.geometry("600x400")
    w.resizable(False, False)

    label1 = Label(w, text="CONGRATULATION", font=("Arial", 30))
    if len(rank_list)!=0:
        label2 = Label(w, text=f"BEST : {rank_list[0][0]}")
    else:
        label2 = Label(w, text=f"BEST : ")
    label3 = Label(w, text=f"TIME: {end_time}초")
    label4 = Label(w, text="PLAY AGAIN?", font=("Arial", 25))
    label1.pack(side="top", pady=10)
    label2.pack(side="top")
    label3.pack(side="top")
    label4.pack(side="top", pady=30)

    btn1 = Button(w, text="YES", width=10, height=2, command=reset)
    btn2 = Button(w, text="NO", width=10, height=2, command=quit)
    btn1.pack(side="left", padx=80, anchor="n")
    btn2.pack(side="right", padx=80, anchor="n")


    entry = Entry(w, fg='gray')
    entry.insert(0, "INSERT YOUR NAME")  # 힌트 추가
    entry.bind('<FocusIn>', on_entry_click)  # 포커스를 받으면 힌트 삭제
    entry.bind('<FocusOut>', on_focus_out)  # 포커스를 잃으면 힌트 추가
    entry.pack()
    entry.pack(side="bottom",pady=70)
    w.mainloop()

def rank(record, user):
    global rank_list
    rank_list.append((record, user))
    rank_list.sort()
    if len(rank_list[:][0])>10:
        rank_list = rank_list[:10]
    with open("rank.txt", "w") as f:
        for i in range(len(rank_list)):
            f.write(f"{i+1}. {rank_list[i][0]} {rank_list[i][1]}\n")


#     def sort():
# InGame.py를 옮겨옴
# 왜냐면 startGame이라는 이 함수를 쓰기위해서 inGame.py를 임포트해야하는데 그러면
# InGame.py랑 mazeTurtle.py가 둘다 서로를 참조하면서 무슨 상호참조? 오류가 발생함
def startGame():
    print("스타트")
    mazeArr = mazeGenerator(mazeSize)
    mazeDrawer(mazeArr, mazeSize, boxSize)
    timer() # 타이머스레드 설정
    mazePlayer() # 플레이어슬레드 설정
    

rank_list = []

# 오류 게임중 갑자기 끄면 thread가 종료가 안되서 오류발생
if __name__ == "mazeTurtle":
    with open("rank.txt", "r") as f:
        for line in f:
            words = line.split()
            rank_list.append((float(words[1]), words[2]))

