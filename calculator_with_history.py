history_file = "history.txt"

def show_history():
    f = open(history_file,"r")
    lines = f.readlines()
    if len(lines) == 0:
        print("No history found!")
    else:
        print("Your history:")
        for line in reversed(lines):
            print(line.strip())
            f.close()

def clear_history():
    f = open(history_file,"w")
    f.close()
    print("History cleared")

def save_to_history(equation,result):
    f = open(history_file,"a")
    f.write(f"{equation} = {result}\n" )
    f.close()

def calculation(user_input):
    allowed_input = "0123456789+-*/%.() "
    if not all(char in allowed_input for char in user_input):
        print("Invalid input.Try using numbers and (+ - * / %)")
        return
    try:
        result = eval(user_input)
        if result == int(result):
            result = result
        print(f"Result = {result}")
        save_to_history(user_input,result)
    except ZeroDivisionError:
        print("Cannot divide by Zero")
    except Exception:
        print("Invalid input.Try this format: num op num (e.g. 5 + 6  9 - 4))")


def main():
    print("\n--SIMPLE CALCULATOR WITH HISTORY")
    while True:
        user_input = input("Enter calculation / Command (history or clear or exit): ").lower()
        if user_input == "exit":
            print("\nCalculator closed.Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculation(user_input)

main()