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

    while player_position < 100:
        spaces_to_move = flip_coin()
        potential_next_pos = spaces_to_move + player_position
        print(f"Player rolled: {spaces_to_move}")

        if potential_next_pos >= 100:
            print("Player wins!!")
            break
        elif potential_next_pos in traps:
            print(f"Player landed on {potential_next_pos}. It's a trap!\nGame Over.")
            break
        elif potential_next_pos in snakes:
            player_position = snakes.get(potential_next_pos)
            print(
                f"Player landed on the head of a snake. Sliding down to {player_position}!"
            )
        elif player_position + spaces_to_move in ladders:
            player_position = ladders.get(potential_next_pos)
            print(
                f"Player landed at the bottom of a ladder. climbing up to {player_position}!"
            )
        else:
            player_position += spaces_to_move
            print(f"Player landed on {player_position}.")

        turns += 1

    return turns


def game_mean_time(
    num_games: int, ladders: Dict[int, int], snakes: Dict[int, int], traps: List[int]
) -> float:
    tot_rounds = 0
    for _ in range(num_games):
        tot_rounds += play_game(ladders=ladders, snakes=snakes, traps=traps)

    return tot_rounds / num_games


if __name__ == "__main__":
    mean_rounds = game_mean_time(
        num_games=num_games, ladders=ladders, snakes=snakes, traps=traps
    )
    print(f"Mean number of rounds: {mean_rounds}")
