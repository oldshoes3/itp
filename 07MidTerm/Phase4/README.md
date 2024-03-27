# Midterm Project - Phase 4: Tiling

- I set the canvas size to 720 x 720 to be able to utilize 720s device?
- First, I attempted to tile 5 obejcts only at the uppermost row. The x coordinate of origin point would be 0, 720 * 1/5, 720 * 2/5, 720 * 3/5, 720 * 4/5. The size of each object would be 720 / 5, and because of orginal size of the object is 150, the s is like:
<pre>
150 * s = 720 / 5
s = 720 / 5 / 150
</pre>

- So I wrote the following code but it didn't work:
<pre>
def draw():
    noLoop()
    drawObject(0, 0, 720 / 5 / 150, random(255), random(255), random(255))
    drawObject(720 * 1/5, 0, 720 / 5 / 150, random(255), random(255), random(255))
    drawObject(720 * 2/5, 0, 720 / 5 / 150, random(255), random(255), random(255))
    drawObject(720 * 3/5, 0, 720 / 5 / 150, random(255), random(255), random(255))
    drawObject(720 * 4/5, 0, 720 / 5 / 150, random(255), random(255), random(255))
</pre>

- I calculated 720 / 5 / 150 = 0.96, and inserted 0.96 instead of 720 / 5 / 150, and now it worked.

- I found that if I input 720.0 / 5 / 150, it worked. It seems scale() function has an issue when dealing with floats/intergers in division?

- If the tiled objects are 3 in one row, s would be 720.0/3/150; if 4, s would be 720.0/s/150; so n objects, s would be 720.0/n/150.


- loop:
<pre>
def draw():
    noLoop()
    for i in range(5):
        drawObject(720 * i / 5, 0, 720.0 / 5 / 150, random(255), random(255), random(255))
</pre>

- Now the y coordinates: 0, 720*1/5, 720*2/5, 720*3/5, 720*4/5.
<pre>
def draw():
    noLoop()
    for i in range(5):
        drawObject(720 * i / 5, 0, 720.0 / 5 / 150, random(255), random(255), random(255))
    for i in range(5):
        drawObject(720 * i / 5, 720 * 1/5, 720.0 / 5 / 150, random(255), random(255), random(255))
    for i in range(5):
        drawObject(720 * i / 5, 720 * 2/5, 720.0 / 5 / 150, random(255), random(255), random(255))
    for i in range(5):
        drawObject(720 * i / 5, 720 * 3/5, 720.0 / 5 / 150, random(255), random(255), random(255))
    for i in range(5):
        drawObject(720 * i / 5, 720 * 4/5, 720.0 / 5 / 150, random(255), random(255), random(255))
</pre>

- and to make a loop:
<pre>
def draw():
    noLoop()
    for i in range(5):
        for j in range(5):
            drawObject(720 * i / 5, 720 * j / 5, 720.0 / 5 / 150, random(255), random(255), random(255))
</pre>

- Now instead of 5, make variable n.
    - I tried input() function so the user can input how many n*n tiling, but it seemed processing does not support input fuction. [look at the first answer of this post](https://forum.processing.org/two/discussion/23646/how-to-use-input-with-python-processing-running-on-a-mac.html)
        - I also copied and pasted the code in the second answer in the link but it didn't work.

- What if n is float???
    - All the x, y coordinate and s should be calculated from n, but tiling will be m*m, where m is the rounded-up interger of n.
    - The result will be that the last object of each row and objects at the last row will patially drawn.
<pre>
def draw():
    noLoop()
    n = 3.14
    if type(n) is float:
        m = int(n) + 1
    else:
        m = n
    for i in range(m):
        for j in range(m):
            drawObject(720.0 * i / n, 720.0 * j / n, 720.0 / n / 150, random(255), random(255), random(255))
</pre>

- maximizing?
    - I can't 100% get it what the instruction about maximizing the objects means,
    - but when looking at the two 8th-note sample objects, the objects has a margin in the phase 2 and 3 but the margin is gone when tiled in phase 4.
    - My original object has 10-size margin in each side, so:
        - the actual size is 130*130: s should be 720.0 / n / 130
        - The origin point of my original object should be shift to (10, 10)
            - I can't find how to do
                - maybe just shift all x,y cordinates inside the original object's code.

- One last thing, remove noLoop() and change framerate() so objects' colors change