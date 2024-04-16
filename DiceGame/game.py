import random
from colorama import Fore, Style, init
from tabulate import tabulate

init()  # Initialize colorama for colored console output


class GameEntity:
    """Base class for all game entities."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Dice:
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
        roll = super().roll()  # Call the roll method of the base class
        if roll >= 2:
            print(f"{Fore.RED}Magic dice rolled a six! Double points on this turn!{
                  Style.RESET_ALL}")
            return 12  # Represents doubled value of 6
        return roll


class Player(GameEntity):
    """Class to create a player with a name, list of attributes, and a score."""

    def __init__(self, name):
        super().__init__(name)
        self.attributes = []
        self.score = 0

    def add_attribute(self, attribute, points):
        self.attributes.append(attribute)
        self.score += points
        print(f"{Fore.GREEN}{self.name} got: {attribute} and {
              points} points{Style.RESET_ALL}")

    def __str__(self):
        attributes_str = ", ".join(self.attributes)
        return f"{super().__str__()} : {attributes_str}, Points: {self.score}"


class Game:
    """Represents a dice-rolling game for multiple players, including game attributes and rounds."""

    def __init__(self):
        num_players = int(input("How many players: "))
        self.players = [
            Player(input(f"Give player {i+1} name: ")) for i in range(num_players)]
        # Array of different dice types
        self.dice = [Dice(), LoadedDice(), MagicDice()]
        self.attribute_map = {
            2: ("Alien Attack", 55),
            3: ("Warm Hand", 45),
            4: ("Bees!", 35),
            5: ("Smashed Potatoes", 20),
            6: ("Broken Fishrod", 5),
            7: ("Fell Over", 5),
            8: ("New lecture with Marika about Project Management", 10),
            9: ("Bigfoot Sighting", 20),
            10: ("Surprise Squat", 35),
            11: ("New Porsche", 50),
            12: ("Yo Mama- jokes!", 55),
            # Added for potential high rolls with Magic Dice
            13: ("Lucky Day at Heidi's", 60),
            14: ("Winning Lottery", 65),
            15: ("Found Treasure from pants", 70),
            16: ("Moon Landing", 75),
            17: ("Discovered Atlantis from Aurajoki", 80),
            # Maximum score for double sixes from Magic Dice
            18: ("Time Travel to first year as a Tiko", 100)
        }

    def roll_dices_and_assign_attribute(self, player):
        dice = random.choice(self.dice)  # Randomly select a dice
        roll_sum = dice.roll()  # Roll the selected dice
        attribute_name, points = self.attribute_map.get(
            roll_sum, ("Nothing", 0))
        print(f"{player.name} threw {roll_sum} and got: {attribute_name}.")
        player.add_attribute(attribute_name, points)

    def play_round(self):
        for player in self.players:
            choice = input(f"{Fore.BLUE}Does {
                           player.name} want to throw dice? (Yes/No) {Style.RESET_ALL}").strip().lower()
            if choice == 'yes':
                self.roll_dices_and_assign_attribute(player)
            else:
                print(f"{Fore.RED}{player.name} opted out of rolling the dice.{
                      Style.RESET_ALL}")

    def play(self):
        print(f"{Fore.CYAN}Game is starting! There are three (3) rounds to roll dices!{
              Style.RESET_ALL}")
        for round in range(1, 4):
            print(f"{Fore.MAGENTA}Round {round} starting:{Style.RESET_ALL}")
            self.play_round()
        print(f"\n{Fore.CYAN}Game's Outcome:{Style.RESET_ALL}")
        headers = ["Player", "Attributes", "Points"]
        data = [(player.name, ", ".join(player.attributes), player.score)
                for player in self.players]
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


if __name__ == "__main__":
    game = Game()
    game.play()
