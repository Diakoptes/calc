from calc_layout import layout

class Calculator():
    """
    This is simple calculator that can: add, subtract, multiplication,
    division, exponentiation and give you  rest of divided.
    Calculator will check your numbers, you cannot divide by zero, 
    and you can give only numbers.
    """

    def calc_sum(first_num, second_num):
        """Addition function."""
        
        try:
            return float(first_num) + float(second_num)
        except ValueError as err:
            return "Unexpected value!"

    def calc_sub(first_num, second_num):
        """Subtract function"""

        try:
            return float(first_num) - float(second_num)
        except ValueError as err:
            return "Unexpected value!"
        
    def calc_multi(first_num, second_num):
        """Multiplication function."""
        
        try:
            return float(first_num) * float(second_num)
        except ValueError as err:
            return "Unexpected value!"

    def calc_div(first_num, second_num):
        """Division function."""
        try:
            return float(first_num) / float(second_num)
        except ZeroDivisionError as err:
            result.config(text=err)
        except ValueError as err:
            result.config(text="Unexpected value!")

    def calc_exp(first_num, second_num):
        """Exponentiation function"""
        
        try:
            return float(first_num) ** float(second_num)
        except ValueError as err:
            result.config(text="Unexpected value!")

    def calc_mod(first_num, second_num):
        """Remainder of divided function."""

        try:
            return float(first_num) % float(second_num)
        except ValueError as err:
            result.config(text="Unexpected value!")