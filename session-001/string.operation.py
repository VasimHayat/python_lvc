# Using capitalize() to capitalize the first letter of a string
name = "john doe"
capitalized_name = name.capitalize()
print(capitalized_name) # Output: "John doe"

# Using lower() to convert all characters in a string to lowercase
message = "Hello, World!"
lowercase_message = message.lower()
print(lowercase_message) # Output: "hello, world!"

# Using upper() to convert all characters in a string to uppercase
name = "John Doe"
uppercase_name = name.upper()
print(uppercase_name) # Output: "JOHN DOE"

# Using replace() to replace a substring in a string with another substring
message = "Hello, World!"
new_message = message.replace("World", "Python")
print(new_message) # Output: "Hello, Python!"

# Using split() to split a string into a list of substrings based on a delimiter
sentence = "This is a sentence."
words = sentence.split(" ")
print(words) # Output: ["This", "is", "a", "sentence."]

# Using join() to join a list of strings into a single string using a delimiter
words = ["This", "is", "a", "sentence."]
sentence = " ".join(words)
print(sentence) # Output: "This is a sentence."

# Using strip() to remove leading and trailing whitespace from a string
text = "  This is some text.  "
stripped_text = text.strip()
print(stripped_text) # Output: "This is some text."

# Using startswith() to check if a string starts with a specified substring
name = "John Doe"
starts_with_j = name.startswith("J")
print(starts_with_j) # Output: True

# Using endswith() to check if a string ends with a specified substring
name = "John Doe"
ends_with_e = name.endswith("e")
print(ends_with_e) # Output: True

# Using find() to find the index of a specified substring in a string
message = "Hello, World!"
index_of_comma = message.find(",")
print(index_of_comma) # Output: 5

# Using count() to count the number of times a specified substring appears in a string
message = "Hello, World!"
count_of_l = message.count("l")
print(count_of_l) # Output:


def swap(str1:str,str2:str):
    # temp=str1
    # str1=str2
    # str2=temp
    # print(str1,str2)
    str1,str2 = str2,str1
    print(str1,str2)

swap('hi','jack')

string = "Hello"
repeated_string = string * 3
print(repeated_string) # Output: "HelloHelloHello"