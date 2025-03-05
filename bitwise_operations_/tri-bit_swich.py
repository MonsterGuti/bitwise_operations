n = int(input("Enter a 32-bit integer: "))
p = int(input("Enter the bit position (0-29): "))

if 0 <= p <= 29:
    mask = 0b111 << p
    result = n ^ mask
    print("Resulting number:", result)
else:
    print("Invalid position. Must be between 0 and 29.")
