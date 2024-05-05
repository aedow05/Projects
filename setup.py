import turtle
import shapes

# competitor information
# Feel free to change these to whatever you would like!
competitor_info = [ ['Daisy','blue'],['Jojo','green'],['Lemon','yellow'],['Tulip','orange'],
                    ['June','red'],['Zippy','purple'],['Blush','DeepPink'],['Fluffy','Lime'] ]

# You might need to change these values to better fit to your computer
# main window
window_height = 800
window_width = 500
max_row = window_height//2
max_col = window_width//2

# basic colors - feel free to change these
ground_color = 'green'
sky_color = 'SkyBlue'

# location and size of sprinter track
finish_row = 300
starter_row = -300
track_width = 600
track_color = 'Gainsboro'


# shotput information
# Row at which the ground is drawn. Competitors are on the ground.
ground_row = -100

# default drawing speed for any new competitor
DEFAULT_SPEED = 15


def make_competitor(x,y,colors):
    '''
    Create a big turtle at the given location.
    Use the "turtle" icon.
    The newly constructed turtle is returned.
    '''
    t = turtle.Turtle()
    t.speed(DEFAULT_SPEED)
    t.color(colors[0],colors[1])

    # increase the size of the turtle -- it is too small
    t.resizemode("user")
    t.shapesize(2,2,1)
    t.shape("turtle")

    # go to its starting position and point "north"
    t.penup()
    t.goto(x,y)
    t.seth(90)
    t.pendown()
    return t


def setup_sprinting():

    # start fresh
    turtle.clearscreen()

    # control the size of the screen and background color
    turtle.screensize(window_width,window_height,ground_color)

    # draw the track
    t = turtle.Turtle()
    t.speed(15)
    t.pensize(5)
    t.penup()
    # the track is a gray strip from bottom to top. positioned at lower left corner
    x = -track_width//2
    y = -max_row
    shapes.draw_rectangle(t,[x,y],window_height,track_width,[track_color,track_color])

    # Draw start line -- thick black line where competitors start race
    t.penup()
    t.goto(x,starter_row)
    t.color('black')
    t.pendown()
    t.pensize(10)
    t.forward(track_width)
    t.pensize(1)
    
    # Draw finish line -- red/white stripe they cross to finish
    t.penup()
    t.goto(x,finish_row)
    t.color('red','red')
    t.pensize(5)
    t.pendown()
    t.forward(track_width)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.color('white','white')
    t.forward(track_width)


def setup_shotput():

    # start fresh
    turtle.clearscreen()
    
    # Establish window size and background color
    turtle.screensize(window_width,window_height,sky_color)

    # create turtle - fat and fast!
    t = turtle.Turtle()
    t.speed(15)
    t.pensize(5)
    
    # Draw the ground
    x = -max_col-200
    y = -max_row
    height = abs(-max_row - ground_row)
    shapes.draw_rectangle(t,[x,y],height,window_width*2,[ground_color,ground_color])







