Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> 
>>> tur = turtle.Turtle()
>>> tur.speed(20)
>>> tur.color("black","orange")
>>> tur.begin_fill()
>>> 
>>> for i in range(50):
...     tur.forward(300)
...     tur.left(170)
... 
...     
tu
>>> tur.end_fill()
>>> turtle.done()
