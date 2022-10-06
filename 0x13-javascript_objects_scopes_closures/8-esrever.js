#!/usr/bin/node

exports.esrever = function (list) {
  const myList = [];
  const len = list.length - 1;
  for (let i = len; i !== -1; i--) myList.push(list[i]);
  return (myList);
};
