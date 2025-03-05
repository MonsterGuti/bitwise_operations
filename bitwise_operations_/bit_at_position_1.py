number = int(input())

binary_list = []
my_num = number

while my_num > 0:
    binary_list.append(my_num % 2)
    my_num //= 2

if len(binary_list) > 1:
    position_1_bit = binary_list[1]
else:
    position_1_bit = 0

print(f"The bit at position 1 in {number} is {position_1_bit}")
