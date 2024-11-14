"""
NAME: ai-code-human.py
DESCRIPTION: is a simple cli game
DATE: 11/13/24
PROGRAMMERS: Claude 3, ChatGPT 4o mini
"""


import random

# Character classes
class CharacterClass:
    # initializes character class variables
    def __init__(self, name, health, attack, magic):
        self.name = name
        self.health = health
        self.attack = attack
        self.magic = magic

# creates 3 players classes with defined variables
warrior = CharacterClass("Warrior", 150, 15, 5)
mage = CharacterClass("Mage", 100, 10, 20)
rogue = CharacterClass("Rogue", 120, 12, 8)

# Game world and story
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Location:
    def __init__(self, name, enemies, items):
        self.name = name
        self.enemies = enemies
        self.items = items

# creates three locations and initializes enemy classes within the location initialization
haunted_forest = Location("Haunted Forest", [Enemy("Zombie", 80, 8), Enemy("Werewolf", 100, 12)], ["Rusty Sword", "Health Potion"])
enchanted_castle = Location("Enchanted Castle", [Enemy("Goblin", 60, 6), Enemy("Wizard", 90, 15)], ["Magic Staff", "Enchanted Cloak"])
bandit_lair = Location("Bandit's Lair", [Enemy("Bandit", 75, 10), Enemy("Bandit Leader", 120, 15)], ["Dagger", "Gold Coins"])

# sets a current location
current_location = haunted_forest

# Player character
# defines set of actions the player can take within the game
class Player:
    def __init__(self, character_class):
        self.character_class = character_class
        self.health = character_class.health
        self.inventory = []

    def attack(self, enemy):
        damage = self.character_class.attack
        print(f"You attack the {enemy.name}, dealing {damage} damage!")
        enemy.health -= damage

    def use_magic(self, enemy):
        if self.character_class.magic > 0:
            damage = self.character_class.magic
            print(f"You cast a spell, dealing {damage} damage to the {enemy.name}!")
            enemy.health -= damage
            self.character_class.magic -= 1
        else:
            print("You don't have enough magic power.")

    def use_item(self, item):
        if item == "Health Potion":
            self.health = min(self.health + 30, self.character_class.health)
            print("You use a Health Potion and restore some health.")
            self.inventory.remove(item)
        else:
            print(f"You can't use the {item}.")

    def list_inventory(self):
        print("Your inventory:")
        for item in self.inventory:
            print("- " + item)

# sets player class based on above variables
player = Player(warrior)

# Game loop
while True:
    # Location description
    print(f"\nYou are in the {current_location.name}.")
    print("You can see the following enemies:")
    for enemy in current_location.enemies:
        print(f"- {enemy.name} (Health: {enemy.health})")
    print("You can see the following items:")
    for item in current_location.items:
        print("- " + item)

    # Player's turn
    print(f"\nYour health: {player.health}")
    action = input("Choose an action (attack/magic/use item/move/quit): ")

    if action == "attack":
        enemy = random.choice(current_location.enemies)
        player.attack(enemy)
        if enemy.health <= 0:
            print(f"You defeated the {enemy.name}!")
            current_location.enemies.remove(enemy)
    elif action == "magic":
        enemy = random.choice(current_location.enemies)
        player.use_magic(enemy)
    elif action == "use item":
        player.list_inventory()
        item = input("Choose an item to use: ")
        player.use_item(item)
    elif action == "move":
        destination = input("Where do you want to go? (Haunted Forest/Enchanted Castle/Bandit's Lair) ")
        if destination == "Haunted Forest":
            current_location = haunted_forest
        elif destination == "Enchanted Castle":
            current_location = enchanted_castle
        elif destination == "Bandit's Lair":
            current_location = bandit_lair
        else:
            print("Invalid destination.")
    elif action == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid action. Please try again.")

    # Enemy's turn
    for enemy in current_location.enemies:
        print(f"\nThe {enemy.name} attacks you!")
        player.health -= enemy.attack
        print(f"You take {enemy.attack} damage.")

        # Check if player's health is zero or below
        if player.health <= 0:
            print("You have been defeated.")
            break  # Exit the enemy loop if player is defeated

    # Exit the game loop if player is defeated
    if player.health <= 0:
        break