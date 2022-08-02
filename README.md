# Palindrone
In this code challenge we check if a string entered by the user is a palindrome.

![GitHub followers](https://img.shields.io/github/followers/hrszpuk?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/hrszpuk?style=social)
<br>
![GitHub language count](https://img.shields.io/github/languages/count/CodingChallengesBooklet/Palindrone?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CodingChallengesBooklet/Palindrone?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/CodingChallengesBooklet/Palindrone?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/CodingChallengesBooklet/Palindrone?style=for-the-badge)
![GitHub branch checks state](https://img.shields.io/github/checks-status/CodingChallengesBooklet/Palindrone/main?style=for-the-badge)

## Problem
Write a program that checks if a string entered by the user is a palindrome. 
A palindrome is a word that reads the same forwards as backwards like “racecar" or "hannah".

## Solution
A palindrome program is one of the easiest programs to write!
In some programming languages reversing text is done in different ways, so in the code below we simply reverse it using the `REVERSE` keywords.

First, we get the user input, and then reverse the text and store the result in a new variable `reversed_text`.
```python
text = INPUT
reversed_text = REVERSE text
```
After that, we check if the text entered is the same as the reversed text.
```python
IF text = reversed_text THEN
    OUTPUT "The text you entered is a palindrome!"
ELSE 
    OTUPUT "The text you entered is NOT a palindrome!"
```
