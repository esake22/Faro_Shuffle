import random

#farrow shuffle
def faro_shuffle(size=52,out=True):
    cards = [x for x in range(size)]
    print('Original Deck: ', cards)

    #shuffle cards
    random.shuffle(cards)
    print('Shuffled Deck: ', cards)
    #make copy to compare to at the end
    deck = cards.copy()

    shuffles = shuffles_needed(size)
    for x in range(shuffles):
        print('Round ',x +1, ' of shuffling')
        #split deck
        left = cards[0:len(cards)//2]
        print('Left Pile: ', left)

        right = cards[len(cards)//2:]
        print('Right Pile: ', right)

        cards = []

        if out: #out shuffled (odd first)
            for y in range(size//2):
                cards.append(left[y])
                cards.append(right[y])
        else: #in shuffled (even first)
            for y in range(size//2):
                cards.append(right[y])
                cards.append(left[y])
        print('Shuffled Deck: ', cards)

    print('Final Deck: ', cards)
    print('Original shuffled deck', deck)
    if cards == deck:
        print('Success')
    else:
        print('Failure')


def shuffles_needed(n):
    """Calculate shuffles needed for n-card deck (out-shuffle)"""
    if n % 2 != 0:
        return "Deck size must be even"

    mod = n - 1
    k = 1
    power = 2

    while power % mod != 1:
        power = (power * 2) % mod
        k += 1

    return k


# Test it
faro_shuffle(52)
