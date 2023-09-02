
# JavaScript Variables Tutorial

In this tutorial, we will learn about JavaScript variables and explore some methods available for manipulating them. This tutorial is designed for beginners.

## Table of Contents
- [Introduction to Variables](#introduction-to-variables)
- [Manipulating String Variables](#manipulating-string-variables)
- [Manipulating Number Variables](#manipulating-number-variables)
- [Manipulating Boolean Variables](#manipulating-boolean-variables)
- [Conclusion](#conclusion)

## Introduction to Variables

Variables in JavaScript are used to store and manipulate data. They act as containers that hold values. Here's how you can declare and assign a variable:

[copy code](www.code1.com)
```javascript
let x; // Variable declaration
x = 10; // Variable assignment
```

In the above code, we declared a variable named `x` using the `let` keyword and assigned it a value of `10`. Variables can also be declared and assigned in a single line:

[copy code](www.code2.com)
```javascript
let y = 5; // Variable declaration and assignment
```

## Manipulating String Variables

Strings are sequences of characters. JavaScript provides several methods for manipulating string variables. Here are some commonly used methods:

- `length`: Returns the length of a string.

[copy code](www.code3.com)
```javascript
let message = "Hello, World!";
let length = message.length;
```

- `toUpperCase()`: Converts a string to uppercase.

[copy code](www.code4.com)
```javascript
let name = "john";
let uppercaseName = name.toUpperCase();
```

- `toLowerCase()`: Converts a string to lowercase.

[copy code](www.code5.com)
```javascript
let name = "JOHN";
let lowercaseName = name.toLowerCase();
```

- `charAt()`: Returns the character at a specified index.

[copy code](www.code6.com)
```javascript
let message = "Hello";
let character = message.charAt(1);
```

- `substring()`: Extracts a portion of a string based on the specified indices.

[copy code](www.code7.com)
```javascript
let message = "Hello, World!";
let subString = message.substring(7, 12);
```

## Manipulating Number Variables

Numbers are used for numeric operations in JavaScript. Although numbers are primitive, they don't have built-in methods like strings. However, the `Number` object provides some useful methods:

- `toFixed()`: Formats a number with a specified number of decimal places.

[copy code](www.code8.com)
```javascript
let pi = 3.14159;
let formattedPi = pi.toFixed(2);
```

- `toString()`: Converts a number to a string.

[copy code](www.code9.com)
```javascript
let number = 42;
let numberString = number.toString();
```

## Manipulating Boolean Variables

Booleans represent logical values (`true` or `false`). Since booleans are primitive, there are no manipulation methods specific to them. However, logical operators can be used for boolean manipulation.

- `!` (Logical NOT): Negates a boolean value.

[copy code](www.code10.com)
```javascript
let isTrue = true;
let isFalse = !isTrue;
```


- `&&` (Logical AND): Returns `true` if both operands are `true`.

[copy code](www.code11.com)
```javascript
let x = true;
let y = false;
let result = x && y;
```

- `||` (Logical OR): Returns `true` if at least one of the operands is `true`.

[copy code](www.code12.com)
```javascript
let x = true;
let y = false;
let result = x || y;
```

## Conclusion

In this tutorial, we learned about JavaScript variables and their manipulation methods for strings, numbers, and booleans. We explored various methods available for each data type and how to use them in our code. Now you have a good understanding of how to declare, assign, and manipulate variables in JavaScript!
