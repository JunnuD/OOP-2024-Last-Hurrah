import random
from colorama import Fore, Style, init
from tabulate import tabulate

init()


class Dice:  # This Class represent a 6-sided dice
    def roll(self):
        """Simulating the dice roll and returning a value from 1-6"""
        return random.randint(1, 6)


class Player:  # This Class creates the Player which has a name, list of attributes and the score
    def __init__(self, name):
        self.name = name
        self.attributes = []
        self.score = 0

    def add_attribute(self, attribute, points):
        self.attributes.append(attribute)
        self.score += points
        print(
            f"{Fore.GREEN}{self.name} got: {attribute} and {points} points {Style.RESET_ALL}")

    def __str__(self):
        attributes_str = ", ".join(self.attributes)
        return f"{self.name} : {attributes_str}, Points: {self.score}"


class Game:
    """Represents a dice-rolling game for multiple players, including game attributes and rounds."""

    def __init__(self):
        num_players = int(input("How many players: "))
        self.players = [
            # Make sure the amount of players wanted will come
            Player(input(f"Give the players {i+1} name: ")) for i in range(num_players)]
        # Each player has two dices to throw and three rounds in total
        self.dice = [Dice(), Dice()]
        self.attribute_map = {
            2: ("Alien Attack", 55),    # Here is the attribute - point list
            # If the double dice roll is quite common you will get an common attribute and not so many points
            3: ("Warm Hand", 45),
            # If the double dice roll is more unique you will score larger points and get more rare attributes
            4: ("Bees!", 35),
            5: ("Smashed Potatoes", 20),
            6: ("Broken Fishrod", 5),
            7: ("Fell Over", 5),
            8: ("New lecture with Marika about Project Management", 10),
            9: ("Bigfoot Sighting", 20),
            10: ("Suprise Squat", 35),
            11: ("New Porsche", 50),
            12: ("Yo Mama- jokes!", 55)
        }

    def roll_dices_and_assign_attribute(self, player):
        input(
            f"{Fore.YELLOW}Press Enter to throw dice {player.name}...{Style.RESET_ALL}")
        roll_sum = sum(dice.roll() for dice in self.dice)
        attribute_name, points = self.attribute_map.get(
            roll_sum, ("Nothing", 0))
        print(f"{player.name} threw {roll_sum} and got: {attribute_name}.")
        player.add_attribute(attribute_name, points)

    def play_round(self):
        for player in self.players:
            choice = input(
                f"{Fore.BLUE}Does {player.name} want to throw dice? (Yes/No) {Style.RESET_ALL}").strip().lower()
            if choice == 'yes':
                self.roll_dices_and_assign_attribute(player)
            else:
                print(
                    f"{Fore.RED}{player.name} Went to take care of the chickens and got salmonella in his eye. Whoops. {Style.RESET_ALL}")

    def play(self):  # Play the game!
        print(f"{Fore.CYAN}Game is starting! There is three (3) rounds to roll dices!.\n{
              Style.RESET_ALL}")
        for round in range(1, 4):
            print(f"{Fore.MAGENTA}Round {round} starting:{Style.RESET_ALL}")
            self.play_round()
        print(f"\n{Fore.CYAN}Games Outcome:{Style.RESET_ALL}")
        headers = ["Player", "Attributes", "Points"]
        data = [(player.name, ", ".join(player.attributes), player.score)
                for player in self.players]
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
