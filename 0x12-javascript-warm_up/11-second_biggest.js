#!/usr/bin/node

function max (array) {
  let max_int = array[0];
  for (let i = 0; array[i] != null; i++) {
    if (array[i] > max_int) {
	    max_int = i;
    } else {
    return (i);
    }
  }
}

let myarray = [];
if (process.argv.length <= 3) {
	console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    myarray.push(Number(process.argv[i]));
  }
}
const max_int = max(myarray);
console.log(myarray[max_int])
myarray.pop(max_int);
const max_int2 = max(myarray);
console.log(myarray[max_int2]);

