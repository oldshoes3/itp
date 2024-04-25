# Chessboard

Write a .js program that uses console.log to print a chess board grid (width =
height) where the value in a definition of a binding called "size"
changes the width and height of the grid. E.G. size = 8 will print out:

<pre>
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # # </pre>



## 1st attempt
- If the size is an even number, the 1st row will have (size/2) pairs of ' ' and '#'.
- If the size is an odd number, the 1st row will have (size/2) pairs of '#' and ' ', and there is additional ' ' at the end.
- so I wrote:

<pre>
(size % 2 == 0) ? ' #'.repeat(size/2) : ' #'.repeat(size/2).concat(' ')
</pre>

- Later while I am writing this documentation file, I found if the size is odd number, the repeatetion should be size/2 but rounded off, but it seems Javascript automatically round off when the .repeat() method have a float value.

- When the size is an even number, the 1st, 3rd, 5th, ... will have size/2 times of ' #',
- while the 2nd, 4th, 6th, ... will have size/2 times of '# '.

<pre>
for (var i = 1; i <= size; i ++) {
  console.log((i % 2 == 0) ? '# '.repeat(size/2) : ' #'.repeat(size/2));
}
</pre>

- Then, I though I had to have if statement above the code.
  - if (size % 2 == 0), execute the code
  - else, I had to a new similar code with additional .concat() method.
- The result will be a code with one 'if' that includes one 'for loop' that includes another 'if'. I think it could be a little dirty?

## 2nd attempt
- Let's think like a cartesian coordinate system,
  - let's say the top, left corner is (1, 1)
- (1, 1) is always ' '.
- (1, 2) is always '#', (1, 3) is always ' ', (1, 4) is always '#', ...
- (2, 1) is always '#', (2, 2) is always ' ' , ...
- If x and y are both even number or both odd number, it's ' '.
- If one of x and y is even number and the other is odd number, it's '#'.
- Then I can have 2 for loops, and 1 if statement that divides whether x, y are both odd-or-even or not
- I though what I could write for if statement, and found when two numbers are both even, or both odd, the sum of two is always even, while if one of two are even and the other is odd, the sum is always odd.
- So I wrote:
<pre>
for (var i = 1; i <= size; i ++) {
    for (var j = 1; j <= size; j ++) {
      ((i + j) % 2 == 0) ? console.log(' ') : console.log('#')
    console.log('\n')}
}
</pre>

- The result has much much empty spaces.
- It turns out console.log always break line at the end. I searched if I can make console.log without line break, and found process.stdout.write, so I replaced all console.log to process.stdout.write, but it didn't work. It turns out process.stdout.write does not work in a browser setting. It seems there is no way.
- So I make a new variable called result with empty string, and every time ' ' or '#' should be added,  it will be appended in result.
<pre>
var result = '';
for (let i = 1; i <= size; i ++) {
    for (let j = 1; j <= size; j ++) {
        ((i + j) % 2 == 0) ? result = result.concat(' ') : result = result.concat('#');
    }
    result = result.concat('\n');
}
console.log(result);
</pre>

- Now the code is 8 lines. I went back to my 1st attempt and finished it. It also works. It is 9 lines, but it doesn't have additional variable like 'result' in the 2nd attempt.

- Later in 2nd attempt, I shorten ? statement.