from random import randint
class Player(object):
    def __init__(self, bank, bet):
        self.bank = bank
        self.bet = bet
    def __str__(self):
        return "Bank: %s"%(self.bank)
    def set_bet(self):
        while True:
            value = int(input("How much money will you bet?\n"))
            if value > self.bank:
                print("That bet is too high fool, you ain't rich enough, try again")
            else:
                self.bet = value
                break
        return value
    def set_bank(self):
        while True:
            try:
                amount = int(input("How much money will you start with in your bank?"))
                self.bank = amount
                break
            except:
                print("bro enter a number")
        return amount
    def choice(self):
        while True:
            p_choice = input("player's Move: ")
            if p_choice == "hit" or p_choice == "stand":
                break
            else:
                print("no, choose hit or stand idiot")
        return p_choice
    def hit(self, deck):
        card = randint(0, 11)
        return deck[card]

class Dealer(object):
    def dealer_hit(self, deck):
        card = randint(0, 11)
        return card
    def first_two(self, output_deck, user_total):
        card1 = randint(0,11)
        card2 = randint(0,11)
        user_total = deck[card1] + deck[card2]
        print("Your first two cards are " + output_deck[card1] + " and " + output_deck[card2])
        return user_total 
class Game(object):
    def calc_bank(self, bank):
        pass
    def replay(self):
        while True:
            r = input("One more round? (Y/N)")
            if r == "Y":
                return True
            elif r == "N":
                return False
            else:
                print("try again, dumbass")

dealer = Dealer()
game = Game()
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
output_deck = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
user_bet = 0
user_bank = 0
cont = True
inner_cont = True
end_game = False
player = Player(user_bank, user_bet)
user_bank = player.set_bank()
print("Lets start the round mofo, type hit and stand to hit and stand\n")

while cont == True:
    user_total = 0
    dealer_total = 0
    user_bet = player.set_bet()
    user_total = dealer.first_two(output_deck, user_total)
    
    while inner_cont == True:
        play = player.choice()
        if play == "hit":
            user_hit = player.hit(deck)
            user_total = user_total + deck[user_hit]
            print("you're next card is a " + output_deck[user_hit] + "\nYour Current Total: " + str(user_total))
            if user_total > 21:
                print("\nbro you busted")
                user_bank = user_bank - user_bet
                print("Your bank total is " + str(user_bank))
                end_game = True
                break
            
            elif user_total == 21:
                print("Bro congrats you won")
                user_bank = user_bank + user_bet
                print("Your bank total: " + str(user_bank))
                end_game = True
            inner_cont = True      
        else:
            inner_cont = False
            end_game = False
    if end_game == False:
        while dealer_total < 17 and dealer_total < user_total:
            dealer_card = dealer.dealer_hit(deck)
            dealer_total = dealer_total + deck[dealer_card]
            print("Dealer: " + output_deck[dealer_card])
        
        print("\nDealer Total: " + str(dealer_total))
        if dealer_total > user_total and dealer_total <= 21:
            print("sry bro the dealer won")
            user_bank = user_bank - user_bet
            print("Your bank total: " + str(user_bank))
        
        elif dealer_total == user_total:
            print("Its a tie bro, aint nobody getting money")
        else:
            print("Bro you won, nice")
            user_bank = user_bank + user_bet
            print("Your bank total: " + str(user_bank))
    if user_bank > 0:
        cont = game.replay()
        inner_cont = True
    else:
        print("Bro you dead, its time to go")
        cont = False