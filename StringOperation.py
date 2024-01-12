# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation:", result)

# String Length
text = "Python is awesome!"
length = len(text)
print("Length:", length)

# String Slicing
text = "Python Programming"
sliced_text = text[0:6]  # Extracts characters from index 0 to 5
print("Sliced Text:", sliced_text)

# String Formatting
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print("Formatted String:", formatted_string)

# String Methods
text = "   Python Programming   "
stripped_text = text.strip()  # Removes leading and trailing whitespaces
print("Stripped Text:", stripped_text)

uppercase_text = text.upper()
print("Uppercase Text:", uppercase_text)

lowercase_text = text.lower()
print("Lowercase Text:", lowercase_text)

# String Search
text = "Python is powerful"
if "power" in text:
    print("Substring found!")

# String Replace
sentence = "I like Java"
new_sentence = sentence.replace("Java", "Python")
print("Replaced Sentence:", new_sentence)

# String Splitting
sentence = "Python is easy to learn"
words = sentence.split()
print("Split Words:", words)

# String Join
words = ["Python", "is", "fun"]
joined_sentence = " ".join(words)
print("Joined Sentence:", joined_sentence)
