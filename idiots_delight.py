import cards

# This module of the project has the functions required to run the game

def deal_hand():
    my_deck = cards.make_deck()  # here we make a deck of 52 cards
    hand1 = []
    for i in range(4):
        cards.draw(my_deck, hand1)  # once again calling the draw function to add cards to an empty hand
    return my_deck, hand1


def discard(hand, numcards):
    # used to get rid of a card using the .pop function
    if len(hand) < 4 or (numcards != 2 and numcards != 4):
        return hand
    elif numcards == 4:
        for x in range(4):
            hand.pop()
    else:
        hand.pop(len(hand) - 2)
        hand.pop(len(hand) - 3)
    return hand


def play_round(deck, hand):
    # This function is used to play one round each time. The function first ensures there are more than 4 cards in the hand, before checking to discard any cards
    while len(hand) < 4:
        cards.draw(deck, hand)
    print(hand)
    if deck[0] != "":
        cards.draw(deck, hand)
        print(hand)
    have_discarded = True
    while len(hand) > 4 and have_discarded == True:
        if hand[(len(hand) - 4)][0] == hand[(len(hand) - 1)][0]:
            hand = discard(hand, 4)
        elif hand[(len(hand) - 2)][1] == hand[(len(hand) - 3)][1]:
            hand = discard(hand, 2)
        else:
            have_discarded = False
    return deck, hand


def main():
    # We run the game until the deck is empty, and declare whether the user won or lost.
    my_game = deal_hand()
    hand = list(my_game[1])
    while len(my_game[0]) > 0:
        my_game = play_round(my_game[0], hand)
    if len(my_game[1]) == 0:
        print("You won! Game over")
    else:
        print("You had " + str(len(my_game[1])) + " cards remaining")
        print("You lost :( Better luck next time!")


main()
