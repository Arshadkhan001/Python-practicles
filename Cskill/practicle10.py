#write a python program to sort a list of tuple using lambda

# List of tuples
tuples_list = [(2, 3), (1, 2), (4, 1), (3, 4)]

# Sort the list of tuples based on the first element
sorted_tuples = sorted(tuples_list, key=lambda x: x[0])

# Print the sorted list
print("Sorted list of tuples:", sorted_tuples)

print("programmed by Arshad Khan roll no.85")