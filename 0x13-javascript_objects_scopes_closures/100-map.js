#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((list, index) => list * index);
console.log(list);
console.log(newList);
