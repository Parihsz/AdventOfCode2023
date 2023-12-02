max = {'red': 12, 'green': 13, 'blue': 14}
games = []

while (game := input('')) != '':
    id = int(game.split(":")[0].split()[1])
    rounds = game.split(":")[1].split(';')
    if not any(int(count) > max[color] for round in rounds for count, color in (part.strip().split() for part in round.split(','))):
        games.append(id)

print(sum(games))
