# Example 1

from functools import reduce

# Example 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
total = reduce(lambda x, y: x + y, numbers)
sumVal = sum(numbers,0)
print(total,sumVal)

# Example 2

greet = lambda name,address:print(f" {name} live in {address}")

greet('Martin','London')