📌 Link:   https://drive.google.com/file/d/179Xjhm9Rv_xMNaWEjdWKJZA7M0bBFFOv/view?usp=sharing

# 🎮 Child Safety Game

A fun and interactive child safety game built using **Python**, combining the power of **Ursina** and **Pygame**.  
Players select a character, dress them, and explore safe and unsafe scenarios in a playful environment.

---

## 📌 Purpose

To build a game that helps kids learn basic safety rules through visual, hands-on interaction and engaging gameplay.

---

## 🌟 Impact

- Makes safety education fun and relatable  
- Encourages children to think before they act  
- Promotes awareness through interactive scenes and characters

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Ursina Engine** – for UI and character selection screens  
- **Pygame** – for gameplay, navigation, and background scrolling  
- **Pillow** – for image handling  
- **Custom assets** – textures, backgrounds, characters, clothing

---

## 🧩 Features

- Start screen with animated "Start Game" button  
- Character selection (boy/girl)  
- Dress-up screen with clothes and shoes  
- Timed switch between Ursina and Pygame views  
- Scenario selection and side-scrolling gameplay  
- Playground interaction logic  
- Modular structure for future scenes like school, park, etc.

---

## 🧠 Learning Outcomes

- Learned how to integrate multiple game frameworks  
- Improved UI/UX logic using Python  
- Built animations, button interactions, and timed transitions  
- Structured the game flow across different screens and modules  
- Practiced clean code and asset management

---

## 📁 Project Structure

📦 GameWithUrsina/
├── final.py                  # Main game launcher
├── ballonGame.py            # Balloon shooter subgame
├── assets/
│   ├── environments/        # Backgrounds, UI scenes
│   ├── characters/          # Boy/Girl models
│   ├── cloths/              # Clothing textures
│   └── shoes/               # Shoe options
├── .venv/                   # Virtual environment
├── README.md                # Project overview


## ✅ How to Run

1. Clone the repo  
2. Create a virtual environment:
   bash
   python -m venv .venv

3. Activate the environment:

   * Windows: `.\.venv\Scripts\activate`
   * Linux/Mac: `source .venv/bin/activate`
4. Install dependencies:

   bash
   pip install -r requirements.txt
5. Run the game:

   bash
   python wholeGame.py
