def add(x, y):             
    return x + y

def subtract(x, y):        
    return x - y

def multiply(x, y):        
    return x * y

def divide(x, y):          
    if y == 0:
        return            
    else:
        return x / y

print("Select operation:")

while True:
    choice = input("Enter choice (Add/Subtract/Multiply/Divide): ")

    if choice in ('Add', 'Subtract', 'Multiply', 'Divide'):
        num1 = float(input("Enter first number: "))
        num2 =float(input("Enter second number: "))

        if choice == 'Add':
            print("Result:", add(num1, num2))
        elif choice == 'Subtract':
            print("Result:", subtract(num1, num2))
        elif choice == 'Multiply':
            print("Result:", multiply(num1, num2))
        elif choice == 'Divide':
            print("Result:", divide(num1, num2))
        break
    else:
        print("Invalid Input")
