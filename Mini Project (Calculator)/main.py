import sys
sys.path.append("D:\Courses\DEPI IBM DS\Mini Project (Calculator)") # if you have problem importing the file use your file path 
import calc
def main():
    while True:
        command = input("Enter command ('add', 'sub', 'mult', 'div') or 'stop' to exit: ").strip().lower()
        if command == "stop":
            print("Exiting the calculator. Goodbye!")
            break

        if command not in ["add", "sub", "mult", "div"]:
            print("Invalid command. Please try again.")
            continue

        try:

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if command == "add":
                result = calc.add(num1, num2)
            elif command == "sub":
                result = calc.sub(num1, num2)
            elif command == "mult":
                result = calc.mult(num1, num2)
            elif command == "div":
                result = calc.div(num1, num2)

            print(f"The result of {command} operation is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__": #This checks if the script is being run directly (not imported as a module in another file).
    main()
