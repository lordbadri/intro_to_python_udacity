import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    badri = turtle.Turtle()
    badri.shape("turtle")
    badri.speed(20)
    badri.color("yellow")
    for i in range(5):
        for i in range(36):
            draw_square(badri)
            badri.right(10)
        badri.circle(20)
        badri.right(90)
    
    window.exitonclick()

    

draw_art()
