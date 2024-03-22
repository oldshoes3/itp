def setup():
    size(150, 150)
    background(0)

    
def draw():
    fill(255)
    noStroke()
    arc(75, 70, 140, 120, 0.7 * PI, 2.3 * PI, OPEN)
#    line(33, 119, 33, 140)
#    line(117, 119, 117, 140)
#    line(33, 140, 117, 140)
    rect(33, 119, 84, 21)
    stroke(255)
    line(75, 122, 75, 140)
