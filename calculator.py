print("Basic Calculator")

# Input numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("1. Sum")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choose = int(input("Enter your choice (1-4): "))

# Perform operation
if choose == 1:
    print("Result:", a + b)
elif choose == 2:
    print("Result:", a - b)
elif choose == 3:
    print("Result:", a * b)
elif choose == 4:
    if b != 0:   # avoid divide by zero error
        print("Result:", a / b)
    else:
        print("Error: Division by zero not allowed!")
else:
    print("Invalid Choice")
