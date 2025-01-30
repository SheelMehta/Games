Cows and Bulls Game 🐮🐂
A fun, interactive web-based Cows and Bulls game where you guess a 4-digit number, and the system provides feedback based on your guess.

📌 Features
✅ Random 4-digit number generation (No repeating digits).
✅ Validates user input (Only unique 4-digit numbers allowed).
✅ Provides real-time feedback:

🐮 Cows (Correct digit in the wrong place).
🐂 Bulls (Correct digit in the correct place).
✅ Tracks and displays previous guesses for easy reference.
✅ Clickable number tracker (0-9) to visually mark numbers you've considered.
✅ Automatic game reset after a correct guess.
✅ Minimalist UI with clean styling for better user experience.
🚀 How to Install & Run
Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/SheelMehta/Games.git
cd Games
Step 2: Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate      # For Windows
Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Run the Application
bash
Copy
Edit
python app.py
Step 5: Open in Browser
Go to:
👉 http://127.0.0.1:5000/

🎮 How to Play
The system generates a secret 4-digit number (digits are unique).
You enter a guess in the input box.
Feedback is provided:
🐂 Bulls → Correct digit in the correct position.
🐮 Cows → Correct digit but in the wrong position.
Track used numbers by clicking on the number tracker (0-9) to toggle colors.
Continue guessing until you get all 4 bulls (correct number).
Game resets automatically after a correct guess.
