# import random
# from abc import ABC, abstractmethod

# # === 1. Player Class (Encapsulation) ===
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self._health = 100  # Private attribute
#         self.attack_power = 10
#         self.inventory = []
    
#     @property
#     def health(self):
#         return self._health
    
#     @health.setter
#     def health(self, value):
#         if value < 0:
#             self._health = 0
#         elif value > 100:
#             self._health = 100
#         else:
#             self._health = value
    
#     def add_item(self, item):
#         self.inventory.append(item)
#         print(f"You picked up: {item}")

#     def attack(self, monster):
#         damage = random.randint(1, self.attack_power)
#         print(f"You attack the {monster.name} for {damage} damage!")
#         monster.take_damage(damage)

# # === 2. Monster Class (Inheritance + Polymorphism) ===
# class Monster(ABC):
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power
    
#     @abstractmethod
#     def attack(self, player):
#         pass
    
#     def take_damage(self, damage):
#         self.health -= damage
#         if self.health <= 0:
#             print(f"The {self.name} has been defeated!")
#         else:
#             print(f"The {self.name} has {self.health} HP left.")

# # === Different Monster Types (Polymorphism) ===
# class Goblin(Monster):
#     def attack(self, player):
#         damage = random.randint(1, self.attack_power)
#         print(f"The {self.name} stabs you for {damage} damage!")
#         player.health -= damage

# class Dragon(Monster):
#     def attack(self, player):
#         damage = random.randint(5, self.attack_power)
#         print(f"The {self.name} breathes fire for {damage} damage!")
#         player.health -= damage

# # === 3. Room Class (Composition) ===
# class Room:
#     def __init__(self, name):
#         self.name = name
#         self.monster = self._generate_monster()
#         self.item = self._generate_item()
    
#     def _generate_monster(self):
#         if random.random() < 0.7:  # 70% chance of a monster
#             if random.random() < 0.5:
#                 return Goblin("Goblin", 30, 5)
#             else:
#                 return Dragon("Dragon", 80, 15)
#         return None
    
#     def _generate_item(self):
#         items = ["Sword", "Potion", "Shield", "Gold"]
#         return random.choice(items) if random.random() < 0.5 else None
    
#     def explore(self, player):
#         print(f"\nYou enter the {self.name}...")
#         if self.monster:
#             print(f"A wild {self.monster.name} appears!")
#             while self.monster.health > 0 and player.health > 0:
#                 action = input("Do you (a)ttack or (r)un? ").lower()
#                 if action == "a":
#                     player.attack(self.monster)
#                     if self.monster.health > 0:
#                         self.monster.attack(player)
#                 elif action == "r":
#                     print("You flee in terror!")
#                     break
#                 else:
#                     print("Invalid choice!")
#         if self.item and player.health > 0:
#             player.add_item(self.item)
#         return player.health > 0

# # === 4. Game Class (Main Logic) ===
# class Game:
#     def __init__(self):
#         self.player = Player(input("Enter your name: "))
#         self.rooms = [
#             Room("Dark Cave"),
#             Room("Spooky Forest"),
#             Room("Ancient Ruins"),
#             Room("Treasure Chamber")
#         ]
    
#     def start(self):
#         print(f"\nWelcome, {self.player.name}! Your adventure begins...")
#         for room in self.rooms:
#             if not room.explore(self.player):
#                 print("Game Over! You died.")
#                 break
#             print(f"\nHealth: {self.player.health} | Items: {', '.join(self.player.inventory)}")
#         else:
#             print("\nCongratulations! You cleared the dungeon!")

# # === Start the Game ===
# if __name__ == "__main__":
#     game = Game()
#     game.start()

# import random
# from abc import ABC, abstractmethod

# # ===== 1. Hero (Player) ===== (Encapsulation)
# class Hero:
#     def __init__(self, name):
#         self.name = name
#         self._health = 100  # Private attribute
#         self.attack_power = 10
#         self.defense = 5
#         self.level = 1
    
#     @property
#     def health(self):
#         return self._health
    
#     @health.setter
#     def health(self, value):
#         self._health = max(0, value)  # Health never goes below 0
    
#     def level_up(self):
#         self.level += 1
#         self.attack_power += 2
#         self.defense += 1
#         self.health = 100  # Full heal
#         print(f"🌟 {self.name} leveled up to {self.level}! (+2 ATK, +1 DEF)")
    
#     def attack(self, enemy):
#         damage = max(1, self.attack_power - enemy.defense // 2)
#         print(f"⚔️ {self.name} attacks for {damage} damage!")
#         enemy.health -= damage
    
#     def defend(self):
#         self.defense += 2
#         print(f"🛡️ {self.name} braces for impact! (+2 DEF)")
    
#     def use_potion(self):
#         heal = 20
#         self.health += heal
#         print(f"❤️ {self.name} heals for {heal} HP!")

# # ===== 2. Enemy Base Class ===== (Inheritance)
# class Enemy(ABC):
#     def __init__(self, name, health, attack_power, defense):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power
#         self.defense = defense
    
#     @abstractmethod
#     def attack(self, hero):
#         pass

# # ===== 3. Polymorphic Enemies =====
# class FireDragon(Enemy):
#     def attack(self, hero):
#         damage = random.randint(8, 15)
#         print(f"🔥 The {self.name} breathes fire for {damage} damage!")
#         hero.health -= damage

