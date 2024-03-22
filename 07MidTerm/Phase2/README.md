# Midterm Project - Phase 2: Translate to Processing.py Sketch

## canvas setup
The size of the canvas is 150, 150, accordingly from the instruction
<pre>
size(150, 150)
</pre>
Background will be black; the skull will be white
<pre>
background(0)
</pre>

## head and teeth
Head: an ellipse that has slightly longer width, filled with white
<pre>
fill(255)
noStroke()
ellipse(75, 70, 135, 120)
</pre>

Teeth:
- first I tried a long rectangle with three lines that seperate each of teeth
<pre>
rect(33, 119, 84, 21) # long rectangle
stroke(0) # to make following lines black
line(54, 123, 54, 140)
line(75, 123, 75, 140)
line(96, 123, 96, 140)
</pre>
- the result is
![alt text](head_and_teeth1.png)
- I didn't like it. I thickened the lines adding following line:
<pre>
strokeWeight(2)
</pre>
- the result is
![alt text](head_and_teeth2.png)



<pre>

</pre>
