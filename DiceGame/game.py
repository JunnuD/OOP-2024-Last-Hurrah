"""
Object Oriented Programming 2024 - Last Hurrah - Dice Game
Authors: Junnu Danhammer & Aarni Kaartokallio

This Python program implements a dice-rolling game designed by amazing authors.
The game supports multiple players who compete over three rounds to collect points and attributes based on dice rolls.
Players roll two dice and can earn various attributes with corresponding points based on the sum of the dice.
Attributes range from 'Alien Attack' to 'Yo Mama- jokes!', with points reflecting the rarity or commonality of the attribute.
The game utilizes the 'colorama' library for colored terminal text and 'tabulate' for displaying tabulated game outcomes.

"""
from classes import Player, Dice, Game

if __name__ == "__main__":  # Start the program
    game = Game()
    game.play()
