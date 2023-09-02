

# Object-Oriented Programming (OOP) in JavaScript
---

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into reusable and self-contained objects. In JavaScript, OOP enables you to model real-world entities and their interactions. Let's explore the key OOP concepts in JavaScript.



## Introduction to Object-Oriented Programming

OOP is centered around objects, which are instances of classes. A class defines the blueprint for creating objects with shared properties and behaviors.

### Classes and Objects

In JavaScript, classes can be created using the `class` keyword. Objects are created from classes using the `new` keyword.

[copy code](www.code1.com)
```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name}.`);
  }
}

const person1 = new Person("Alice", 30);
person1.greet(); // Output: Hello, my name is Alice.
```

## Inheritance

Inheritance allows one class (subclass) to inherit properties and methods from another class (superclass). This promotes code reuse and hierarchy.

[copy code](www.code2.com)
```javascript
class Student extends Person {
  constructor(name, age, grade) {
    super(name, age);
    this.grade = grade;
  }

  study() {
    console.log(`${this.name} is studying.`);
  }
}

const student1 = new Student("Bob", 18, 12);
student1.greet(); // Output: Hello, my name is Bob.
student1.study(); // Output: Bob is studying.
```

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. This simplifies code by enabling uniform handling of different objects.

[copy code](www.code3.com)
```javascript
function introduce(person) {
  person.greet();
}

introduce(person1);   // Output: Hello, my name is Alice.
introduce(student1);  // Output: Hello, my name is Bob.
```

## Static Methods

Static methods are methods defined on a class itself, not on its instances. They are called using the class name, not an object.

[copy code](www.code4.com)
```javascript
class MathUtil {
  static square(x) {
    return x * x;
  }
}

const result = MathUtil.square(5); // result = 25
```

## Abstraction

Abstraction is the process of hiding complex implementation details and showing only essential features of an object. It helps reduce complexity and improve maintainability.

## Encapsulation

Encapsulation involves bundling data (properties) and methods (functions) that operate on the data into a single unit, called a class. It prevents direct access to internal data from outside the class.

[copy code](www.code5.com)
```javascript
class BankAccount {
  constructor(balance) {
    this.balance = balance;
  }

  deposit(amount) {
    this.balance += amount;
  }

  withdraw(amount) {
    if (amount <= this.balance) {
      this.balance -= amount;
    } else {
      console.log("Insufficient balance.");
    }
  }

  getBalance() {
    return this.balance;
  }
}
```

## Conclusion

Object-Oriented Programming is a powerful paradigm that enhances code organization, reusability, and maintainability. By understanding and applying concepts like classes, inheritance, polymorphism, static methods, abstraction, and encapsulation, you can build well-structured and modular applications in JavaScript.

---

This tutorial has provided you with a comprehensive understanding of Object-Oriented Programming and its core concepts in JavaScript. By practicing these concepts, you can design and implement more robust and flexible software solutions.

