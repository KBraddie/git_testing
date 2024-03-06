print(input("Enter Data to be printed:"))


class Calculation:
    def __innit__(self):
        pass

    def addition(self, num1, num2):  # adds together two integers
        print(f"{num1}+{num2}={num1 + num2}")  # prints sum of two integers

    def subtract(self, num1, num2):  # subtracts two integers
        print(f"{num1}-{num2}={num1 - num2}")  # prints subtraction of two integers


# obtain user input of numbers for addition
num_req1 = int(input("Enter the first number for calculation:"))
num_req2 = int(input("Enter the second number for calculation:"))

new_object = Calculation()  # create object of class
new_object.addition(num_req1, num_req2)  # call addition function
new_object.subtract(num_req1, num_req2)  # call subtract function
