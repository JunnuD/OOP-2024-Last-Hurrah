import random
from colorama import Fore, Style, init
from tabulate import tabulate

init()  # Initialize colorama


class GameEntity:
    """Base class for all game entities."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Dice:
    """This class represents a 6-sided dice."""

    def roll(self):
        return random.randint(1, 6)


"""Different Dice types added to integrate polymorphism"""

class RegularDice(Dice):
    """This class represents a 6-sided dice."""

    def roll(self):
        print(f"{Fore.CYAN}Rolling regular dice...{Style.RESET_ALL}")
        return random.randint(1, 6)

class LoadedDice(Dice):
    """A dice that is loaded to favor higher numbers."""

    def roll(self):
        print(f"{Fore.YELLOW}Rolling loaded dice...{Style.RESET_ALL}")
        return random.randint(4, 6)


class MagicDice(Dice):
    """A magical dice that doubles the score on a roll of 6."""

    def roll(self):
        print(f"{Fore.MAGENTA}Rolling magic dice...{Style.RESET_ALL}")
        roll = super().roll()
        if roll == 6:
            print(f"{Fore.RED}Magic dice rolled a six! Double points on this turn!{Style.RESET_ALL}")
            return 12  # Doubled value for scoring purposes
        return roll


class Player(GameEntity):
    """Class to create a player with a name, list of attributes, and score."""

    def __init__(self, name):
        super().__init__(name)
        self.attributes = []
        self.score = 0

    def add_attribute(self, attribute, points):
        self.attributes.append(attribute)
        self.score += points
        print(f"{Fore.GREEN}{self.name} got: {attribute} and {points} points{Style.RESET_ALL}")

    def __str__(self):
        attributes_str = ", ".join(self.attributes)
        return f"{super().__str__()} : {attributes_str}, Points: {self.score}"


class Game:
    """Represents a dice-rolling game for multiple players, including game attributes and rounds."""

    def __init__(self):
        while True:
            try:
                num_players = int(input("How many players: "))
                if num_players < 1:
                    print(f"{Fore.RED}Please enter a number greater than 0.{Style.RESET_ALL}")
                    continue
                break
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a valid number.{Style.RESET_ALL}")

        self.players = [
            Player(input(f"Give player {i+1} name: ")) for i in range(num_players)]
        self.dice = [RegularDice(), LoadedDice(), MagicDice()]
        self.attribute_map = {
            2: ("Alien Attack in Salo", 55),
            3: ("Warm Hand To The Face", 45),
            4: ("Bees!", 35),
            5: ("Smashed Potatoes", 20),
            6: ("Broken Fishrod", 5),
            7: ("Fell Over", 5),
            8: ("New lecture with Marika about Project Management", 10),
            9: ("Bigfoot Sighting at Kupittaa", 20),
            10: ("Suprise Squat", 35),
            11: ("New Porsche (Lada)", 50),
            12: ("Yo Mama- jokes!", 55),
            13: ("Lucky Day (not really)", 60),
            14: ("Winning Lottery (in a dream)", 65),
            15: ("Found Treasure", 70),
            16: ("Moon Landing", 75),
            17: ("Discovered Atlantis from Aurajoki", 80),
            18: ("Time Travel back to the 90's", 100)
        }  
        
        # Here is the list of all attributes and points included with them


    def roll_dices_and_assign_attribute(self, player):
        input(f"{Fore.YELLOW}Press Enter to throw dices for {player.name}...{Style.RESET_ALL}")
        selected_dice = random.sample(self.dice, 2)  # Randomly select two dice
        roll_sum = sum(d.roll() for d in selected_dice)
        attribute_name, points = self.attribute_map.get(
            roll_sum, ("Nothing", 0))
        print(f"{player.name} threw {roll_sum} and got: {attribute_name}.")
        player.add_attribute(attribute_name, points)

    def play_round(self):
        for player in self.players:
            while True:  # Keep asking until a valid input is given
                choice = input(f"{Fore.BLUE}Does {player.name} want to throw dice? (Yes/No) {Style.RESET_ALL}").strip().lower()
                if choice == 'yes' or choice == 'no':
                    break  # Break the loop if the input is valid
                print(f"{Fore.RED}Invalid input. Please type 'Yes' or 'No'.{Style.RESET_ALL}")
            if choice == 'yes':
                self.roll_dices_and_assign_attribute(player)
            else:
                print(f"{Fore.RED}{player.name} opted out of rolling the dice.{Style.RESET_ALL}")

    def play(self):
        print(f"{Fore.CYAN}Game is starting! There are three (3) rounds to roll dices!{Style.RESET_ALL}")
        for round in range(1, 4):
            print(f"{Fore.MAGENTA}Round {round} starting:{Style.RESET_ALL}")
            self.play_round()

        # Determine the highest score
        max_score = max(player.score for player in self.players)

        # Find all players who have the max score (supports multiple winners in case of a tie)
        winners = [
            player.name for player in self.players if player.score == max_score]

        # Announce the outcome of the game

        print(f"\n{Fore.CYAN}Game's Outcome:{Style.RESET_ALL}")
        headers = ["Player", "Attributes", "Points"]

        # Sort players based on their scores in descending order
        data = sorted([(player.name, ", ".join(player.attributes), player.score) for player in self.players],
                      key=lambda x: x[2], reverse=True)
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

        # Announce winners
        if len(winners) > 1:
            print(f"{Fore.CYAN}It's a tie! The winners are: {', '.join(winners)} with {max_score} points each!{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.CYAN}The winner is {winners[0]} with {max_score} points!{Style.RESET_ALL}\n")
