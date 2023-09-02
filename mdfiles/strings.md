
---

# String Methods

In JavaScript, strings are one of the fundamental data types used to store and manipulate text. Strings come with a variety of built-in methods that allow you to perform various operations on strings. In this tutorial, we'll explore some of the most commonly used string methods along with examples.

## 1. `length`

The `length` property returns the number of characters in a string.

[copy code](www.code1.com)
```javascript
const message = "Hello, world!";
const length = message.length; // 13
```

## 2. `charAt` and `charCodeAt`

`charAt(index)` returns the character at the specified index. `charCodeAt(index)` returns the Unicode value of the character at the specified index.

[copy code](www.code2.com)
```javascript
const str = "JavaScript";
const char = str.charAt(4); // S
const charCode = str.charCodeAt(4); // 83
```

## 3. `concat`

The `concat` method combines two or more strings.

[copy code](www.code3.com)
```javascript
const firstName = "John";
const lastName = "Doe";
const fullName = firstName.concat(" ", lastName); // John Doe
```

## 4. `indexOf` and `lastIndexOf`

`indexOf(substring)` returns the index of the first occurrence of the substring. `lastIndexOf(substring)` returns the index of the last occurrence of the substring.

[copy code](www.code4.com)
```javascript
const sentence = "JavaScript is fun and JavaScript is versatile.";
const firstIndex = sentence.indexOf("JavaScript"); // 0
const lastIndex = sentence.lastIndexOf("JavaScript"); // 23
```

## 5. `toUpperCase` and `toLowerCase`

These methods change the case of the string to uppercase or lowercase.

[copy code](www.code5.com)
```javascript
const message = "Hello, world!";
const upperCaseMessage = message.toUpperCase(); // HELLO, WORLD!
const lowerCaseMessage = message.toLowerCase(); // hello, world!
```

## 6. `trim`

`trim()` removes whitespace from both the beginning and end of a string.

[copy code](www.code6.com)
```javascript
const input = "   JavaScript is awesome!   ";
const trimmedInput = input.trim(); // JavaScript is awesome!
```

## 7. `split`

`split(delimiter)` splits a string into an array of substrings based on a delimiter.

[copy code](www.code7.com)
```javascript
const fruits = "apple,banana,orange";
const fruitArray = fruits.split(","); // ["apple", "banana", "orange"]
```

## 8. `replace`

`replace(oldValue, newValue)` replaces occurrences of a substring with a new substring.

[copy code](www.code8.com)
```javascript
const sentence = "I like cats and dogs.";
const newSentence = sentence.replace("cats", "birds"); // I like birds and dogs.
```

## 9. `startsWith` and `endsWith`

`startsWith(prefix)` checks if a string starts with the specified prefix. `endsWith(suffix)` checks if a string ends with the specified suffix.

[copy code](www.code9.com)
```javascript
const text = "Hello, world!";
const startsWithHello = text.startsWith("Hello"); // true
const endsWithWorld = text.endsWith("world!"); // true
```

## 10. `substr` and `substring`

`substr(startIndex, length)` returns a portion of the string from the specified index with the given length. `substring(startIndex, endIndex)` returns a portion of the string between the specified start and end indices.

[copy code](www.code10.com)
```javascript
const str = "JavaScript is amazing!";
const portion1 = str.substr(4, 10); // Script is
const portion2 = str.substring(4, 14); // Script is a
```

## Conclusion

JavaScript provides a variety of powerful string methods for manipulating text. By understanding and utilizing these methods, you can efficiently work with strings and create more dynamic and feature-rich applications.

---

This tutorial has introduced you to some of the commonly used string methods in JavaScript. By practicing the concepts covered here, you'll be well-equipped to handle and manipulate strings effectively in your programming endeavors.