# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main(argv):

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    with open(argv[1],'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            teams+=[row]
    #print(teams)
    # TODO: Read teams into memory from file

    winner=[]
    counts = {}
    for i in range(N):
        winner=simulate_tournament(teams)
        #print(list(winner[0].items())[0])
        if list(winner[0].items())[0][1] in counts:
            counts[list(winner[0].items())[0][1]]+=1
        else:
            counts[list(winner[0].items())[0][1]]=1
    # TODO: Simulate N tournaments and keep track of win counts

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((int(rating2) - int(rating1)) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):

    while len(teams)!=1:
        teams=simulate_round(teams)
    return teams


if __name__ == "__main__":
    main(sys.argv)
