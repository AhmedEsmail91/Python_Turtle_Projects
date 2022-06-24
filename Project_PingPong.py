import turtle
import time
if __name__ == "__main__":
    # make screen
    wind = turtle.Screen()  # make screen
    wind.title("Ping Pong")
    wind.bgcolor("#444")
    wind.setup(width=800, height=600)
    wind.tracer(0)  # stops window from updating

    # make madrab1

    mad1 = turtle.Turtle()
    mad1.speed(0)
    mad1.shape("square")
    mad1.color("#eee")
    mad1.penup()  # removing the turtle from making any lines while moving
    mad1.goto(-350, 0)
    mad1.shapesize(stretch_wid=5, stretch_len=1)

    # make madrab2
    mad2 = turtle.Turtle()
    mad2.speed(0)
    mad2.shape("square")
    mad2.color("red")
    mad2.penup()  # removing the turtle from making any lines while moving
    mad2.goto(350, 0)
    mad2.shapesize(stretch_wid=5, stretch_len=1)

    # make ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.shapesize(stretch_len=0.8, stretch_wid=0.8)
    ball.goto(0, 0)
    ball.color("purple")
    ball.penup()
    ball.dx = 0.8
    ball.dy = 0.8
    # Score
    score1 = 0
    score2 = 0
    score = turtle.Turtle()
    score.speed(0)
    score.penup()
    score.color("black")
    score.hideturtle()
    score.goto(0, 260)
    score.write("Player1 : 0  Player2: 0", align="center", font=25)

    def mad1_up():
        y = mad1.ycor()
        y += 50
        mad1.sety(y)

    def mad1_down():
        y = mad1.ycor()
        y -= 50
        mad1.sety(y)

    def mad2_up():
        y = mad2.ycor()
        y += 50
        mad2.sety(y)

    def mad2_down():
        y = mad2.ycor()
        y -= 50
        mad2.sety(y)

    # keyboard actions:
    wind.listen()
    wind.onkeypress(mad1_up, "w")
    wind.onkeypress(mad1_down, "s")
    wind.onkeypress(mad2_up, "Up")
    wind.onkeypress(mad2_down, "Down")

    '''
        ------To_Make_Ball_Hitting_All_Corners------
        def ball_xback():
            if ball.xcor()>350:
                ball.setx(350)
                ball.dx*=-1
            if ball.xcor()<-350:
                ball.setx(-350)
                ball.dx*=-1
        '''

    def hitter1_ball():
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < mad1.ycor() + 40 and ball.ycor() > mad1.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

    def hitter2_ball():
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < mad2.ycor() + 40 and ball.ycor() > mad2.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1

    while True:
        wind.update()  # updated screen
        # moxing the ball
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score.clear()

            score1 += 1
            score.write("Player1 : {}  Player2: {}".format(
                score1, score2), align="center", font=25)
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score.clear()

            score2 += 1
            score.write("Player1 : {}  Player2: {}".format(
                score1, score2), align="center", font=25)

        hitter1_ball()

        hitter2_ball()
        if score1 == 3 or score2 == 3:
            turtle.Turtle().write("Game Over", align="center", font=("Bold", 60))
            time.sleep(0.8)
            break
