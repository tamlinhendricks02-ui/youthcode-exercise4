fruits = ["pears" , "cherries" , "mangoes"]

for fruit in fruits:
    print(fruits)




count = 5

while count >= 1:
    print(count)
    count -= 1




squares = []

for i in range(1, 11):

    print(i ** 2)




import random 

colours = ["red", "green", "blue", "purple"]
for colour in range(3):
    hold= random.choice(colours)
    print(hold)


import math_operations


import math_operations as mo

print("--- Testing Functions Directly ---")
print(f"5 + 3 = {mo.add(5, 3)}")
print(f"10 - 4 = {mo.subtract(10, 4)}")
print(f"6 * 7 = {mo.multiply(6, 7)}")
print(f"20 / 4 = {mo.divide(20, 4)}")
print("-" * 34 + "\n")


def run_calculator():
    print("Welcome to the Custom Module Calculator!")
    
    while True:
        print("\nSelect an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
                
            if choice == '1':
                result = mo.add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = mo.subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = mo.multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                result = mo.divide(num1, num2)
                print(f"Result: {result}")
        else:
            print("Invalid choice. Please select a valid option from the menu (1-5).")

if __name__ == "__main__":
    run_calculator()







