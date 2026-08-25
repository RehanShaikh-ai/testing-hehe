def divide(dividend: int, divisor: int):
    try:
        return dividend / divisor
    except ArithmeticError as e:
        print(f"Something went wrong ! {e}")
