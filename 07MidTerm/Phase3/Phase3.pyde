def setup():
    frameRate(30)
    size(400, 400)
    background(0)
    
def drawObject(x, y, s, r=255, g=255, b=255):
    push()
    translate(x, y)
    scale(s)
    fill(r, g, b)
    noStroke()
    arc(75, 65, 130, 110, 0.65 * PI, 2.35 * PI, CHORD)

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
    drawObject(0, 0, 1)
    drawObject(150, 30, 0.2, 255, 255, 255)
    drawObject(3, 115, 2, 0, 255, 255)
    noLoop()
    drawObject(350, 200, -0.5, random(255), random(255), random(255))
#    drawObject(mouseX, mouseY, 0.25, random(10, 255), random(10, 255), random(10, 255))
