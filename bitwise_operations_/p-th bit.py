number = int(input())

binary_list = []
my_num = number
p = int(input())

while my_num > 0:
    binary_list.append(my_num % 2)
    my_num //= 2

if len(binary_list) < p:
    for i in range(16 - len(binary_list)):
        binary_list.append(0)

position_1_bit = binary_list[p]

print(f"The bit at position {p} in {number} is {position_1_bit}")
