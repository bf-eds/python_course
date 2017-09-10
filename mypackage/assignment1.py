import sys

if len(sys.argv) == 1:
    print("You should enter a digit string")
    exit()

digit_string = sys.argv[1]

if not digit_string.isdigit():
    print("String contains not digits")
    exit()
sum = 0
for ch in digit_string:
    sum += int(ch)
print(sum)
