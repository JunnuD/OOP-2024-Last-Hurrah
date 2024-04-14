# Authors: Junnu Danhammer & Aarni Kaartokallio

import random

class Dice:
    def __init__(self):
        self.value = 0  # Initial value before the first roll

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

def roll_all_dices(dices):
    return [dice.roll() for dice in dices]

def show_dice_values(dice_values):
    for i, value in enumerate(dice_values, start=1):
        print(f"Rolled number for dice {i}: {value}")

def tiebreaker(dices):
    print("Tiebreaker initiated...")
    while True:
        dice_values = roll_all_dices(dices)
        show_dice_values(dice_values)
        if len(set(dice_values)) == 1:  # If there's still a tie, roll again
            print("Tie in tiebreaker, rolling again...\n")
        else:
            winner_dice = dice_values.index(max(dice_values)) + 1
            print(f"Tiebreaker winner is dice {winner_dice} with value {max(dice_values)}\n")
            break

def play_game():
    num_dice = int(input("Enter the number of dice: "))
    dices = [Dice() for _ in range(num_dice)]

    total_round_sums = []
    for round_number in range(1, 4):  # 3 rounds
        print(f"\nRound {round_number}")
        dice_values = roll_all_dices(dices)
        round_sum = sum(dice_values)
        total_round_sums.append(round_sum)
        show_dice_values(dice_values)
        print(f"Round sum: {round_sum}")

    # Check for tie after all rounds are completed
    if len(set(total_round_sums)) == 1:  # Indicates a tie
        tiebreaker(dices)
    else:
        max_sum = max(total_round_sums)
        winner_round = total_round_sums.index(max_sum) + 1
        print(f"\nWinner is found in round {winner_round} with the highest sum: {max_sum}")

       
class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
        self.dice = Dice()  # Each player has one dice
        self.pet = None  # Will be set in Part 5
    
    def roll_dice(self):
        return self.dice.roll()
    
    def set_pet(self, pet):
        self.pet = pet
    
    def __str__(self):
        return f"Player {self.player_id}: {self.name}, Pet: {self.pet}"
        
        
class Attributes:  # WORK IN PROGRESS
    def __init__(self, ID, name, attribute):
        self.ID = ID
        self.name = name
        self.attribute = attribute
        
    def __str__(self):
        return f"Attribute: {self.attribute}, Name: {self.name}"
    
    def create_attributes():
    # Create a list of attributes,  selection can be based on dice roll
        return [
            Attributes(ID=1, name="Yllätyskyykky", attribute="Löydä uusi noppa pöksyistäsi!"),
            Attributes(), # Add here as many as we like...
        ]
        
    def select_attribute_for_player(player, attribute):
    # Roll two dices to determine the pet
    dice1, dice2 = Dice(), Dice()
    roll_sum = dice1.roll() + dice2.roll()
    print(f"{player.name} rolled a {roll_sum} selecting a attribute.") # THIS IS WRONG NOW

    # Select a attribute based on the dice roll, mapping the roll sum to the list of attributes
    
    selected_index = min(roll_sum-2, len(attribute)-1)  # -2 because minimum roll sum is 2, and we adjust for list index
    selected_pet = attribute[selected_index]
    player.set_attribute(selected_pet)
    print(f"{player.name} now has a pet: {selected_attribute}")
    
def main():
    # Create players
    players = [Player("Alice", 1), Player("Bob", 2)]

    # Create attributes WORK IN PROGRESS
    Attributes = create_attribute()

    # Assign a attribute to each player WORK IN PROGRESS
    for player in players:
        select_attribute_for_player(player, Attributes)

    # Print out each player and their attribute information WORK IN PROGRESS
    for player in players:
        print(player)

if __name__ == "__main__":
    main()