
# Loops (for and while)

Loops are essential programming constructs that allow you to repeat a certain block of code multiple times. They are especially useful when you need to perform the same task multiple times or iterate over data structures.

## Introduction to Loops

Loops help automate repetitive tasks, making your code more efficient and compact. In this lesson, we'll cover two types of loops: `for` and `while`.

## Syntax and Usage of for Loops

The `for` loop allows you to specify the number of iterations and control how the loop variable changes each time.

[copy code](www.code1.com)
```javascript
for (initialization; condition; increment/decrement) {
  // Code to be executed in each iteration
}
```

Here's an example that prints numbers from 1 to 5:

[copy code](www.code2.com)
```javascript
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

## Syntax and Usage of while Loops

The `while` loop repeats a block of code as long as a certain condition is `true`.

[copy code](www.code3.com)
```javascript
while (condition) {
  // Code to be executed in each iteration
}
```

Here's an example that prints numbers from 1 to 5 using a `while` loop:

[copy code](www.code4.com)
```javascript
let i = 1;
while (i <= 5) {
  console.log(i);
  i++;
}
```

## Using Loops to Iterate Over Arrays

Loops are commonly used to iterate over arrays and perform operations on each element.

### Example: Sum of Numbers in an Array

[copy code](www.code5.com)
```javascript
let numbers = [1, 2, 3, 4, 5];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
  sum += numbers[i];
}

console.log(sum); // Output: 15
```

## Practice Exercises

1. Write a `for` loop to print all even numbers from 2 to 10.
2. Write a `while` loop to calculate the factorial of a given number.
3. Write a program that uses a loop to find the maximum value in an array of numbers.

---

