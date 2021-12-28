# BlackJack OOP

###################################
# Classes
###################################

# For Shuffling cards 
import random

# For Deck Generation. Ace is initialized at 1.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

#  Stores Suit, Rank, and Values 
class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit 
        self.rank = rank 
        self.value = values[rank]
    
# Creates all 52 card objects, and holds them as a list 
# CAN shuffle the deck AND deal cards.
class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        # Loops thru suits and ranks
        for suit in suits:
            for rank in ranks:
                # Create the cards 
                created_card = Card(suit,rank)
                # Add to Deck
                self.all_cards.append(created_card)
                
    # Shuffles Deck 
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    # Deals 1
    def deal_one(self):
        return self.all_cards.pop(0)

# Will hold either the Computer's or Player's hands. 
# Must be able to add a single card.
class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
    
    
    def hit(self,new_card):
        self.all_cards.append(new_card)
    
    def __str__(self):
        return f'Player {self.name} has {self.all_cards} in their hand.'
    
# Will hold the player's balance, and any modifications.
# If player attempts to bet more than they have, then returns
# a FALSE Boolean, meaning that they can't bet.
class PlayerMoney:
    
    def __init__(self, balance):
        self.balance = balance
    
    def add(self,amount):
        self.balance += amount
        print(f"You currently have ${self.balance}")
        
    def bet(self,amount):
        if amount > self.balance:
            print("Insufficient Funds.")
            return False
        else:
            self.balance-=amount
            print(f"You have bet ${amount}. You currently have ${self.balance} left.")
            return True

##########################
# Game Logic
##########################

# Start the Game
game_on = True
player_balance = PlayerMoney(50)

while game_on:
    # Check if player has money. Mostly for continuous play. 
    if player_balance.balance > 0:
        # Creating and shuffling deck
        deck = Deck()
        deck.shuffle()

        # Making sure Player wants to play
        print(f"Your current balance is ${player_balance.balance} \n")
        while True:
            play_check = input("Play BlackJack (Y or N)? ")
            # If wanted input
            if play_check in ("Y","N"):
                if play_check == "Y":
                    print("I'll deal.\n")
                    break
                elif play_check == "N":
                    print("Coward.\n")
                    game_on = False
                    break
            # If not wanted input
            else:
                print("That's not an option.\n")

        # Ending game if player didn't want to play.
        if game_on == False:
            break

        # Player placing bet
        bet_placed = False
        bet_amount = 0 

        # Player Input
        while not bet_placed:
            try:
                bet_amount = int(input("How much will you bet? Enter a number. Note: Will Round Down. "))
            # Anything not a number.
            except:
                print("That's not a number.")
            # Update bet placed. Essential display info is taken from the class.
            else:
                # Making sure it's a positive value.
                if bet_amount > 0:
                    bet_placed = player_balance.bet(bet_amount)
                else:
                    print("Ha Ha. No.")
                    
        ###############
        # Player Turn 
        ###############
        player_cards = []
        hit = True
        player_bust = False
        player_total = 0
        values['Ace'] = 11
        ace_present = False

        # Player goes until they want to stop or bust.
        while hit and not player_bust:
            # Dealing
            player_cards.append(deck.deal_one())

            # Getting summation of Player's hand
            for card in player_cards:
                player_total+=card.value

            # Checking if there's an Ace
            for card in player_cards:
                if card.rank == "Ace":
                    ace_present = True
                    break
                else:
                    ace_present = False

            # If over 21 and there's no Ace
            if player_total > 21: 
            # If over 21 and there's an Ace
                if ace_present:
                    # Set Ace's value = 1
                    values['Ace'] = 1
                    # Get hand summation again
                    player_total = 0
                    for card in player_cards:
                        player_total+=card.value
                    # Give new total.
                    print(f"You have an Ace! Your card total is now {player_total}. \n")
                    if player_total > 21:
                        print("Bust! \n")
                        player_bust = True

                else:
                    print(f"Your card total is {player_total}. Bust! \n")
                    player_bust = True

            # If, NOT elif because if the new value is less than 21 with an Ace 
            # It would pass over this, giving an unintended deal which we don't want. 
            if player_total <= 21:
                while True:
                    print(f"Your card total is {player_total}.")
                    play_check = input("Will you hit? (Y or N)? ")
                    # If wanted input
                    if play_check in ("Y","N"):
                        if play_check == "Y":
                            print("I'll deal.\n")
                            break
                        elif play_check == "N":
                            print("Coward.\n")
                            hit = False
                            break
                    # If not wanted input
                    else:
                        print("That's not an option.\n")

        ################
        # Computer Turn
        ################
        computer_cards = []
        hit = True
        computer_bust = False
        computer_total = 0
        values['Ace'] = 11
        ace_present = False

        # Computer goes until they get between 17 and 21 or busts.
        while computer_total not in range(15,22) and not computer_bust:

            # Dealing
            computer_cards.append(deck.deal_one())

            # Getting summation of Player's hand
            for card in computer_cards:
                computer_total+=card.value

            # Checking if there's an Ace
            for card in computer_cards:
                if card.rank == "Ace":
                    ace_present = True
                    break
                else:
                    ace_present = False

            # If over 21 and there's no Ace
            if computer_total > 21: 
            # If over 21 and there's an Ace
                if ace_present:
                    # Set Ace's value = 1
                    values['Ace'] = 1
                    # Get hand summation again
                    computer_total = 0
                    for card in computer_cards:
                        computer_total+=card.value
                    # Give new total.
                    print(f"Computer has an Ace! Computer card total is now {computer_total}. \n")
                    if computer_total > 21:
                        print("Bust! \n")
                        computer_bust = True

                else:
                    print(f"Computer card total is {computer_total}. Bust! \n")
                    computer_bust = True

            # If, NOT elif because if the new value is less than 21 with an Ace 
            # It would pass over this, giving an unintended deal which we don't want.
            # Just to give final total at end of computer turn.
            if total in range(15,22):
                print(f"Computer stops with a card total of {total}.")

        ################
        #Comparisons
        ################

        # Busts
        if player_bust == True:
            print("The Computer Wins!")
        elif computer_bust == True:
            print("The Player Wins!")
            winnings = bet_amount * 2
            player_balance.add(winnings)
        # Comparisons
        elif player_total < computer_total:
            print("The Computer Wins!")
        elif player_total > computer_total:
            print("The Player Wins!")
            winnings = bet_amount * 2
            player_balance.add(winnings)
        # An unlikely tie
        elif play_total == computer_total:
            print("Tie. Player gets their money back.")
            player_balance.add(bet_amount)
       
    # If player has no money.
    else:
        print("The player is out of money! They must stop!")
        game_on = False
