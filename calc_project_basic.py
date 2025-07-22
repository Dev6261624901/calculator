while True:
    try:
        print("\n--- Simple Calculator ---")
        print("Type 'exit' at any time to quit.")
        
        a_input = input("Enter operand number 1: ")
        if a_input.lower() == "exit":
            print("Goodbye!")
            break
        a = int(a_input)

        b_input = input("Enter operand number 2: ")
        if b_input.lower() == "exit":
            print("Goodbye!")
            break
        b = int(b_input)

        print('''Choose the operation you want to perform:
+  → Addition
-  → Subtraction
*  → Multiplication
/  → Division
// → Floor Division
%  → Modulus''')

        o = input("Enter your operator (or 'exit' to quit): ")
        if o.lower() == "exit":
            print("Goodbye!")
            break

        match o:
            case "+":
                print(f"The addition of {a} and {b} is: {a + b}")
            case "-":
                print(f"The subtraction of {a} and {b} is: {a - b}")
            case "*":
                print(f"The multiplication of {a} and {b} is: {a * b}")
            case "/":
                if b != 0:
                    print(f"The division of {a} and {b} is: {a / b}")
                else:
                    print("Error: Cannot divide by zero.")
            case "//":
                if b != 0:
                    print(f"The floor division of {a} and {b} is: {a // b}")
                else:
                    print("Error: Cannot floor divide by zero.")
            case "%":
                if b != 0:
                    print(f"The modulus of {a} and {b} is: {a % b}")
                else:
                    print("Error: Cannot take modulus by zero.")
            case _:
                print("Invalid operator entered.")
    except ValueError:
        print("Please enter valid integer numbers.")
    except Exception as e:
        print("An unexpected error occurred:", e)