
try:
    while True:
        a_in = input("Enter the first number (or q to quit): ")
        if a_in.lower() == "q":
            print("Exiting the calculator. Goodbye!")
            break
        a = int(a_in)

        b_in = input("Enter the second number (or q to quit): ")
        if b_in.lower() == "q":
            print("Exiting the calculator. Goodbye!")
            break
        b = int(b_in)


        print("What kind of operation you want to perform.\nPress + for addition \nPress - for subtraction \nPress / for division \nPress * for multiplication \nPress '%' for percentage (a out of b) \nPress q to quit.")

        o = input("Enter Operation : ")
        match o:
            case "+":
                print(f"The result is : {a + b}")
            case "-":
                print(f"The result is : {a - b}")
            case "/":
                print(f"The result is : {a / b}")
            case "*":
                print(f"The result is : {a * b}")
            case "%":
                if b != 0:
                    print(f"{a} is {(a / b) * 100:.2f}% of {b}")
                else:
                    print("Error: Division by zero is not allowed in percentage.")
            case "q" | "Q":
                print(f"Exiting the Calculator. Goodbye!")
                break
            case _:
                print(f"There was an error")

except Exception as e:
    print("Enter a valid value of a and b")
