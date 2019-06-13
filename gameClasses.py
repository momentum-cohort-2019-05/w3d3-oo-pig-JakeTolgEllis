from random import randint

class Player:
    def __init__(self, name, score=0, winner = False):
        self.score = score
        self.name = name
        self.winner = winner

    def is_winner(self):
        if self.score >= 100:
            self.winner = True

    def add_to_score(self, round_score):
        self.score += round_score
    


        
class Dice:
    # def __init__(self, number):
    #     self.number = number
         
    def roll(self):
        r = randint(1, 6)
        if r == 1:
            print("Oh No! You rolled a 1! You don't score anything this round.")
            return 0
        print(f"You rolled a {r}!")
        return r   