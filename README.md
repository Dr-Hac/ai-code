Overview
This is a simple text-based RPG game where players select a character class, explore various locations, encounter enemies, and use items to survive. The player can perform actions such as attacking enemies, using magic, moving to different locations, and using items to restore health.

The game loop continues until the player is defeated or chooses to quit.

Code Structure
1. Character Classes (CharacterClass Class)
Defines the attributes for different character types that the player can choose.
Attributes:
name: Name of the character class (e.g., "Warrior", "Mage").
health: Initial health points of the character.
attack: Physical attack power.
magic: Magic power, used for spells.
Example Instances:
warrior = CharacterClass("Warrior", 150, 15, 5)
mage = CharacterClass("Mage", 100, 10, 20)
2. Enemies (Enemy Class)
Represents enemies the player encounters in different locations.
Attributes:
name: Name of the enemy (e.g., "Zombie", "Goblin").
health: Health points of the enemy.
attack: Attack power of the enemy.
Example Instances:
zombie = Enemy("Zombie", 80, 8)
werewolf = Enemy("Werewolf", 100, 12)
3. Locations (Location Class)
Represents different areas that the player can explore, each containing unique enemies and items.
Attributes:
name: Name of the location (e.g., "Haunted Forest").
enemies: A list of Enemy instances that the player may encounter.
items: A list of items available in the location.
Example Instances:
haunted_forest = Location("Haunted Forest", [zombie, werewolf], ["Rusty Sword", "Health Potion"])
4. Player (Player Class)
Represents the player character, who can perform actions such as attacking, casting spells, and using items.
Attributes:
character_class: The selected character class for the player (an instance of CharacterClass).
health: Current health of the player, initialized from the selected character class.
inventory: List of items the player has collected.
Methods:
attack(enemy): Performs a physical attack on an enemy, reducing the enemy's health.
use_magic(enemy): Uses magic to deal damage to an enemy if magic points are available.
use_item(item): Allows the player to use items from the inventory, like health potions.
list_inventory(): Lists items in the player's inventory.
5. Game Loop
The game loop provides the main interface for gameplay and keeps the game running.
Player Actions:
attack: Attacks a randomly chosen enemy in the current location.
magic: Uses magic to attack a randomly chosen enemy.
use item: Allows the player to use an item from their inventory.
move: Allows the player to move to a different location.
quit: Exits the game.
Enemy Actions:
Each enemy in the current location attacks the player, reducing their health.
If the player's health reaches zero or below, the game loop ends, and the player is considered defeated.
Example Game Flow
Character Selection:

The player starts by selecting a character class from predefined options: Warrior, Mage, or Rogue.
Exploring Locations:

The player starts in the Haunted Forest and can move to other locations, such as the Enchanted Castle or Bandit's Lair.
Combat:

The player can attack or use magic against enemies.
After each player turn, remaining enemies in the location take turns attacking the player.
Item Use:

The player can use items like Health Potions to restore health.
Game End:

The game ends if the player chooses to quit or if their health reaches zero, resulting in a defeat.
Code Sample Usage
The player can interact with the game via terminal inputs. Here's an example of how a game session might look:

plaintext
Copy code
You are in the Haunted Forest.
You can see the following enemies:
- Zombie (Health: 80)
- Werewolf (Health: 100)
You can see the following items:
- Rusty Sword
- Health Potion

Your health: 150
Choose an action (attack/magic/use item/move/quit): attack
You attack the Zombie, dealing 15 damage!
The Zombie attacks you!
You take 8 damage.
...
Potential Enhancements
Adding Item Pickup: Allow the player to add items found in a location to their inventory.
Expanded Magic and Abilities: Add more complex spell and attack mechanics.
More Win/Lose Conditions: Introduce a final boss or a quest that, when completed, allows the player to win the game.
This documentation covers the structure and general flow of the game, making it easier to understand the codebase and develop further features.