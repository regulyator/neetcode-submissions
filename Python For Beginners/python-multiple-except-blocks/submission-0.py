def divide_numbers(a: str, b: str) -> None:
    try:
        print(int(a) / int(b))
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as ex:
        print(f"An error occurred: {ex}")



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
