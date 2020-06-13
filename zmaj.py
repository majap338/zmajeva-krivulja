import turtle
def dragon(red, l):
    if red==0:
        turtle.forward(l)
    elif red>0:
        dragon(red-1, l)
        turtle.right(90)
        dragon(-red+1, l)
    else:
        dragon(-red-1, l)
        turtle.left(90)
        dragon(red+1, l)

dragon(8, 15)
