---

# Objects

## Introduction to Objects

In the world of programming, **objects** are a powerful way to represent complex data structures. Unlike arrays, which store collections of elements, objects store data in the form of **key-value pairs**, making them ideal for modeling real-world entities, their attributes, and behaviors. Objects are a fundamental concept in many programming languages, including JavaScript.

## Why Use Objects?

Objects allow you to organize related data and functionality into a single unit. They mimic real-world objects and entities, making it easier to model and manipulate complex systems. Objects are the building blocks of most modern applications and enable you to create organized, modular, and efficient code.

## Object Declaration

In JavaScript, you can create an object using curly braces `{}` and defining its properties and values.

[copy code](www.code1.com)
```javascript
let person = {
  firstName: "John",
  lastName: "Doe",
  age: 30,
  isStudent: false
};
```

## Accessing Object Properties

You can access object properties using dot notation or bracket notation.

[copy code](www.code2.com)
```javascript
console.log(person.firstName); // Output: John
console.log(person["age"]); // Output: 30
```

## Object Methods

In addition to properties, objects can also have **methods** - functions that are associated with the object and can be called to perform specific actions.

[copy code](www.code3.com)
```javascript
let person = {
  firstName: "John",
  lastName: "Doe",
  greet: function() {
    console.log("Hello, I'm " + this.firstName);
  }
};

person.greet(); // Output: Hello, I'm John
```

## Object Manipulation

Objects are mutable, meaning you can modify their properties and methods after they're created.

[copy code](www.code4.com)
```javascript
person.age = 31;
person["isStudent"] = true;
```

## Combining Objects and Arrays

Objects and arrays can be combined to represent more complex data structures.

[copy code](www.code5.com)
```javascript
let student = {
  name: "Alice",
  scores: [85, 92, 78]
};

console.log(student.scores[1]); // Output: 92
```

## Practice Exercises

1. Create an object representing a car with properties for make, model, and year.
2. Add a method to the car object that calculates its age based on the current year.
3. Create an array of objects representing different books with properties for title, author, and year published.
4. Write a function that takes an array of books and returns the titles of books published in a specific year.

## Conclusion

Objects are fundamental to JavaScript and programming in general. They allow you to model and manipulate complex data structures efficiently. By understanding how to declare objects, work with their properties and methods, and combine them with arrays, you'll have a solid foundation for creating organized and dynamic applications.

---

This lesson has introduced you to the concept of objects in JavaScript. By practicing the concepts covered here, you'll be well-equipped to work with objects and create more complex and feature-rich applications.