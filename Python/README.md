# Palindrones
In this code challenge we check if a string entered by the user is a palindrome.

## Problem
Write a program that checks if a string entered by the user is a palindrome. 
A palindrome is a word that reads the same forwards as backwards such as “racecar" or "hannah".

## Solution
A palindrome program is one of the easiest programs to write!
In Python, reversing a string can be done using [slices](https://stackoverflow.com/questions/509211/understanding-slicing),
we can use `text[::-1]` to flip the string around.
This works because slices are separated into `[start:stop:step]`, in this case, we put nothing for start and stop but for
step we put `-1` which means Python will read the string from back to front.

Read more
- [The GOTO stack overflow post to understand slices](https://stackoverflow.com/questions/509211/understanding-slicing)
- [Programiz article](https://www.programiz.com/python-programming/methods/built-in/slice)

### Solution in Python
To get started, we take the user input, which is the text we are going to check.
Next, we reverse the text using `[::-1]` slice syntax.
```python
# Get text and reverse it
text = input("Enter the text you think could be a palindrome: ")
reversed_text = text[::-1]
```
Now, we check if the original text, and the reversed text is the same.
We then tell the user.
```python
# Check if palindrome and tell the user
if text == reversed_text:
    print(f"The text \"{text}\" is a palindrome!")
else:
    print(f"The text \"{text}\" is NOT a palindrome!")
```

### Solution in a single line
Python is a perfect language for compacting code.
It can do this extremely well, and to showcase this, I've written this simple program as a single line.
```python
print(f"Palindrome: {True if (lambda x: x == x[::-1])(input('Text: ')) else False}")
```