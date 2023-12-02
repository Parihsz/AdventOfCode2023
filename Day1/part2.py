import re

mapping = {
    'one': 'one1one', 'two': 'two2two', 'three': 'three3three',
    'four': 'four4four', 'five': 'five5five', 'six': 'six6six',
    'seven': 'seven7seven', 'eight': 'eight8eight', 'nine': 'nine9nine'
}

total = 0

while (line := input("").lower()) != '':
    for key, value in mapping.items():
        line = re.sub(key, value, line)
    digits = re.findall(r'\d', line)
    if digits:
        total += int(digits[0] + (digits[-1] if len(digits) > 1 else digits[0]))

print("Total:", total)