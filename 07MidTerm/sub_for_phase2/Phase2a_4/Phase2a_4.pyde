def setup():
    size(150, 150)
    background(0)

def draw():
    fill(255)
    noStroke()
    arc(75, 70, 130, 110, 0.65 * PI, 2.35 * PI, CHORD)
    rect(36, 110, 18, 30, 0, 0, 5.2, 5.2)
    rect(56, 110, 18, 30, 0, 0, 5.2, 5.2)
    rect(76, 110, 18, 30, 0, 0, 5.2, 5.2)
    rect(96, 110, 18, 30, 0, 0, 5.2, 5.2)

    save("head_and_teeth4.png")
