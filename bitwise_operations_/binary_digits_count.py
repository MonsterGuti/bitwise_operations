number = int(input())
binary_digit = int(input())

binary_list = []
my_num = number

while my_num > 0:
    binary_list.append(my_num % 2)
    my_num //= 2

count = 0
for digit in binary_list:
    if digit == binary_digit:
        count += 1

print(f"{binary_digit} occurs {count} times in number {number}")