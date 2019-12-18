import turtle
import time
import random

delay = 0.1

# Result
result = 0
high_score = 0

# Screen parameters
window = turtle.Screen()
window.title("Snake Game")
window.setup(width=700, height=700)
window.bgcolor("yellow")
window.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake snack
snack = turtle.Turtle()
snack.speed(0)
snack.shape("circle")
snack.color("black")
snack.penup()
snack.goto(0, 100)

snake_bodyparts = []

# Score inscription
score_inscription = turtle.Turtle()
score_inscription.speed(0)
score_inscription.shape("square")
score_inscription.color("black")
score_inscription.penup()
score_inscription.hideturtle()
score_inscription.goto(0, 300)
score_inscription.write("Score: 0  Best Score: 0", align="center", font=("Arial", 20, "bold"))


# Snake movements
def move_up():
    if head.direction != "down":
        head.direction = "up"


def move_down():
    if head.direction != "up":
        head.direction = "down"


def move_left():
    if head.direction != "right":
        head.direction = "left"


def move_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)


# Keyboard settings
window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Main game
while True:
    window.update()

    # Collision with the border
    if head.xcor() > 320 or head.xcor() < -320 or head.ycor() > 320 or head.ycor() < -320:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide snake body parts
        for segment in snake_bodyparts:
            segment.goto(1000, 1000)

        # Clear body parts list
        snake_bodyparts.clear()

        # Reset the result
        result = 0

        # Reset the delay
        delay = 0.1

        score_inscription.clear()
        score_inscription.write("Score: {}  Best Score: {}".format(result, high_score), align="center",
                                font=("Arial", 20, "bold"))

    # Collision with the snack
    if head.distance(snack) < 20:
        # Move the snack to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snack.goto(x, y)

        # Add new body part
        new_bodypart = turtle.Turtle()
        new_bodypart.speed(0)
        new_bodypart.shape("square")
        new_bodypart.color("yellowgreen")
        new_bodypart.penup()
        snake_bodyparts.append(new_bodypart)

        # Shorten the delay
        delay -= 0.001

        # Increase the result
        result += 10

        if result > high_score:
            high_score = result

        score_inscription.clear()
        score_inscription.write("Score: {}  Best Score: {}".format(result, high_score), align="center",
                                font=("Arial", 20, "bold"))

    # Move the end body parts first in reverse order
    for index in range(len(snake_bodyparts) - 1, 0, -1):
        x = snake_bodyparts[index - 1].xcor()
        y = snake_bodyparts[index - 1].ycor()
        snake_bodyparts[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(snake_bodyparts) > 0:
        x = head.xcor()
        y = head.ycor()
        snake_bodyparts[0].goto(x, y)

    move()

    # Check for head collision with the body parts
    for segment in snake_bodyparts:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide snake body parts
            for segment in snake_bodyparts:
                segment.goto(1000, 1000)

            # Clear snake body parts list
            snake_bodyparts.clear()

            # Reset the result
            result = 0

            # Reset the delay
            delay = 0.1

            # Update the result display
            score_inscription.clear()
            score_inscription.write("Score: {}  Best Score: {}".format(result, high_score), align="center",
                                    font=("Arial", 20, "bold"))

    time.sleep(delay)

window.mainloop()