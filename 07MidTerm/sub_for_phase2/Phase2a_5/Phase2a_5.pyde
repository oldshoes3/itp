def setup():
    size(150, 150)
    background(0)

def draw():
    fill(255)
    noStroke()
    arc(75, 70, 130, 110, 0.65 * PI, 2.35 * PI, CHORD)
    quad(35.5, 99, 32.5, 138, 51.5, 140, 54.5, 100)
    rect(56, 110, 18, 30, 0, 0, 5.2, 5.2)
    rect(76, 110, 18, 30, 0, 0, 5.2, 5.2)
    quad(95.5, 100, 98.5, 140, 117.5, 138, 114.5, 99)

    save("head_and_teeth5.png")
