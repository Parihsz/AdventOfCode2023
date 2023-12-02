total_sum = 0
while (line := input()) != "":
    digits = ''.join(filter(str.isdigit, line))
    total_sum += int(digits[0] + digits[-1]) if digits else 0
print(total_sum)
