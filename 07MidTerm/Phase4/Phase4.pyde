def setup():
    frameRate(3)
    size(720, 720)
    background(0)

def drawObject(x, y, s, r=255, g=255, b=255):
    push()
    translate(x, y)
    scale(s)
    fill(r, g, b)
    noStroke()
    arc(65, 60, 130, 110, 0.65 * PI, 2.35 * PI, CHORD) # shifted -10

    for i in range(4):
        pushMatrix()
        translate(i * 20 + 35, 115) # shifted -10
        rotate(i * -0.1 + 0.15)
        rect(-9, -15, 18, 30, 0, 0, 5.2, 5.20)
        popMatrix()

    fill(0)
    circle(40, 60, 20) # shifted - 10
    circle(90, 60, 20) # shifted - 10
    triangle(65, 70, 55, 95, 75, 95) # shifted - 10
    pop()
 
def draw():
#    noLoop()
    n = 2
    if type(n) is float:
        m = int(n) + 1
    else:
        m = n
    for i in range(m):
        for j in range(m):
            drawObject(720.0 * i / n, 720.0 * j / n, 720.0 / n / 130, random(255), random(255), random(255))
