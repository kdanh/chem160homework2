from random import choices

ntrials = 10000

player1wins = 0

# total for player 1
total1 = 0

# total for player 2
total2 = 0

for i in range(ntrials):
    dice2 = choices(range(1,7), k = 2)

    if dice2[0] == dice2[1]:
        # player 2 wins
        continue

    else:
        total2 = dice2[0] + dice2[1]

    dice1 = choices(range(1,7), k = 3)
    dice1.sort(reverse=True)
    total1 = total1 + dice1[0] + dice1[1]

    if total1 > total2:
        player1wins = player1wins + 1

print(player1wins/ntrials)
