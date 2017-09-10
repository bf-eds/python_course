import sys

if len(sys.argv) == 1:
    print("You should enter a number of steps")
    exit()

digit_string = sys.argv[1]

if not digit_string.isdigit():
    print("String contains not digits")
    exit()

num_steps = int(digit_string)

step_symbol = "#"
space_symbol = " "

for step_num in range(1, num_steps + 1):
    space_num = num_steps - step_num
    print(space_symbol * space_num + step_symbol * step_num)
