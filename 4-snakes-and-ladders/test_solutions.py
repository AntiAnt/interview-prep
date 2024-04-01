from dataclasses import dataclass
import random
from typing import Dict, List, Set, Tuple

snakes = {34: 2, 41: 22, 48: 26, 67: 35, 97: 64, 25: 17}
ladders = {5: 16, 8: 13, 88: 99, 74: 91, 40: 66, 36: 72, 24: 42, 17: 25}
traps = [15, 76]

num_games = 100


def visit_map_position(
    position: int,
    visited: Set[int],
    ladders: Dict[int, int],
    snakes: Dict[int, int],
    traps: List[int],
) -> bool:
    if position >= 100:
        return True
    if position in visited or position in traps:
        return False

    visited.add(position)
    if position in snakes:
        return visit_map_position(
            position=snakes[position],
            visited=visited,
            ladders=ladders,
            snakes=snakes,
            traps=traps,
        )
    elif position in ladders:
        return visit_map_position(
            position=ladders[position],
            visited=visited,
            ladders=ladders,
            snakes=snakes,
            traps=traps,
        )
    else:
        return any(
            [
                visit_map_position(
                    position=position + i,
                    visited=visited,
                    ladders=ladders,
                    snakes=snakes,
                    traps=traps,
                )
                for i in [2, 3]
            ]
        )


def map_compleatable(
    ladders: Dict[int, int], snakes: Dict[int, int], traps: List[int]
) -> bool:
    """we have 2 options at every position either roll a 2 or a 3. 
    Landing on a position offers one of 4 options, trap, snake, ladder, or nothing.
    using DFS to try every path and either find a path to the end or complete the 
    search with no path forward.
    """

    return visit_map_position(1, set(), ladders, snakes, traps)


def flip_coin() -> None:
    return random.randint(2, 3)


def play_game(
    ladders: Dict[int, int], snakes: Dict[int, int], traps: List[int]
) -> Tuple[int, int]:
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


def test_map_completeable() -> None:
    assert map_compleatable(ladders=ladders, snakes=snakes, traps=traps) == True


def test_map_not_compleatable_given_triple_traps() -> None:
    triple_traps = traps + [97, 98, 99]

    assert map_compleatable(ladders=ladders, snakes=snakes, traps=triple_traps) == False


def test_map_not_completable_given_triple_snakes_at_end() -> None:
    snakes_at_the_end = {**snakes, 97: 1, 98: 2, 99: 3}
    assert (
        map_compleatable(ladders=ladders, snakes=snakes_at_the_end, traps=traps)
        == False
    )


def test_map_compleatable_given_ladder_that_skips_triple_snakes() -> None:
    triple_snakes = {**snakes, 7: 1, 8: 2, 9: 3}
    ladder_that_skip = {6: 10}
    assert (
        map_compleatable(ladders=ladder_that_skip, snakes=triple_snakes, traps=traps)
        == True
    )


def test_map_not_compleatable_without_ladder_that_skips_triple_snakes() -> None:
    triple_snakes = {**snakes, 7: 1, 8: 2, 9: 3}
    assert map_compleatable(ladders=ladders, snakes=triple_snakes, traps=traps) == True


if __name__ == "__main__":
    # assert can_complete
    mean_rounds, games_won = game_mean_time(
        num_games=num_games, ladders=ladders, snakes=snakes, traps=traps
    )
    print(f"Mean number of rounds: {mean_rounds} and games won: {games_won}")
