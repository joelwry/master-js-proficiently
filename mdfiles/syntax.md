# Syntax & Structure

## JavaScript Language syntax and basic structure:

JavaScript code is written in plain text and can be embedded directly in HTML documents or stored in external .js files. We typically use the script tag to include JavaScript in HTML files. Let us start with a basic structure example

[copy code](www.code1.com)
```html
<!DOCTYPE html>
<html>
	<head>
	  <title>JavaScript Syntax Example</title>
	</head>
	<body>
	  <h1>Hello, JavaScript!</h1>

	  <script>
	    // JavaScript code goes here
	  </script>
	</body>
</html>

```

### Comments 
Comments are ignored by the javascript interpreter. They can be used to document on a partcular code written down. Comments are of two type in javascript.
Single line comment and the multiple type comment. 
The single line comment is meant for a single line while the multiple line comment allow one extend more than one line 

[copy code](www.code2.com)
```javascript
 // This is a single line comment
 /**
	This is a muiltiple line comment.
	This is particularly useful for documenting what a code block does for ease
	of remembrance, reuseability, passing the right arguments to a function
 **/	

```

### Variables and their purpose:

Variables are used to store and manipulate data in JavaScript. They act as containers that hold values. In javascript we can declare a variable using let, var and const keyword. 
To declare a variable, we use any of those keyword followed by the variable name. We can then assign a value to the variable using the assignment operator (=)
Let's declare a variable called message and assign it a string value:

[copy code](www.code3.com);
```javascript
  let message = "Hello, World!";
  console.log(message);

  const country = "USA";
  console.log(country);

  var point = 234;
```
In the code above, we declared a variable named message using the var keyword. The value assigned to the variable is the string "Hello, World!". We then use console.log() to output the value of the variable to the browser console.

##### N.b
Variables declared with const can not be reassigned values, hence it means constant value that should not change. var is the oldest way to declare variables in JavaScript. Variables declared with var have function scope or global scope. let is a relatively new way to declare variables introduced in the ECMAScript 6 (ES6) specification. Variables declared with let have block scope, which means they are only accessible within the block where they are defined. let and const are the relatively preferred way of declaring variables in this era of javascript


###  Variable declaration and assignment:

. Here's an example:

### Data types:

JavaScript has several built-in data types. Some of the most common ones are:

* Strings: Used to represent text and are enclosed in single or double quotes. Example:

[copy code](www.code4.com)
```javascript
var name = "John";
console.log(name);
```

* Numbers: Used to represent numeric values. 

[copy code](www.code5.com)
```javascript
var age = 23;
let point = 45.78
console.log(age, point);
```

* Booleans: Represent either true or false.

[copy code](www.code6.com) 
```javascript
var isPresent = true;
 console.log(isPresent);
```

* Null : Represent a null value hence no manipulation can be done on this type of data type. 

[copy code](www.code7.com)
```javascript
var empty = null;
 console.log(empty);
```
<br>

* Undefined : This type helps to denote that a variable has either not been initialized with a value or the variable the user is trying to access has not been declared and defined.

[copy code](www.code8.com) 
```javascript
let task;
console.log(task);
let result = undefined
console.log(result)
```


### Type of Data Stored 
For us to know the type of data that is been stored in a variable, we use the typeof keyword. This is called as a function and the variable to check it type is passed into it open and close bracket

[copy code](www.code9.com)
```javascript
console.log(typeof(age)) // number
console.log(typeof(isPresent)) // boolean
console.log(typeof(name)) // string
``` 
