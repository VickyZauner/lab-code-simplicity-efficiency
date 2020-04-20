
# Calculator

numbers = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

# function for the calculation
def calculation (b,a,c):
    if b == "plus":
        equals = a + c
        print("The result of your calculation is ", equals)
    if b == "minus":
        equals = a - c
        print("The result of your calculation is ", equals)
    else:
        print("Sorry, I do not understand, please try again")
        print("Thanks for using this calculator, goodbye :)")

# welcoming, asking for input, starting the loop
print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
calculate = input("Would you like to use this calculator? ")

while calculate in ["yes", "y", "Yes"]:
    a = numbers.value(input('Please choose your first number ("zero" to "five"): '))
    c = numbers.value(input('Please choose your second number ("zero" to "five"): '))
    b = input('What do you want to do? "plus" or "minus": ')
    calculation()




