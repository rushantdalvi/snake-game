# 🐍 Snake Game (Pygame)
A classic Snake Game built using **Python** and **Pygame**. Control the snake, eat food to increase your score, avoid colliding with yourself or the walls, and try to beat the high score.


## 🎮 Features
- Classic Snake gameplay
- High score saved in a text file
- Background image support
- Background music
- Game over sound effect
- Restart game without closing the application
- Smooth movement with keyboard controls


## 🛠 Requirements
- Python 3.8+
- Pygame

## 📦 Installation

Install **Pygame** using **pip**:

```bash
pip install pygame
```

**OR**

```bash
pip install pygame-ce
```


## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/rushantdalvi/snake-game.git
   ```

2. Move into the project folder:
   ```bash
   cd snake-game
   ```

3. Run the game:
   ```bash
   python main.py
   ```


## 🎯 Controls

- ⬆️ **Up Arrow** – Move Up
- ⬇️ **Down Arrow** – Move Down
- ⬅️ **Left Arrow** – Move Left
- ➡️ **Right Arrow** – Move Right
- **Space** – Start Game
- **Enter** – Restart after Game Over
- **Q** – Increase score by 10 *(Debug Shortcut)*


## 📷 Gameplay
The objective is simple:
- Eat the red food blocks to grow longer.
- Every food gives **10 points**.
- Avoid hitting the screen boundaries.
- Avoid colliding with your own body.
- Beat your previous high score.


## 🏆 High Score

The game automatically creates a file named:

```text
hiscore.txt
```

This file stores the highest score achieved and is updated automatically whenever a new high score is set.

Your highest score is stored in this file and loaded every time the game starts.


## 🎵 Assets Required
Place the following files in the project directory:
- `snake.jpg` – Background image
- `background.mp3` – Background music
- `gameover.mp3` – Game over sound


## 📷 Screenshots
<img width="913" height="644" alt="image" src="https://github.com/user-attachments/assets/204e2e4a-d5b1-4270-b7ab-9e0606c260a7" />
<img width="912" height="637" alt="Screenshot (165)" src="https://github.com/user-attachments/assets/471d91da-0b5f-49b8-b82b-5679a7f5ad5f" />

