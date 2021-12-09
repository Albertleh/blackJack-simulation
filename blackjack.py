import pandas as pd
import os

deck_global = pd.DataFrame(['2s','2d','2c','2h','3s','3d','3c','3h','4s','4d','4c','4h','5s','5d','5c','5h','6s','6d','6h','6c','7s','7d','7c','7h','8s','8d','8c','8h','9s','9d','9c','9h','10s','10d','10c','10h','Js','Jd','Jc','Jh','Qs','Qd','Qc','Qh','Ks','Kd','Kc','Kh','As','Ad','Ac','Ah'])
""" created an additional file for me just to get the line above with the single quotes and commas automatically inserted
    for me to copy and paste cause I'm a lazy fuck who doesn't like manual work
    
    cards = pd.read_csv('deck.txt', header=None)
    fil = open('copy.txt', 'w+')
    fil.close()
    with open('copy.txt', 'a') as fil:
        for e in range(0, len(cards)-1):
            fil.write(f"'{cards[0][e]}',")
"""

""" TO DO LISt:
    
    - create BOT with a variable accuracy 0-100%
    - finish play hand function
    - create a paying system (maybe with external files) where wins and losses are documented   
        furthermore small little dashboard would be nice (maybe graph of bankroll)
    - implement card counting algorithm 
    - for large scale simulations of the card counting algorithm maybe implement threading
    - later on autogenerated datasets of the simulations would be nice BOT as well as card counting algorithm
    - find optimal card counting algorithm maybe later on machine learning
    - visualize data and insigths with seaborn library
    - create docker container for project
    - publish working project on github
"""

def generate_files():
    # Checks if deck.txt file exists and create a new one when not 
    if os.path.isfile("./deck.txt") == False:
        print('deck.txt not found! File containing a standard 52 Card deck has been created!')
        createf = open('deck.txt', 'w+')
        createf.close()
        deck_global.to_csv('deck.txt',index=False, header=None)

    # Checks if shoe.txt exists and create a new one when not
    if os.path.isfile("./shoe.txt") == False:
        print('shoe.txt not found! New file created!')
        createf = open('shoe.txt', 'w+')
        createf.close()

    # Checks if cardtray.txt exists and create a new one when not
    if os.path.isfile("./cardtray.txt") == False:
        print('cardtray.txt not found! New file created!')
        createf = open('cardtray.txt', 'w+')
        createf.close()


def shuffle_shoe(decks: int): 
    preshuffle = pd.read_csv("deck.txt", header=None)
    postshuffle = preshuffle.sample(frac = decks, replace=True)

    with open('shoe.txt','r+') as f:
        # empty shoe if necessary
        if os.path.getsize("./shoe.txt") > 0:
            f.truncate(0)
            print("shoe cleared")
        # empty cardtray if necessary
    with open('cardtray.txt','r+') as f:
        if os.path.getsize("./cardtray.txt") > 0:
            f.truncate(0)
            print("cardtray cleared")
    postshuffle.to_csv('shoe.txt',index=False, header=None)
    print(f"Shoe full of {decks} decks has been shuffled")

def draw_card() -> str:
    before_draw = pd.read_csv("shoe.txt", header=None)
    first_card = before_draw[0][0]
    after_draw = pd.DataFrame()
    after_draw = before_draw[0].iloc[1:]

    with open('shoe.txt', 'r+') as f:
        f.truncate(0)
    with open("shoe.txt", 'w+') as f:
        after_draw.to_csv('shoe.txt',index=False, header=None)
    with open("cardtray.txt", 'a') as f:
        f.write(f"{first_card}\n")
    return str(first_card)

def get_cardvalue(card: str) -> int:
    if 'A' in card:
        return 11
    elif 'K' in card:
        return 10
    elif 'Q' in card:
        return 10
    elif 'J' in card:
        return 10
    else:
        return int(card[:-1])
    

    
def play_hand():
    player_hand = []
    player_handvalue = 0
    dealer_hand = []
    dealer_handvalue = 0

    # player gets first card
    player_hand.append(draw_card())
    player_handvalue = player_handvalue + get_cardvalue(player_hand[0])
    print(f"player shows {player_hand[0]} = {player_handvalue}")
    # deaker draws second card
    dealer_hand.append(draw_card())
    dealer_handvalue = dealer_handvalue + get_cardvalue(dealer_hand[0])
    print(f"dealer shows {dealer_hand[0]} = {dealer_handvalue}")




def main():
    generate_files()
    #shuffle_shoe(3)
    play_hand()


if __name__ == '__main__':
    main()
