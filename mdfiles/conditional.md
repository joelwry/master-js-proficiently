
---

# Conditional Statements (if...else)

Conditional statements are fundamental concepts in programming that allow your code to make decisions and execute different blocks of code based on conditions. One of the most commonly used conditional statements is the `if...else` statement.

## Concept of Conditional Statements

Conditional statements enable your program to choose between different paths of execution depending on the conditions met. They replicate how we make decisions in everyday life: "If it's raining, take an umbrella; otherwise, just go out."

## Syntax and Usage of if...else Statements

The basic syntax of an `if...else` statement in JavaScript is as follows:

[copy code](www.code1.com)
```javascript
if (condition) {
  // Code to be executed if the condition is true
} else {
  // Code to be executed if the condition is false
}
```

Here's how it works:

- The `condition` is a Boolean expression that evaluates to either `true` or `false`.
- If the `condition` is `true`, the code within the first block will be executed.
- If the `condition` is `false`, the code within the second block (the `else` block) will be executed.

## Common Use Cases and Examples

### Example 1: Voting Eligibility

[copy code](www.code2.com)
```javascript
let age = 17;

if (age >= 18) {
  console.log("You are eligible to vote.");
} else {
  console.log("Sorry, you are not eligible to vote yet.");
}
```

### Example 2: Temperature Interpretation

[copy code](www.code3.com)
```javascript
let temperature = 25;

if (temperature > 30) {
  console.log("It's a hot day!");
} else if (temperature < 10) {
  console.log("It's a cold day!");
} else {
  console.log("The weather is moderate.");
}
```

### Example 3: User Authentication

[copy code](www.code4.com)
```javascript
let username = "john";
let password = "secret";

if (username === "john" && password === "secret") {
  console.log("Login successful.");
} else {
  console.log("Login failed. Invalid username or password.");
}
```

## Practice Exercise

Write a program that checks if a given number is even or odd using an `if...else` statement.

---
