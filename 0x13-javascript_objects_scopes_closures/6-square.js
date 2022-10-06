#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let holder = '';
    for (let i = 0; i < this.width; i++) {
      if (c) {
        holder += c;
      } else {
        holder += 'X';
      }
    }
    for (let i = 0; i < this.height; i++) console.log(holder);
  }
}

module.exports = Square;
