# Pokémon Game

This repository contains a simple terminal-based Pokémon RPG game developed as part of a **bonus project** from the **Pentest: From Zero to Professional** course by **Solyd**. The game is a fun, interactive way to explore Python programming through a text-based Pokémon adventure.

## Table of Contents
1. [Introduction](#introduction)
2. [Game Structure](#game-structure)
    - 2.1. [Main Files](#main-files)
    - 2.2. [Classes](#classes)
3. [Game Mechanics](#game-mechanics)
    - 3.1. [Choosing a Starter Pokémon](#choosing-a-starter-pokémon)
    - 3.2. [Battles](#battles)
    - 3.3. [Exploration](#exploration)
    - 3.4. [Save System](#save-system)
4. [References and Classes](#references-and-classes)
    - 4.1. [Pokémon Classes](#pokémon-classes)
    - 4.2. [Person Classes](#person-classes)
    - 4.3. [Enemies](#enemies)
5. [Available Commands in the Game](#available-commands-in-the-game)
6. [Final Considerations](#final-considerations)

---

## 1. Introduction
This terminal-based Pokémon game is a bonus project from the **Pentest: From Zero to Professional** course by **Solyd**. The game simulates a simple RPG where players can capture Pokémon, battle enemies, and explore the world in search of new adventures.

## 2. Game Structure

### 2.1. Main Files
- **`pokemon.py`**: Defines the Pokémon classes, their attributes, and battle mechanics.
- **`pessoa.py`**: Defines the player, enemy, and NPC classes, as well as interactions like battles and capturing Pokémon.
- **`main.py`**: Handles the core game loop, Pokémon selection, exploration, and saving/loading the game state.

### 2.2. Classes
- **Pokémon**: The base class for all Pokémon, handling their attributes and attacks.
- **Person**: Represents any person in the game, including the player and enemies.
- **Player**: Inherits from `Person` and represents the player's character in the game.
- **Enemy**: Represents non-playable characters controlled by the game, which the player battles against.

---

## 3. Game Mechanics

### 3.1. Choosing a Starter Pokémon
At the start of the game, the player is prompted to choose their first Pokémon:
- **Pikachu** (Electric Type)
- **Charmander** (Fire Type)
- **Squirtle** (Water Type)

The chosen Pokémon is added to the player's team.

### 3.2. Battles
Battles are turn-based and occur between the player's Pokémon and enemy Pokémon. Each Pokémon can attack based on their type (Electric, Fire, or Water). The player wins by reducing the opponent's HP to zero, earning money after each victory.

### 3.3. Exploration
The player can explore the world and has a random chance of encountering wild Pokémon. The player can choose to battle and try to capture these wild Pokémon.

### 3.4. Save System
The game includes a save and load feature that allows players to store their progress and continue playing later. The game state is saved in a local file (`database.db`) using Python's `pickle` module.

---

## 4. References and Classes

### 4.1. Pokémon Classes
Each Pokémon has:
- **Level**: Determines its strength and HP.
- **HP (Health Points)**: Calculated based on level (`HP = level * 10`).
- **Attack Power**: Based on level (`Attack Power = level * 5`).

Types of Pokémon:
- **Electric Pokémon**: Such as Pikachu.
- **Fire Pokémon**: Such as Charmander.
- **Water Pokémon**: Such as Squirtle.

### 4.2. Person Classes
- **Person**: The base class for people in the game, such as the player and enemies.
- **Player**: The playable character who can capture Pokémon and battle enemies.
- **Enemy**: Characters controlled by the game that challenge the player to battles.

### 4.3. Enemies
Enemies are randomly generated with a list of Pokémon. They may have 1 to 6 Pokémon with varying levels and types.

---

## 5. Available Commands in the Game
The game provides several interactive options:
1. **Explore**: Search the world for wild Pokémon.
2. **Battle an Enemy**: Engage in a battle with a randomly generated opponent.
3. **View Pokémon Roster**: Check the list of captured Pokémon.
0. **Exit the Game**: Save progress and exit the game.

---

## 6. Final Considerations
This Pokémon game is a fun and simple text-based RPG built to apply Python programming skills in a gaming context. As part of the **Pentest: From Zero to Professional** course by **Solyd**, this project offers an enjoyable way to enhance coding knowledge, featuring a save system, battle mechanics, and a growing roster of Pokémon to capture.

Feel free to expand the game by adding more Pokémon types, battle features, and new mechanics!

