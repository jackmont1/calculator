#make a calculator that can add, subtract, multiply, and divide

#path: place your file path here

#welcome message
def welcome():
    print('''
Welcome to Jackson's Calculator''')

#define calculate()
def calculate():
    operation = raw_input('''
Please choose an operation:
+ for addition
- for subtraction
* for multiplication
/ for division
''''''
''')

    if operation == '+':
        num1 = int(input('Enter your first number: '))
        num2 = int(input('Enter your second number: '))
        print('{} + {} ='.format(num1, num2))
        print(num1 + num2)

    elif operation == '-':
        num1 = int(input('Enter your first number: '))
        num2 = int(input('Enter your second number: '))
        print('{} - {} ='.format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        num1 = int(input('Enter your first number: '))
        num2 = int(input('Enter your second number: '))
        print('{} * {} ='.format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        num1 = int(input('Enter your first number: '))
        num2 = int(input('Enter your second number: '))
        print('{} / {} ='.format(num1, num2))
        print(num1 / num2)

    else:
        return(error())

    again()

#define again()
def again():
    calc_again = raw_input('''
Do you want to execute another operation?
Type Y for YES or N for NO.
''''''
''')

    if calc_again.upper() == 'Y':
        calculate()
        return(again())

    elif calc_again.upper() == 'N':
        print('Goodbye!')
        quit()

    else:
        again()


#define error()
def error():
    invalid_operation = raw_input('''
Uh-oh! You have entered an invalid operation.
Would you like to return and enter a valid operation?
Type Y for YES or N for NO.
''''''
''')

    if invalid_operation.upper() == 'Y':
        return(calculate())

    elif invalid_operation.upper() == 'N':
        print('Goodbye!')
        quit()

    else:
        print('Goodbye!')
        quit()

#function calls
welcome()
calculate()
again()
