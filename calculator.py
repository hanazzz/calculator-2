"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# print instructions with available commands
# while loop
    # ask user for input
    # tokenize input (split input)
    # if first token is "q":
        # break
    # try to convert the other two tokens to floats
    # except:
        # tell user they messed up
        # continue (skip checking remaining conditionals and start over)
    # if first token is "+":
        # result = call add() using last two tokens
    # elif first token is "-":
        # call subtract() using last two tokens
    # elif first token is "*":
        # call multiply() using last two tokens
    # elif first token is "/":
        # call divide() using last two tokens
    # elif first token is "square":
        # call square() using last two tokens
    # elif first token is "cube":
        # call cube() using last two tokens
    # elif first token is "pow":
        # call power() using last two tokens
    # elif first token is "mod":
        # call mod() using last two tokens
    # else
        # tell user input isn't allowed
    # give user answer (print result)