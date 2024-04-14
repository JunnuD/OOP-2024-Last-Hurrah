import random
from colorama import Fore, Style, init
from tabulate import tabulate

init()


class Dice:
    def roll(self):
        return random.randint(1, 6)


class Player:
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
    def __init__(self):
        num_players = int(input("How many players: "))
        self.players = [
            Player(input(f"Give the players {i+1} name: ")) for i in range(num_players)]
        self.dice = [Dice(), Dice()]
        self.attribute_map = {
            2: ("Suprise Squat", 5),
            3: ("Harm Hand", 10),
            4: ("Bees!", 15),
            5: ("Smashed Potatoes", 20),
            6: ("Broken Fishrod", 25),
            7: ("Bigfoot Toe", 30),
            8: ("Fell Over", 35),
            9: ("Marika's Lectures", 40),
            10: ("Alien Attack", 45),
            11: ("New Porsche", 50),
            12: ("Yo Mama!", 55)
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
                    f"{Fore.RED}{player.name} Went to take care of the chickens and got salmonella in his eye {Style.RESET_ALL}")

    def play(self):
        print(f"{Fore.CYAN}Game is starting! Each player gets three (3) tries to roll dice.\n{Style.RESET_ALL}")
        for round in range(1, 4):
            print(f"{Fore.MAGENTA}Round {round} starting:{Style.RESET_ALL}")
            self.play_round()
        print(f"\n{Fore.CYAN}Games Outcome:{Style.RESET_ALL}")
        headers = ["Player", "Attributes", "Points"]
        data = [(player.name, ", ".join(player.attributes), player.score)
                for player in self.players]
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


if __name__ == "__main__":
    game = Game()
    game.play()
