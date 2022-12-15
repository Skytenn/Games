import random
import turtle

##### Turtle 
turtle.title('Tic Tac Toe')
t=turtle.Turtle()


def draw_board():
    t.pensize(3)
    t.fd(300)
    t.bk(200)
    t.lt(90)
    t.fd(100)
    t.bk(300)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.bk(300)
    t.fd(100)
    t.rt(90)
    t.fd(200)
    t.bk(300)
def draw_x(x,y):
    t.pencolor('red')
    t.penup()
    t.goto(x,y)
    t.pd()
    t.lt(0)
    t.rt(45)
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.rt(45)
def draw_circle(x,y):
    t.pencolor('blue')
    t.penup()
    t.goto(x,y)
    t.pd()
    t.circle(30)
    t.penup()
def draw_horizontal_line(x,y):
    t.penup()
    t.goto(x,y)
    t.pd()
    t.lt(0)
    t.rt(90)
    t.fd(300)
    t.bk(300)
    t.rt(180)
def draw_ver_line(x,y):
    t.penup()
    t.goto(x,y)
    t.pd()
    t.lt(0)
    t.rt(180)
    t.fd(300)
    t.lt(0)
def draw_left_line(x,y):
    t.penup()
    t.goto(x,y)
    t.pd()
    t.lt(0)
    t.rt(135)
    t.fd(400)
def draw_right_line(x,y):
    t.penup()
    t.goto(x,y)
    t.pd()
    t.lt(0)
    t.lt(135)
    t.fd(400)
def draw_marker(player,player_pos):
    if player_pos==1 and player=='o':
        draw_circle(80,50)
    elif player_pos==2 and player=='o':
        draw_circle(180,50)
    elif player_pos==3 and player=='o':
        draw_circle(280,50)
    elif player_pos==4 and player=='o':
        draw_circle(80,-40)
    elif player_pos==5 and player=='o':
        draw_circle(180,-40)
    elif player_pos==6 and player=='o':
        draw_circle(280,-40)
    elif player_pos==7 and player=='o':
        draw_circle(80,-140)
    elif player_pos==8 and player=='o':
        draw_circle(180,-140)
    elif player_pos==9 and player=='o':
        draw_circle(280,-140)

    elif player_pos==1 and player=='x':
        draw_x(10,10)
    elif player_pos==2 and player=='x':
        draw_x(110,10)
    elif player_pos==3 and player=='x':
        draw_x(210,10)
    elif player_pos==4 and player=='x':
        draw_x(10,-90)
    elif player_pos==5 and player=='x':
        draw_x(110,-90)
    elif player_pos==6 and player=='x':
        draw_x(210,-90)
    elif player_pos==7 and player=='x':
        draw_x(10,-190)
    elif player_pos==8 and player=='x':
        draw_x(110,-190)
    else:
        draw_x(210,-190)

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
vs=' '
player1=' '
player2=' '
player1_pos=' '
player2_pos=' '
moves_played=0
def check_emptyspaces():
    check=0 
    for x in range(1,10):
        if board[x]==' ':
            check=1
    if check==1:
        check=0
        return True
    else:
        check=0
        return False
def user_input(player):
    a=0
    if check_emptyspaces()==True:
        while type(a)!=type('int'):
            try:
                a = int(input("Тоглогч "+player+" 1-ээс 9-ийн хооронд тоо оруулна уу: "))
                if a>0 and a<= 9:
                    return a
                else:
                    print("Буруу утга оруулсан байна, Дахин тоо оруулна уу! ")
                    a=None
            except ValueError:
                print("Буруу утга оруулсан байна, Дахин тоо оруулна уу! ")
    else:
        print("Тэнцлээ")
def validate_position(position):
    if board[position] == ' ':
        return True
    else:
        return False
