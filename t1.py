from turtle import *
import math
import time
t=Turtle()
def dda(x1,y1,x2,y2):
	m=(y2-y1)/(x2-x1)
	penup()
	t.goto(x1,y1)
	for i in range(x1,x2+1):
		if m<=1:
			y1=y1+m
			z=round(y1)
			t.goto(i,z)
			t.pendown()
		else:
			i=i+1/m
			d=round(i)
			t.goto(i,d)
			t.pendown()
dda(80,100,5,6)
Screen().exitonclick()