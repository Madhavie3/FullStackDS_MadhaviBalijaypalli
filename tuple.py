#A tuple in Python is an ordered, immutable, and heterogeneous sequence of elements. Tuples are defined using parentheses () and can contain 
# elements of different data types, such as integers, floats, strings, and even other tuples or lists. Once a tuple is created, its elements cannot be modified, 
# added, or removed, making it suitable for storing fixed collections of data.

empty_tuple = ()
print(empty_tuple)

my_tuple = ("apple", 42, 3.14, True)
print(my_tuple)

#slicing
nums = (0, 1, 2, 3, 4, 5)
print(nums[1:4])  # Output: (1, 2, 3)

#tuple with only integers
int_tuple = (10, 20, 30, 40, 50)
print(int_tuple)