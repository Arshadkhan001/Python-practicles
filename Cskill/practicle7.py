#write a python program to find largest of three numbers

# Function to find the largest of three numbers
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# passing value to the function 
largest = find_largest(10, 20, 15)
print("The largest number is:", largest)

print("programmed by Arshad Khan roll no.85")