import random
from typing import Dict, List

snakes = {
    34: 2,
    41: 22,
    48: 26,
    67: 35,
}
ladders = {5: 16, 8: 13, 88: 99, 74: 91, 40: 66, 36: 72, 24: 42, 17: 25}
traps = [15, 76, 98]

num_games = 100


def flip_coin() -> None:
    return random.randint(2, 3)


def play_game(ladders: Dict[int, int], snakes: Dict[int, int], traps: List[int]) -> int:
    player_position = 1
    turns = 0
    game_won = False

    while player_position < 100:
        spaces_to_move = flip_coin()
        potential_next_pos = spaces_to_move + player_position

        if potential_next_pos >= 100:
            game_won = True
            break
        elif potential_next_pos in traps:
            break
        elif potential_next_pos in snakes:
            player_position = snakes.get(potential_next_pos)

        elif player_position + spaces_to_move in ladders:
            player_position = ladders.get(potential_next_pos)

        else:
            player_position += spaces_to_move

        turns += 1

    return turns, game_won


def game_mean_time(
    num_games: int, ladders: Dict[int, int], snakes: Dict[int, int], traps: List[int]
) -> float:
    tot_rounds = 0
    games_won = 0
    for _ in range(num_games):
        game_rounds, game_won = play_game(ladders=ladders, snakes=snakes, traps=traps)
        tot_rounds += game_rounds
        if game_won:
            games_won += 1

    return (tot_rounds / num_games, games_won)


if __name__ == "__main__":
    mean_rounds, games_won = game_mean_time(
        num_games=num_games, ladders=ladders, snakes=snakes, traps=traps
    )
    print(f"Mean number of rounds: {mean_rounds} and games won: {games_won}")
