# Hex Game in Python


## 🎯 Project Goal & Description
This project is a **Hex board game**, where two players compete to connect their designated sides of the board. One player must connect the **top and bottom**, while the other connects the **left and right**. The first player to form a continuous path wins.

The game is implemented using the **two_player_games** framework and runs in the **terminal**.

This project was created during the **1st semester** of university.

---

## 🏗️ Class Structure
### **Hex**
- The main class managing the game.
- Facilitates communication with other classes.
- Stores the current game state (HexState).
- Inherits from the `Game` class in the framework.

### **HexState**
- Represents the current game state.
- Stores the board and tracks which player is making a move.
- Responsible for game logic.
- Inherits from the `State` class in the framework.

### **HexMove**
- Represents a move on the board.
- Stores the coordinates of a hex as a tuple `[row, column]`.
- Inherits from the `Move` class in the framework.

### **HexPlayer**
- Represents a player.
- Each player has a unique symbol (a one-character string).
- Stores a `up_down` attribute indicating whether the player connects **top-bottom** (`True`) or **left-right** (`False`).
- Inherits from the `Player` class in the framework.

---

## 🛠️ Installation & Usage
### **Installation**
Clone the repository from:  
🔗 `https://github.com/Alveaenerle/Hex-Game-Project.git`

### **Running the Game**
Run `main.py` to start the game:
- **Windows:** `python main.py`
- **Linux:** `python3 main.py`

Make sure you are inside the **Hex** project folder before running the script.

### **How to Play**
1. Each player enters a **unique one-character symbol**.
2. The game prompts for the **board size** (from 1 to 26).
3. Players take turns placing pieces by entering **coordinates**:
   - **Column (Letter), Row (Number)** (e.g., `C5`).
4. The game continues until one player forms a **winning path**.

---

## 📝 Reflection
Using a **framework** significantly streamlined the development process. 
However, two major challenges emerged:

1. **Efficient Board Representation:**
   - The board is stored as a **list of lists**, where each sublist represents a **column**.
   - Since the board consists of **hexagons**, structuring it this way allows for efficient handling.
   - If a cell is occupied by a player, it is marked with their symbol.

2. **Determining the Winner:**
   - Implemented using the **BFS (Breadth-First Search) algorithm**.
   - Chosen for its **efficiency** and **ease of understanding**.

### ❌ Unimplemented Features
- **Graphical User Interface (GUI) - in progress:**
  - Due to the **variable board size**, a GUI would be time-consuming to implement.
  - The framework is designed for **terminal-based** gameplay.

- **Single-Player Mode (AI) - in progress:**
  - Implementing an AI capable of defeating a human player is a **complex challenge**.

---

