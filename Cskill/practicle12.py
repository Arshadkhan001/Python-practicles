#write a python program to find prime number of a given number

#taking number from user
num = int(input("Enter the number: "))

if num == 1:
    print("it is not a prime number:")
if num > 1:
    for i in range (2,num):
        if num % i == 0:
            print("it is not a prime number:")
            break
    else:
        print("it is prime number")
        
print("programmed by Arshad Khan roll no.85")