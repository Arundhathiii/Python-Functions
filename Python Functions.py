 # Python - Functions

# 1)What does the len() function do in Python? Write a code example using len() to find the length of a list.
# my_list = [1,2,3,4,5,6]
# print(my_list)
# print(len(my_list))

# 2)Write a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!".
# def greet(name):
#     print("Hello"+name+"!")
# greet("Anu")

"""
  3)Write a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value
 without using the built-in max() function. Use a loop to iterate through the list and compare values
"""
# def find_maximum(numbers):
#     # Initialize the maximum value to the first element in the list
#     max_value = numbers[0]
#     # Iterate through the list starting from the second element
#     for num in numbers[1:]:
#         # Compare the current element with the max_value
#         if num > max_value:
#             # Update max_value if the current element is greater
#             max_value = num
#
#     # Return the maximum value found
#     return max_value
# numbers = [3, 1, 4, 1, 5, 9, 2]
# print(find_maximum(numbers))

"""
  4)Explain the difference between local and global variables in a Python function.
    Write a program where a global variable and a local variable have the same name and 
    show how Python differentiates between them.
"""
# x = 10  # global variable
#
# def my_function():
#     x = 20  # local variable
#     # print("Local x:", x)
#
# print("Global x:", x)
# my_function()
# print("Global x:", x)

"""
  5)Create a function calculate_area(length, width=5) that calculates the area of a rectangle. 
    If only the length is provided, the function should assume the width is 5. 
    Show how the function behaves when called with and without the width argument.
"""
# def calculate_area(length,width=5):
#     return length*width
# # Calling the function with only the length argument
# print("area of the rectangle:",calculate_area(10)) # Output: 50 (uses default width=5)
#
# # Calling the function with both length and width arguments
# print("area of the rectangle:",calculate_area(10,20)) # Output: 200 (uses provided width=20)
#
# # Calling the function with only the length argument again
# print("area of the rectangle:",calculate_area(15))   # Output: 75 (uses default width=5)
