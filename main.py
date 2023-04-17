import random


class Player:
    def __init__(self, score=0):
        self.score = score
        self.moves = ['rock', 'paper', 'scissors']

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        choice = input("Choose your move, R for rock,"
                       " P for paper or S for scissors?\n")
        if choice == 'S' or choice == 's' or choice == 'scissors':
            return 'scissors'
        elif choice == 'P' or choice == 'p' or choice == 'paper':
            return 'paper'
        if choice == 'R' or choice == 'r' or choice == 'rock':
            return 'rock'
        else:
            print("This is an invalid input")
            return self.move()

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def move(self):
        # check if my_move is not yet added (round-01)
        # to the dictionary class (self object) beside score & moves
        if len(self.__dict__.keys()) == 2:
            self.my_move = random.choice(self.moves)
            return self.my_move
        # check if my_move is added (round-02,03)
        # to the dictionary class (self object) beside score & moves
        elif len(self.__dict__.keys()) > 2:
            print(self.my_move)
            return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = their_move
        return my_move


class CyclePlayer(Player):
    def move(self):
        if len(self.__dict__.keys()) == 2:
            return random.choice(self.moves)
        else:
            if self.my_move in self.moves:
                # get the index of the item
                indx = self.moves.index(self.my_move)
                # create a repeatted list to avoid out of rane error
                cycle_list = [x for i in range(2) for x in self.moves]
                return cycle_list[indx + 1]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        return my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("Player 1 wins the round!")
            self.p1.score = + 1
        elif beats(move2, move1):
            print("Player 2 wins the round!")
            self.p2.score = + 1
        else:
            print("That was a tie!")

    def play_game(self):
        print("Game start!")
        print('Hello, you are playing the traditional'
              ' Rock Paper Scissors as Player 1')
        print("The game will run in 3 rounds")
        for round in range(3):
            print(f"Round {round+1}:")
            self.play_round()
            print(f"Player 1 score is: {self.p1.score}")
            print(f"Player 2 score is: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print(f"Final Game Score: {self.p1.score}/{self.p2.score}")
            print("__Player 1 wins the game!__")
        else:
            print(f"Final Game Score: {self.p1.score}/{self.p2.score}")
            print("__Player 2 wins the game!__")
        print("Game over!")


if __name__ == '__main__':
    opponent = input("Choose your opponent, R for Random Player, "
                     "Ref for Reflected Player or C for Cycle Player\n")
    if opponent == 'R' or opponent == 'r':
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
    elif opponent == 'Ref' or opponent == 'ref':
        game = Game(HumanPlayer(), ReflectPlayer())
        game.play_game()
    elif opponent == 'C' or opponent == 'c':
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()
    else:
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
