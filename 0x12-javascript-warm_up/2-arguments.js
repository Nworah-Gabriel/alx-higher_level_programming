#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Found argument');
} else if (process.argv.length > 3) {
  console.log('Found argumts');
}
