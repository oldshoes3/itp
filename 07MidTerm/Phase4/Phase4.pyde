def setup():
    frameRate(30)
    size(720, 720)
    background(0)
    
def drawObject(x, y, s, r, g, b):
    push()
    translate(x, y)
    scale(s)
    fill(r, g, b)
    noStroke()
    arc(75, 70, 130, 110, 0.65 * PI, 2.35 * PI, CHORD)

    for i in range(4):
        pushMatrix()
        translate(i * 20 + 45, 125)
        rotate(i * -0.1 + 0.15)
        rect(-9, -15, 18, 30, 0, 0, 5.2, 5.20)
        popMatrix()

    fill(0) # fill following shapes with black
    circle(50, 70, 20) # left eye
    circle(100, 70, 20) # right eye
    triangle(75, 80, 65, 105, 85, 105) # nose
    pop()
    
    
def draw():
    n = 20
    noLoop()
    for i in range(n):
        for j in range(n):
            drawObject(width * i / n, height * j / n, float(width)/ n / 150, random(255), random(255), random(255))