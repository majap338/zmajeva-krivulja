import turtle
r=["F", "X"]
def rewriting():
    i=0
    while i < len(r):
        if r[i]=="X":
            r[i:i+1]="X", "+", "Y", "F", "+"
            i+=4
        if r[i]=="Y":
            r[i:i+1]="-", "F", "X", "-", "Y"
            i+=4
        i+=1
    return r
def draw(l,a):
    for i in range(len(r)):
        if r[i]=="F":
            turtle.forward(l)
        if r[i]=="+":
            turtle.right(a)
        if r[i]=="-":
            turtle.left(a)
def dragon(red, l, a):
    for i in range(red):
        rewriting()
    draw(l,a)
dragon(8, 5, 90)