def check_wins(player):
    if board[1]==player and board[2]==player and board[3]== player:
        draw_horizontal_line(10,50)
        return True
    elif board[4]== player and board[5]== player and board[6]== player:
        draw_horizontal_line(10,-50)
        return True
    elif board[7]== player and board[8]== player and board[9]== player:
        draw_horizontal_line(10,-150)
        return True

    elif board[1]== player and board[5]== player and board[9]== player:
        draw_left_line(10,90)
        return True
    elif board[3]== player and board[5]== player and board[7]== player:
        draw_right_line(300,90)
        return True

    elif board[1]== player and board[4]== player and board[7]== player:
        draw_ver_line(50,90)
        return True
    elif board[2]== player and board[5]== player and board[8]== player:
        draw_ver_line(150,90)
        return True
    elif board[3]== player and board[6]== player and board[9]== player:
        draw_ver_line(250,90)
        return True
    else:
        return False
def update(player, player_pos):
    global moves_played
    if moves_played!=9:
        while validate_position(player_pos)!=True:
            player_pos = user_input(player)
            validate_position(player_pos)
        else:
            if check_emptyspaces()==True:

                board[player_pos]=player
                draw_marker(player, player_pos)
                moves_played+=1
def generate_random():
    return random.randint(1,9)               




print("-------------Tic Tac Toё тоглоомд тавтай морилно уу-------------")
print("----------------------------Дүрэм-------------------------------")
print("****************************************************************")
print("* Сонгосон тэмдэгээ 3 дараалуулан байрлуулах \n* 1- ээс 9-ийн хооронд утга гараас оруулах  \n* Зүүн дээд булан 1ээс эхлэн Баруун доод булан  9 хүртэл байна")
print("*******************************************")
print("Доор гарч ирэх хувилбараас сонголт хийнэ үү: ")
print("----------------------------------------------")
print("1. Тоглогч  VS Комьпютер \n2. Тоглогч  VS Хүн  ")
print("----------------------------------------------")

while vs ==' ' or vs>2:
    try:    
        vs=int(input("Сонгосон дугаараа оруулна уу:"))
        if vs >0 and vs<=2:
            while player1 != 'x' or player1 != 'o':
                player1= str(input("Тоглогч 1 дараах сонголтуудаас сонгох X эсвэл O :"))
                if player1 == 'x' or player1=='o':
                    if player1=='x':
                        player2='o'
                    else:
                        player2='x'
                    print("Тоглоом эхэллээ!! \n")
                    #draw()
                    draw_board()                   

                    while check_emptyspaces()== True:
                        ### Player 1
                        player1_pos=user_input(player1)
                        update(player1, player1_pos)

                        if check_wins(player1)== True:
                            t.penup()
                            t.goto(20,120)
                            t.pendown()
                            t.write("Тоглоом дууслаа.", font=("Arial",20,"normal"))
                            print("Баяр хүргэе тоглогч", player1, "хожлоо !!!")
                            break

                        ### player 2
                        if vs==1:
                            player2_pos=generate_random()
                            if moves_played!=9:
                                while validate_position(player2_pos)!= True:
                                    player2_pos=generate_random()
                                    validate_position(player2_pos)
                                
                                else:
                                    board[player2_pos]=player2
                                    draw_marker(player2,player2_pos)
                                    moves_played+=1

                                    if check_wins(player2)== True:
                                        t.penup()
                                        t.goto(20,120)
                                        t.pendown()
                                        print("Баяр хүргэе тоглогч", player2,"хожлоо!!!!")
                                        break
                        else:
                            player2_pos=user_input(player2)
                            update(player2,player2_pos)
                            ### check for player 2 if wins.
                            if check_wins(player2)==True:
                                print("Баяр хүргэе тоглогч", player2,"хожлоо!!!!")
                                t.penup()
                                t.goto(20,120)
                                t.pendown()
                                t.write("Тоглоом дууслаа.",font=("Arial",15,"normal"))
                                break
                    if check_emptyspaces()!=False:
                        t.penup()
                        t.goto(20,120)
                        t.pendown()
                        t.write("Тоглоом дууслаа.",font=("Arial",20,"normal"))
                        #print("Тоглоом дууслаа.")

                    break
    except ValueError:
        print(" Оруулсан утга тоо биш байна  Дахин оруулна уу! ") 
turtle.done()                  
                    
