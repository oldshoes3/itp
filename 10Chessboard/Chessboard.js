size = 7

// 2nd attempt

var result = '';
for (let i = 1; i <= size; i ++) {
    for (let j = 1; j <= size; j ++) {
        result = ((i + j) % 2 == 0) ? result.concat(' ') : result.concat('#');
    }
    result = result.concat('\n');
}
console.log(result);


// 1st attempt
/*
if (size % 2 == 0) {
    for (var i = 1; i <= size; i ++) {
        console.log((i % 2 == 0) ? '# '.repeat(size/2) : ' #'.repeat(size/2));
    }
} else {
    for (var i = 1; i <= size; i ++) {
        console.log((i % 2 == 0) ? '# '.repeat(size/2).concat('#') : ' #'.repeat(size/2).concat(' '));
    }
}
*/