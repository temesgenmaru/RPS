#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.my_move = ''
        self.their_move = ''

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        move = valid_input("Rock, paper, scissors? > ", moves).lower()
        return move


class ReflectPlayer(Player):
    def move(self):
        if self.their_move == '':
            return random.choice(moves)
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == '':
            return random.choice(moves)
        else:
            value = moves.index(self.my_move)
            if value == 0:
                return moves[1]
            elif value == 1:
                return moves[2]
            else:
                return moves[0]


def beats(one, two):
    if ((one == 'rock' and two == 'scissors') or
       (one == 'scissors' and two == 'paper') or
       (one == 'paper' and two == 'rock')):
        return 1
    elif((one == 'rock' and two == 'rock') or
         (one == 'scissors' and two == 'scissors') or
         (one == 'paper' and two == 'paper')):
        return 2
    else:
        return 3


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'Sorry, "{option}" is an invalid option, Try again!')


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.count1 = 0
        self.count2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}\n")
        if beats(move1, move2) == 1:
            self.count1 += 1
            print("** PLAYER ONE WINS **")
            print(f'SCORE: Player One {self.count1}, '
                  f'Player Two {self.count2}\n')
        elif beats(move1, move2) == 2:
            print("** TIE GAME **")
        else:
            self.count2 += 1
            print("** PLAYER TWO WINS **")
            print(f'SCORE: Player One {self.count1}, '
                  f'Player Two {self.count2}\n')

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!\n")
        for round in range(2):
            print(f"Round {round+1}:")
            self.play_round()

        print(f'FINAL SCORE: Player One {self.count1}, '
              f'Player Two {self.count2} \n')
        if self.count1 > self.count2:
            print("** Player ONE WINS the overall game! **\n")
            print("Game over!")
            Game.play_again()

        elif self.count1 == self.count2:
            print("** No winner! The overall game is a TIE! **\n")
            print("Game over!")
            Game.play_again()

        else:
            print("** Player TWO WINS the overall game! **\n")
            print("Game over!")
            Game.play_again()

    def play_again():
        response = valid_input("Would you like to play again? Please "
                               "press y/n \n", ['y', 'n'])
        if 'n' in response:
            print("Thank you for playing the game.")

        else:
            print("Glad you decided to play the game again.")
            game.play_game()

    def choose_opponent():
        print("You can play this game against three types of opponents.\n")
        print("Enter 1 for Random Player. \n"
              "Enter 2 for Cycle Player. \n"
              "Enter 3 for Reflect Player.")

        opponent = valid_input("Choose your Opponent ", ['1', '2', '3'])
        if opponent == '1':
            return RandomPlayer()
        elif opponent == '2':
            return CyclePlayer()
        else:
            return ReflectPlayer()


if __name__ == '__main__':
    game = Game(Game.choose_opponent(), HumanPlayer())
    game.play_game()