# class IceGoblin(Enemy):
#     def attack(self, hero):
#         damage = random.randint(5, 10)
#         if random.random() < 0.3:  # 30% chance to freeze
#             print(f"❄️ The {self.name} freezes you! (Skip next turn)")
#             return damage, "freeze"
#         else:
#             print(f"🧊 The {self.name} hits you for {damage} damage!")
#             return damage , None

# # ===== 4. Battle System ===== (Composition)
# class BattleSystem:
#     def __init__(self, hero):
#         self.hero = hero
#         self.enemies = [
#             FireDragon("Fire Dragon", 50, 12, 3),
#             IceGoblin("Ice Goblin", 30, 8, 2)
#         ]
    
#     def start_battle(self):
#         print("\n=== BATTLE BEGIN ===")
#         for enemy in self.enemies:
#             print(f"\nA wild {enemy.name} appears!")
#             while enemy.health > 0 and self.hero.health > 0:
#                 print(f"\n{self.hero.name}: HP {self.hero.health} | {enemy.name}: HP {enemy.health}")
#                 choice = input("(A)ttack | (D)efend | (H)eal: ").lower()
                
#                 if choice == "a":
#                     self.hero.attack(enemy)
#                 elif choice == "d":
#                     self.hero.defend()
#                 elif choice == "h":
#                     self.hero.use_potion()
#                 else:
#                     print("Invalid choice!")
#                     continue
                
#                 if enemy.health > 0:
#                     result = enemy.attack(self.hero)
#                     if result and result[1] == "freeze":
#                         print("You're frozen and miss a turn!")
            
#             if self.hero.health <= 0:
#                 print("💀 You died! Game Over.")
#                 return False
            
#             print(f"🎉 You defeated the {enemy.name}!")
#             if random.random() < 0.5:  # 50% chance to level up
#                 self.hero.level_up()
        
#         print("\n=== YOU WIN! ===")
#         return True

# # ===== Start Game =====
# if __name__ == "__main__":
#     name = input("Enter your hero's name: ")
#     hero = Hero(name)
#     battle = BattleSystem(hero)
#     battle.start_battle()

import random
from collections import defaultdict

# === 1. ScrabbleLetter (Inheritance) ===
class ScrabbleLetter(str):
    LETTER_VALUES = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
        'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
        'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
        'Y': 4, 'Z': 10
    }

    def __init__(self, char):
        super().__init__()
        self.value = self.LETTER_VALUES.get(char.upper(), 0)

# === 2. WordValidator (Polymorphism) ===
class WordValidator:
    def __init__(self, word_list):
        self.word_list = word_list
    
    def is_valid(self, word):
        return word.lower() in self.word_list

# === 3. Player (Composition) ===
class Player:
    def __init__(self):
        self.guesses = []
        self.score = 0
    
    def add_guess(self, word, score):
        self.guesses.append((word, score))
        self.score += score

# === 4. WordPieGame (Encapsulation) ===
class WordPieGame:
    def __init__(self):
        self.word_list = self._load_word_list()
        self.validator = WordValidator(self.word_list)
        self.player = Player()
        self.secret_word = self._pick_secret_word()
        self.scrabble_secret = [ScrabbleLetter(c) for c in self.secret_word]
    
    def _load_word_list(self):
        # In a real game, load from a file like "words.txt"
        return ["apple", "brave", "crane", "dwarf", "elbow", "flame", "grape", "happy"]
    
    def _pick_secret_word(self):
        return random.choice(self.word_list).upper()
    
    def calculate_score(self, guess):
        score = 0
        correct_positions = []
        
        # Check for correct letters in correct positions (green tiles)
        for i, (g_char, s_char) in enumerate(zip(guess, self.secret_word)):
            if g_char == s_char:
                score += ScrabbleLetter(g_char).value * 2  # Double points for correct position
                correct_positions.append(i)
        
        # Check for correct letters in wrong positions (yellow tiles)
        remaining_secret = [c for i, c in enumerate(self.secret_word) if i not in correct_positions]
        remaining_guess = [c for i, c in enumerate(guess) if i not in correct_positions]
        
        for char in remaining_guess:
            if char in remaining_secret:
                score += ScrabbleLetter(char).value  # Single points for correct letter
                remaining_secret.remove(char)
        
        return score
    
    def play_round(self, guess):
        guess = guess.upper()
        
        if len(guess) != 5:
            print("Word must be 5 letters!")
            return False
        
        if not self.validator.is_valid(guess):
            print("Not a valid word!")
            return False
        
        score = self.calculate_score(guess)
        self.player.add_guess(guess, score)
        
        print(f"\nGuess: {guess}")
        print(f"Score: {score}")
        print(f"Total Score: {self.player.score}")
        
        if guess == self.secret_word:
            print("\n🎉 You guessed the word! 🎉")
            return True
        
        return False
    
    def give_hint(self):
        hint = random.choice([c for c in self.secret_word if c not in [g[0] for g in self.player.guesses]])
        print(f"💡 Hint: The word contains the letter '{hint}'")

# === Game Loop ===
if __name__ == "__main__":
    game = WordPieGame()
    print("Welcome to WordPie!")
    print("Guess the 5-letter word. Letters have Scrabble-like values.")
    print("Correct letters in the right place = 2x points!")
    
    while True:
        guess = input("\nEnter your guess (or 'hint' for help): ").strip().lower()
        
        if guess == "hint":
            game.give_hint()
            continue
        
        if game.play_round(guess):
            break
        
        if len(game.player.guesses) >= 6:
            print(f"\nGame Over! The word was: {game.secret_word}")
            break