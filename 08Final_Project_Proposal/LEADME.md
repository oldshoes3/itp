# Yuseok's final project proposal

## What will (likely) be the title of your project?

Simple sheet music maker

## In just a sentence or two, summarize your project. (E.g., "My project a web-based synthesizer.")

My project will be a web application that make simple sheet music.

## List at least 3 resources you know you will use in developing your project

Javascript
music font, probably [bravura](https://github.com/steinbergmedia/bravura/releases), an OpenType music font for Dorico
[staff.js](https://github.com/instrumentbible/staff.js) for reference?

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

The webpage screen divides into two sections. The left section of the screen has buttons with notes (whole, half, quater, 8th, ... notes and rests) and text input field where the a user will write notes or midinotes. The right section shows a 5-line staff. For example, when a user types 'c4' in the text field and press a quater note button, a quater note of middle C appears on the staff. There will be dropdown menus to determine the time signature and key signature as well. There will be a console window that shows what notes the user inputs so far; for example, if the user input two quarter notes (C5 B4 each) followed by four 8th notes (B-flat4, B4, B-flat4, A4), the console window shows something like "c5/q b4/q bb4/8 b4/8 bb4/8 a4/8", and the user can modify it. 

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

a sheet with 1-4 measure melody within 1 system.
4/4 time signature, no key signature
all notes shorter than 8th note will be rendered with flags.
use treble clef only

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

A sheet with 1 or more systems. Each system has 1-4 measures.
several time signatures and key signatures.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

dynamic, tempo indication
chord symbol
chords instead of only one note at a time
transpose option: If user make 16-measure melody and push a transpose button, everything automatically gets transposed.
8th, 16th, 32nd, ... will be beamed together.
clef change option

## In a paragraph or more, outline your next steps WITH A SPECIFIC CALENDAR. What new skills will you need to acquire? What topics will you need to research?

April 15-21
learn javascript

April 22-28
figure out how to render symbols: bravura is a SMuFL what is SMuFL? How I can position each glyph?
analyze staff.js: can modify css file and use it?
try to make one note
note spacing...

April 29 - May 5
note spacing...
try to make a few bars

May 6-9
time signatures other than 4/4
key signatures other than C maj/A min
try to apply features in BEST outcome section above one by one