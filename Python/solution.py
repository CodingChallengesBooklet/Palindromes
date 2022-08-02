
# Get text and reverse it
text = input("Enter the text you think could be a palindrome: ")
reversed_text = text[::-1]

# Check if palindrome and tell the user
if text == reversed_text:
    print(f"The text \"{text}\" is a palindrome!")
else:
    print(f"The text \"{text}\" is NOT a palindrome!")

