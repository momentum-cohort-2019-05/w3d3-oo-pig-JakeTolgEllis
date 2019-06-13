from gameClasses import Player, Dice

name = input("What's your name? ")

player1 = Player(name)
player2 = Player("CPU")
dice = Dice()

def round_of_game(player):
    keep_rolling = True
    round_score = 0
    while keep_rolling:
        a = input("Hit ENTER to roll dice. Input H to hold. ")
        if a.lower == "f":
            keep_rolling = False
        elif a == "":
            roll_score = dice.roll()
            if roll_score == 0:
                round_score = 0
                return round_score
        else:
            print("I didn't recognize that input.")
    return round_score

    