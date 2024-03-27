# Midterm Project - Phase 3: Function

- For the phase 3, I just followed the instruction. The canvas size is now bigger. I already knew translate(). scale() was new but I understood everything under scale() would be scaled. Because I already used pushMatrix()and popMatrix() I could guess why the pair of push()/pop() wraps the code: apply translate() and scale() only within each function.

- Between scale(s) and pop() I just pasted the code from phase 2, and it seemed it worked well. I played around parameters of drawObject().

- I added a color parameters, and messed with random() to make each object a random color. The color changes drastically, and I found noLoop() insde draw() function can stop constant drawing.

- I also tried mouseX/mouseY so the object can move. However noLoop() disables the location update. I tried having seperte draw() defination, having background(0) somewhere else than setup, etc but could not figure out how to have the following two objects at the same time: one with fixed random color and the other that follows the mouse point.