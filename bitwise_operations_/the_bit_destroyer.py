number = int(input("Enter a number: "))
p = int(input("Enter bit position to remove: "))

binary_list = []
my_num = number

while my_num > 0:
    binary_list.append(my_num % 2)
    my_num //= 2

binary_list.reverse()

if p >= len(binary_list):
    print("Error: Bit position out of range")
else:
    binary_list.pop(len(binary_list) - 1 - p)
    print("".join(map(str, binary_list)))
