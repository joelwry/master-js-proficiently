
# Operators 
Let's explore arithmetic, assignment, comparison, and logical operators in JavaScript with examples in this section.

**1) Arithmetic Operators:**
Arithmetic operators perform mathematical operations on numbers. Here are some commonly used arithmetic operators:

- Addition (`+`): Adds two numbers together.

[copy code](www.code1.com)
```javascript
var sum = 5 + 3;
console.log(sum); // Output: 8
```

- Subtraction (`-`): Subtracts one number from another.

[copy code](www.code2.com)
```javascript
var difference = 10 - 4;
console.log(difference); // Output: 6
```

- Multiplication (`*`): Multiplies two numbers.

[copy code](www.code3.com)
```javascript
var product = 6 * 2;
console.log(product); // Output: 12
```

- Division (`/`): Divides one number by another.

[copy code](www.code4.com)
```javascript
var quotient = 20 / 5;
console.log(quotient); // Output: 4
```

- Modulo (`%`): Returns the remainder after division.

[copy code](www.code5.com)
```javascript
var remainder = 15 % 7;
console.log(remainder); // Output: 1
```

**2) Assignment Operators:**
Assignment operators are used to assign values to variables. Here are a few examples:

- Assignment (`=`): Assigns a value to a variable.

[copy code](www.code6.com)
```javascript
var x = 10;
console.log(x); // Output: 10
```

- Addition assignment (`+=`): Adds a value to the variable and assigns the result.

[copy code](www.code7.com)
```javascript
var y = 5;
y += 3;
console.log(y); // Output: 8
```

- Subtraction assignment (`-=`): Subtracts a value from the variable and assigns the result.

[copy code](www.code8.com)
```javascript
var z = 10;
z -= 4;
console.log(z); // Output: 6
```

**3) Comparison Operators:**
Comparison operators compare two values and return a boolean (`true` or `false`) based on the comparison result. Here are some commonly used comparison operators:

- Equality (`==`): Checks if two values are equal.

[copy code](www.code9.com)
```javascript
var isEqual = 5 == 5;
console.log(isEqual); // Output: true
```

- Inequality (`!=`): Checks if two values are not equal.

[copy code](www.code10.com)
```javascript
var isNotEqual = 5 != 3;
console.log(isNotEqual); // Output: true
```

- Greater than (`>`), less than (`<`), greater than or equal to (`>=`), less than or equal to (`<=`): Compare the values of two numbers.

[copy code](www.code11.com)
```javascript
var isGreater = 8 > 5;
console.log(isGreater); // Output: true

var isLess = 3 < 10;
console.log(isLess); // Output: true

var isGreaterOrEqual = 5 >= 5;
console.log(isGreaterOrEqual); // Output: true

var isLessOrEqual = 3 <= 3;
console.log(isLessOrEqual); // Output: true
```

**4) Logical Operators:**
Logical operators are used to combine or manipulate boolean values. Here are the three main logical operators:

- AND (`&&`): Returns `true` if both operands are `true`.

[copy code](www.code12.com)
```javascript
var isTrue = true && false;
console.log(isTrue); // Output: false
```

- OR (`||`): Returns `true` if at least one of the operands is `true`.

[copy code](www.code13.com)
```javascript
var isTrue = true || false;
console.log(isTrue); // Output: true
```

- NOT (`!`): Negates a boolean value.

[copy code](www.code14.com)
```javascript
var isFalse = !true;
console.log(isFalse); // Output: false
```

**Demonstrating the Use of Operators in Expressions:**
Operators can be used in expressions to perform calculations or comparisons. Here's an example that combines arithmetic and comparison operators:

[copy code](www.code15.com)
```javascript
var x = 5;
var y = 10;
var result = (x * 2) > (y - 5);
console.log(result); // Output: true
```

In this code, we use the arithmetic operators (`*` and `-`) to calculate `x * 2` and `y - 5`. Then we compare the two results using the greater than (`>`) operator. The final result is `true` because `10` is indeed greater than `5`.

