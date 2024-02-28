# 01 Madlibs Game

### String Concatenation
String concatenation refers to the process of combining multiple strings into a single string. In Python, this can be done using various methods, one of which is using f-strings. 

- **F-strings**: F-strings are a convenient and efficient way to format strings in Python. They allow you to embed expressions inside string literals by prefixing the string with 'f' or 'F' and placing the expressions inside curly braces {}. This allows for easy interpolation of variables and expressions within strings.

Example:
```python
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)
```
Output:
```
My name is Alice and I am 30 years old.
```

### Input Function
The input function in Python is used to prompt the user to enter a value from the keyboard. It reads input from the user as a string. 

- **Syntax**: `input(prompt)`, where `prompt` is the message displayed to the user.

Example:
```python
name = input("Enter your name: ")
print("Hello,", name)
```
Output:
```
Enter your name: Alice
Hello, Alice
```

## Implementation in Madlibs Project
In this Madlibs project, string concatenation using f-strings will be utilized to dynamically generate a story based on user input. The input function will prompt the user to enter various words and phrases (e.g., person's name, age, nouns, verbs, adjectives, places, etc.), which will then be incorporated into the Madlib story using string concatenation with f-strings.

Example:
```python
persons_name = input("Person's name: ")
age = input("Age: ")
noun = input("Noun: ")
number = input("Number: ")
verb = input("Verb: ")
...
madlib = f'When {persons_name} was {age}, her parents told her \
they were going on a trip to China. They told her to pack her {noun}. \
The plane ride was {number} hours long! She {verb} and {verb2}. \
...
```

This approach allows for dynamic and personalized storytelling by substituting user-provided inputs into predefined placeholders within the Madlib template.

---
<p align="right">Completed: ２０２４年０２月２８日（水）</p>