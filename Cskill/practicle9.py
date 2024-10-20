#write python program in which a class is defines, then create object of that class and call simple print 
#function define in class

# Define a class
class MyClass:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("Name:", self.name)

# Create an object of the class
my_object = MyClass("Arshad")

# Call the print function
my_object.print_name()

print("programmed by Arshad Khan roll no.85")
