import turtle

def draw_circle( t, position, radius, colors ):
    '''
    Draw a circle at location (x,y), with given radius and color.
    color is a LIST of 2 strings: the first is pen color, and
    the second is fill color.
    '''

    # move turtle to (x,y) -- without drawing
    t.pu()
    t.goto(position[0],position[1])
    t.pd()

    # ready the colors for outline and fill
    t.color(colors[0],colors[1])
    t.begin_fill()

    # draw the circle
    t.circle(radius)

    t.end_fill()

def draw_ellipse( t, position, height, width, colors ):
    '''
    Draw an ellipse at location (x,y), with given height,width, and color.
    color is a LIST of 2 strings: the first is pen color, and
    the second is fill color.
    '''

    # move turtle to (x,y) -- without drawing
    t.pu()
    t.goto(position[0],position[1])
    t.pd()

    # ready the colors for outline and fill
    t.color(colors[0],colors[1])
    t.begin_fill()

    # draw the circle
    t.circle(height//2,140)
    t.circle(width//2,40)
    t.circle(height//2,140)
    t.circle(width//2,40)

    t.end_fill()


def draw_rectangle( t, position, h, w, colors ):
    '''
    Draw a rectangle at location (x,y) -- this is the lower left corner.
    rectangle has height h and width w
    color is a LIST of 2 strings: the first is pen color, and
    the second is fill color.
    '''

    # extract the x- y-coordiantes from position
    x = position[0]
    y = position[1]

    # move the turtle to (x,y) -- without drawing
    t.pu()
    t.goto(x,y)
    t.pd()

    # ready the colors
    t.color(colors[0],colors[1])
    t.begin_fill()

    # draw the 4 sides
    t.goto(x+w,y)
    t.goto(x+w,y+h)
    t.goto(x,y+h)
    t.goto(x,y)

    t.end_fill()
    

    

def draw_triangle( t, position, h, w, colors ):
    '''
    Draw a triangle at location (x,y) -- this is the lower left corner.
    The triangle has height h and width w
    color is a LIST of 2 strings: the first is pen color, and
    the second is fill color.

    This assumes an equilateral triangle. The three points of the triangle
    are (x,y), (x+w,y), and (x+w//2,y+h).
    '''

    # extract the x- y-coordiantes from position
    x = position[0]
    y = position[1]

    # move the turtle to (x,y) -- without drawing
    t.pu()
    t.goto(x,y)
    t.pd()
    # set up color    
    t.color(colors[0],colors[1])
    t.begin_fill()
    # navigate to the 3 points of the triangle
    t.goto(x+w,y)
    t.goto(x+w//2,y+h)
    t.goto(x,y)
    
    t.end_fill()



# Test code
if __name__ == '__main__':
    t = turtle.Turtle()
    t.speed(15)
    draw_circle(t,[0,-80],200,['black','orange'])
    draw_rectangle(t,[-50,0],30,140,['black','black'])
    draw_triangle(t,[-130,120],60,80,['black','black'])
    draw_triangle(t,[40,120],60,80,['black','black'])
    draw_rectangle(t,[-10,280],110,50,['green','green'])
    

