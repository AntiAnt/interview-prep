We are going to explore a modified game of Snakes & Ladders (https://www.ymimports.com/pages/how-to-play-snakes-and-ladders):
0. Players lands on ladder, move up to the other end. (Original rule).
1. Players lands on head of snake, move down to the other end (Original rule).
2. There's one new element, called "Trap". If a player lands on a trap,
   game over for that player.
3. Instead of rolling a dice, the player flips a coin. Head means move 2 steps,
   tail means move 3 steps. (we may extend this later to more potential moves)
4. If you get to the final grid point you win the game.

There may be elements of the game that are unclear, so let's talk them through whenever you find them. If you have to make a decision about the rules just let me know and we can talk it through.

part1:

Let's write a simulation of where players will end up after N steps. A function (or class, your choice), that takes in a map definition and outputs the position after a given amount of moves.

Can we compute the mean time to finish a particular game?

Write a function or class (or if you have an alternative, feel free to ask about doing it some other way) that simulates a game after N steps. It should give us a list of player positions over time. If the game ends before N steps, we can return a list with less than N elements.

Please use good coding style and you are free to write tests or whatever else will help you.

part2:

Let's write a function (or a class, your choice) that tells us whether a map is completable. This means whether its possible for a player to complete (even if its improbable). Given a map definition, return whether that map can be completed