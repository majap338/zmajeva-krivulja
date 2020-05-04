import turtle
francek=turtle.Turtle()
francek.color("purple")
francek.speed("fastest")
list0=[1]
list1=[]
a=0
x=0
b=0
while True:
    if list0[x]==1:
        francek.right(90)
    else:
        francek.left(90)
    francek.forward(5)
    if x+1==len(list0):
        list1=[1]+list0
        list0.extend(list1)
        b=2**a*3-1
        if list0[b]==0:
            list0[b]=1
        else:
            list0[b]=0
        a+=1
    x+=1
