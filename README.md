# Py‑Snake Game 🐍

A classic Snake game built in **Python**, featuring responsive controls, growing snake body, and score tracking. Slide the snake around, eat food, avoid hitting walls or yourself!

---

## Demo / Preview

![Game Preview](game-video.gif)

---

## Table of Contents

- [Features](#features)  
- [Project Structure](#project-structure)  
- [Game Rules](#game-rules)  
- [Installation](#installation)  
- [Running the Game](#running-the-game)  
- [Controls](#controls)  
- [Future Improvements](#future-improvements)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- Snake moves in 4 directions across a grid.  
- Food randomly spawns; eating food increases the snake’s length.  
- Incremental score increases as you eat food.  
- Game Over when snake runs into wall or into itself.  
- Clean, simple visuals using Python.  

---

## Project Structure

```
py-snake-game/
├── main.py           # Main loop and game management  
├── snake.py          # Snake class: movement, growth, collision  
├── food.py           # Food class: spawning food at random positions  
├── scoreboard.py     # Track and display the player’s score  
├── game_video.gif    # Preview / demo GIF  
├── README.md         # This file  
└── .gitignore        # Files/folders to ignore in version control
```

---

## Game Rules

- Use the controls to move the snake: up, down, left, right.  
- Food appears at random spots; each food eaten increases your score by 1 and increases snake length.  
- Hitting a wall (boundary) or the snake itself ends the game.  
- Try to eat as much food as possible without crashing!

---

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/ShaileshLambode/py-snake-game.git
   cd py-snake-game
   ```

2. Make sure you have Python installed (preferably Python 3.6+).  

3. (Optional) If there are any dependencies, install them:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Game

To launch the game, run:

```bash
python main.py
```

Ensure you're in the project directory when running the command.

---

## Controls

- **Up arrow** → move up  
- **Down arrow** → move down  
- **Left arrow** → move left  
- **Right arrow** → move right  

(If supporting WASD or others, list them accordingly.)

---

## Future Improvements

- Add pause / resume functionality.  
- More levels or increased speed over time.  
- Add obstacles in the play area.  
- Save high scores to a file.  
- GUI enhancements (graphics / better visuals).  
- Mobile or touch support.  

---

## Contributing

Contributions are very welcome! 🎉 Here’s how to get involved:

1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature‑name
   ```
3. Make your changes, test thoroughly.  
4. Commit with clear messages.  
5. Push your branch and make a Pull Request.  

---

## License
