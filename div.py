def divide(dividend: int, divisor: int):
    try:
        return dividend / divisor
    except ValueError:
        print("Please provide valid numbers !")
    except ZeroDivisionError:
        print("You can't divide by zero !")
    except ArithmeticError as e:
        print(f"Something went wrong ! {e}")
