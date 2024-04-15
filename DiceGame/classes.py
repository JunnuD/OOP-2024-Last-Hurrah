import random
from colorama import Fore, Style, init
from tabulate import tabulate

init()  # Initialize colorama and tabulate


class GameEntity:
    """ Base class for all game entities. Inheritance is utilized in this game to enhance design clarity and scalability. 
        By establishing a 'GameEntity' base class, we lay a foundational framework that future game components can extend. 
        This approach streamlines enhancements and maintenance, demonstrating robust application of object-oriented programming principles.
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Dice:
    """This class represents a 6-sided dice."""

    def roll(self):
        return random.randint(1, 6)


class Player(GameEntity):  # Inherits from GameEntity
    """Class to create a player with name, list of attributes, and score."""

    def __init__(self, name):
        super().__init__(name)
        self.attributes = []
        self.score = 0

    def add_attribute(self, attribute, points):
        self.attributes.append(attribute)
        self.score += points
        print(f"{Fore.GREEN}{self.name} got: {attribute} and {points} points {Style.RESET_ALL}")

    def __str__(self):
        attributes_str = ", ".join(self.attributes)
        return f"{super().__str__()} : {attributes_str}, Points: {self.score}"


class Game:
    """Represents a dice-rolling game for multiple players, including game attributes and rounds."""

    def __init__(self):
        num_players = int(input("How many players: "))
        self.players = [
            Player(input(f"Give player {i+1} name: ")) for i in range(num_players)]
        self.dice = [Dice(), Dice()]
        self.attribute_map = {
            2: ("Alien Attack", 55),
            3: ("Warm Hand", 45),
            4: ("Bees!", 35),
            5: ("Smashed Potatoes", 25),
            6: ("Broken Fishrod", 5),
            7: ("Fell Over", 7),
            8: ("New lecture with Marika about Project Management", 15),
            9: ("Bigfoot Sighting", 23),
            10: ("Suprise Squat", 35),
            11: ("New Porsche", 50),
            12: ("Yo Mama- jokes!", 60)
        }

    def roll_dices_and_assign_attribute(self, player):
        input(f"{Fore.YELLOW}Press Enter to throw dice {player.name}...{Style.RESET_ALL}")
        roll_sum = sum(dice.roll() for dice in self.dice)
        attribute_name, points = self.attribute_map.get(
            roll_sum, ("Nothing", 0))
        print(f"{player.name} threw {roll_sum} and got: {attribute_name}.")
        player.add_attribute(attribute_name, points)

    def play_round(self):
        for player in self.players:
            while True:
                choice = input(f"{Fore.BLUE}Does {player.name} want to throw dice? (Yes/No) {Style.RESET_ALL}").strip().lower()
                if choice == 'yes':
                    self.roll_dices_and_assign_attribute(player)
                    break # Break if answer is valid
                elif choice == 'no':
                    print(f"{Fore.RED}{player.name} Went to take care of the chickens and got salmonella in his eye. Whoops. {Style.RESET_ALL}")
                    break # Break if answer is valid
                else:
                    print(f"{Fore.RED}Invalid input! Please enter 'Yes' or 'No' {Style.RESET_ALL}")

    def play(self):
        print(f"{Fore.CYAN}Game is starting! There are three (3) rounds to roll dices!\nAll players will roll two dices if they want to and the sum of those will give you an attribute which has points!{Style.RESET_ALL}")
        for round in range(1, 4):
            print(f"\n{Fore.MAGENTA}Round {round} starting:{Style.RESET_ALL}")
            self.play_round()

        # Determine the highest score
        max_score = max(player.score for player in self.players)

        # Find all players who have the max score (supports multiple winners in case of a tie)
        winners = [player.name for player in self.players if player.score == max_score]

        # Announce the outcome of the game
        print(f"\n{Fore.CYAN}Games Outcome:{Style.RESET_ALL}")
        headers = ["Player", "Attributes", "Points"]
        data = [(player.name, ", ".join(player.attributes), player.score) for player in self.players]
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

        # Announce winners
        if len(winners) > 1:
            print(f"{Fore.CYAN}It's a tie! The winners are: {', '.join(winners)} with {max_score} points each!{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.CYAN}The winner is {winners[0]} with {max_score} points!{Style.RESET_ALL}\n")
