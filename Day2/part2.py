total_power = 0

while (game := input()) != '':
    rounds = game.split(":")[1].split(';')
    min = {color: max(int(count) for count, clr in (map(str.strip, cube.split()) for round in rounds for cube in round.split(',')) if clr.lower() == color) for color in ['red', 'green', 'blue']}
    total_power += min["red"] * min["green"] * min["blue"]

print(total_power)
