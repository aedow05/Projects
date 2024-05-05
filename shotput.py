import turtle
import random
import math

from setup import *

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)
def go_shotput(putters):
    setup_shotput()

     # List to store shot put results for each competitor
    shot_results = []

    for _ in range(putters):
        startx = -max_col + 50
        starty = ground_row

        lemon = make_competitor(startx, starty, ['black', 'yellow'])

        offsetx = startx - 20
        offsety = starty + 20

        shot = turtle.Turtle()
        shot.speed(15)
        shot.hideturtle()
        shot.penup()
        shot.goto(offsetx, offsety)
        shot.color('black', 'black')
        shot.pendown()
        shot.begin_fill()
        shot.circle(10)
        shot.end_fill()

        angle = random.randint(20, 70)
        velocity = random.randint(20, 60)

        lemon.seth(angle)

        gravity = 9.81

        x = 1
        y = 1
        vx = velocity * math.cos(math.radians(angle))
        vy = velocity * math.sin(math.radians(angle))
        dt = 0.5

        while y >= 0:
            shot.color(sky_color, sky_color)
            shot.begin_fill()
            shot.circle(12)
            shot.end_fill()
            shot.color('black', 'black')

            x = x + vx * dt
            y = y + vy * dt
            vy = vy - 0.5 * gravity * dt

            shot.pu()
            shot.goto(x + offsetx, y + offsety)
            shot.begin_fill()
            shot.circle(10)
            shot.end_fill()

            shot.color(sky_color, sky_color)
            shot.begin_fill()
            shot.circle(12)
            shot.end_fill()
            shot.color('black', 'black')

        # Mark where the shot put landed and record the distance thrown
        distance = math.sqrt((x + offsetx) ** 2 + (y + offsety) ** 2)
        shot_results.append([distance, f'Competitor {_ + 1}'])

        # Draw a flag at the landing spot
        flag = turtle.Turtle()
        flag.hideturtle()
        flag.pu()
        flag.goto(x + offsetx, y + offsety)
        flag.color('yellow')
        flag.pendown()
        flag.begin_fill()
        for _ in range(4):
            flag.forward(10)
            flag.right(90)
        flag.end_fill()

        # Pause between each competitor
        input(f'Press Return to continue to the next competitor ({_ + 1})')

    # Sort the shot results in descending order (largest distance first)
    shot_results.sort(reverse=True)

    # Call the awards ceremony function
    awards_ceremony(shot_results)

def awards_ceremony(winners):
    podium_heights = [200, 150, 100]

    i = 0  # Initialize the index manually
    for winner in winners[:3]:
        winner_turtle = make_competitor(-50 + i * 50, starter_row, ['black', 'gold'])
        winner_turtle.shapesize(4, 4, 1)

        medal = turtle.Turtle()
        medal.hideturtle()
        medal.pu()
        medal.goto(winner_turtle.xcor(), winner_turtle.ycor() + 50)
        medal.color(winner_turtle.fillcolor())
        medal.begin_fill()
        medal.circle(10)
        medal.end_fill()

        i += 1  # Increment the index 



if __name__ == '__main__':
    # Adjust the number of competitors as needed
    competitor_count = 3
    go_shotput(competitor_count)


