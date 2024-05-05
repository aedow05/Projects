import turtle
import random
import math

# Import the missing setup function
from setup import setup_sprinting, make_competitor, starter_row, finish_row, competitor_info,track_width

def run_the_race(runner_count):
    writer = turtle.Turtle()
    writer.hideturtle()

    # go to printing text
    writer.pu()
    writer.goto(-100, -150)

    setup_sprinting()

    # Create as many competitors as the user indicated.
    competitors = []
    for i in range(runner_count):
        competitors.append(make_competitor(-track_width/2 + i * (track_width/(runner_count-1)), starter_row, ['black', 'blue']))

    # Print competitor information to the screen using a for loop.
    # Evenly distribute the turtles across the width of the track.
    # Stagger the competitor’s names across different rows so they do not overlap.
    for i in range(runner_count):
        # Write the name of each competitor below their turtle
        writer.pu()
        writer.goto(-track_width/2 + i * (track_width/(runner_count-1)), starter_row - i % 2 * 30)
        writer.pd()
        writer.color('white')  # Set text color to white
        writer.write(competitor_info[i][0], font=('Arial', 24, 'normal'))

    # Keep track of how many finished and in what order
    finished = []

    # Once they have all crossed the finish line, the race is over
    while len(finished) < runner_count:
        # Nest a for-loop inside this while loop to move each
        # competitor forward some random distance at each iteration.
        # The for loop is a counting loop that iterates as many times
        # as there are runners. You must use range because you will use
        # the index value to access different lists.

        # Change the first if-statement so that it uses your for loop
        # iterator, not a hard-coded index (e.g. [0]).

        # DELETE the if-statements for 'Jojo' and 'Lemon'

        for i in range(runner_count):
            competitor = competitors[i]

            # Move only if not finished the race
            if competitor_info[i][0] not in finished:
                # Move forward a random amount
                delta = random.randint(1, 9)
                competitor.forward(delta)

                # Check if they crossed the finish line
                if competitor.pos()[1] >= finish_row:
                    finished.append(competitor_info[i][0])

    writer.pu()
    writer.goto(-20, finish_row + 50)
    writer.pd()
    writer.write(f'The winner is {finished[0]}!!', False, font=('Arial', 24, 'normal'))

    return finished

if __name__ == '__main__':
    run_the_race(3)
