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



print("This is a prefix calculator.\nThe available operators are:\n+ for addition \n- for subtraction \n* for multiply \n/ for divide \nsquare for square \ncube for cube \npow for power \nmod for modulo")

while True:
    tokens = []
    user_input = input("> ")
    operator_list = ["+", "-", "*", "/", "square", "cube", "pow", "mod"]
    tokens = user_input.split(' ')
    operator = tokens[0]

    if operator == "q":
        print("Goodbye!")
        break
    
    if operator not in operator_list:
        print("You entered an invalid operator!")
        continue

    # converting 1st operand to float
    num1 = tokens[1]
    try:
        num1 = float(num1)
    except:
        print("Oops, not a number! Please try again.")
        continue


    # checking for 2nd operand
    # if 2nd operand- converting to float, error msg if unable 
    if len(tokens) == 3:
        num2 = tokens[2]
        try:
            num2 = float(num2)
        except:
            print("Oops, not a number! Please try again.")
            continue

    if operator == "+":
        result = add(num1, num2)
    
    elif operator == "-":
        result = subtract(num1, num2)
    
    elif operator == "*":
        result = multiply(num1, num2)
    
    elif operator == "/":
        result = divide(num1, num2)
    
    elif operator == "square":
        result = square(num1)
    
    elif operator == "cube":
        result = cube(num1)
    
    elif operator == "pow":
        result = power(num1, num2)
    
    elif operator == "mod":
        result = mod(num1, num2)

    print(result)