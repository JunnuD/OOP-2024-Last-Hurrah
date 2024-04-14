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
            f"{Fore.GREEN}{self.name} sai: {attribute} ja {points} pistettä{Style.RESET_ALL}")

    def __str__(self):
        attributes_str = ", ".join(self.attributes)
        return f"{self.name} : {attributes_str}, Pisteet: {self.score}"


class Game:
    def __init__(self):
        num_players = int(input("Anna pelaajien määrä: "))
        self.players = [
            Player(input(f"Anna pelaajan {i+1} nimi: ")) for i in range(num_players)]
        self.dice = [Dice(), Dice()]
        self.attribute_map = {
            2: ("Yllätyskyykkyä", 5),
            3: ("Lämmin käsi", 10),
            4: ("2", 15),
            5: ("3", 20),
            6: ("4", 25),
            7: ("5", 30),
            8: ("6", 35),
            9: ("7", 40),
            10: ("Ylisuuri varvas", 45),
            11: ("3", 50),
            12: ("Jäätävä darra", 55)
        }

    def roll_dices_and_assign_attribute(self, player):
        input(
            f"{Fore.YELLOW}Paina Enter heittääksesi noppaa {player.name}...{Style.RESET_ALL}")
        roll_sum = sum(dice.roll() for dice in self.dice)
        attribute_name, points = self.attribute_map.get(
            roll_sum, ("Ei mitään", 0))
        print(f"{player.name} heitti {roll_sum} ja sai: {attribute_name}.")
        player.add_attribute(attribute_name, points)

    def play_round(self):
        for player in self.players:
            choice = input(
                f"{Fore.BLUE}Haluaako {player.name} heittää noppaa? (Joo/Ei) {Style.RESET_ALL}").strip().lower()
            if choice == 'joo':
                self.roll_dices_and_assign_attribute(player)
            else:
                print(
                    f"{Fore.RED}{player.name} Meni hoitamaan kanoja ja sai salmonellan silmään. {Style.RESET_ALL}")

    def play(self):
        print(f"{Fore.CYAN}Peli alkaa! Kukin pelaaja saa kolme yritystä heittää noppaa.\n{Style.RESET_ALL}")
        for round in range(1, 4):
            print(f"{Fore.MAGENTA}Kierros {round} alkaa:{Style.RESET_ALL}")
            self.play_round()
        print(f"\n{Fore.CYAN}Pelin tulos:{Style.RESET_ALL}")
        headers = ["Pelaaja", "Ominaisuudet", "Pisteet"]
        data = [(player.name, ", ".join(player.attributes), player.score)
                for player in self.players]
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


if __name__ == "__main__":
    game = Game()
    game.play()
