def setup():
    size(150, 150) # canvas size
    background(0) # background will be black

    
def draw():
    fill(255) # fill shapes with white
    noStroke() # no boundaries of shapes
    arc(75, 70, 135, 120, 0.65 * PI, 2.35 * PI, OPEN) # head
    quad(35, 99, 31, 135, 50, 140, 55, 100) # left-most tooth
    rect(55, 100, 19, 40, 0, 0, 5.2, 5.2) # second left tooth
    rect(76, 100, 19, 40, 0, 0, 5.2, 5.2) # second right tooth
    quad(95, 100, 100, 140, 119, 135, 114, 99) # right-most tooth
#    fill(0) # fill following shapes with black
#    circle(50, 60, 30) # left eye
#    circle(100, 60, 30) # right eye
#    triangle(75, 75, 65, 102, 85, 102) # nose
    save("head_and_teeth5.png")
