def setup():
    size(150, 150)
    background(0)

def draw():
    fill(255)
    noStroke()
    arc(75, 65, 130, 110, 0.65 * PI, 2.35 * PI, CHORD)
    for i in range(4):
        pushMatrix()
        translate(i * 20 + 45, 125)
        rotate(i * -0.1 + 0.15)
        rect(-9, -15, 18, 30, 0, 0, 5.2, 5.20)
        popMatrix()

    save("head_and_teeth6.png")
