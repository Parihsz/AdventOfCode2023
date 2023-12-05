schematic_lines = []
answer = 0

while True:
    line_input = input()
    if not line_input:
        break
    schematic_lines.append(line_input)

for row_index, line in enumerate(schematic_lines):
    i = 0
    while i < len(line):
        if line[i].isdigit():
            num_start = i
            while i < len(line) and line[i].isdigit():
                i += 1
            num_end = i
            adjacent_indices = [(row_index, num_start - 1), (row_index, num_end)] + \
                               [(row_index + offset, col) for offset in (-1, 1) for col in range(num_start - 1, num_end + 1)]
            symbol_count = sum(0 <= r < len(schematic_lines) and 0 <= c < len(schematic_lines[r]) and schematic_lines[r][c] not in '.0123456789'
                               for r, c in adjacent_indices)
            if symbol_count:
                answer += int(line[num_start:num_end])
        i += 1

print(answer)
