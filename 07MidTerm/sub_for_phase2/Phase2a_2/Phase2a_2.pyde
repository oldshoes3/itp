def setup():
    size(150, 150)
    background(0)

def draw():
    fill(255)
    noStroke()
    ellipse(75, 70, 130, 110)
    rect(35, 110, 80, 30) # long rectangle
    stroke(0) # to make following lines black
    strokeWeight(2)
    line(54, 123, 54, 140) # line 1
    line(75, 123, 75, 140) # line 2
    line(96, 123, 96, 140) # line 3
    save("head_and_teeth2.png")
