from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Generate a random 4-digit number with unique digits
def generate_number():
    while True:
        num = str(random.randint(1023, 9876))
        if len(set(num)) == 4:
            return num

answer = generate_number()
guesses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global answer, guesses
    
    user_input = request.json.get('guess')
    if not user_input or len(user_input) != 4 or len(set(user_input)) != 4:
        return jsonify({'error': 'Invalid input. Enter a unique 4-digit number.', 'guesses': guesses})

    cows, bulls = 0, 0
    
    if user_input == answer:
        past_guesses = guesses.copy()  # Store old guesses before reset
        result = f'Congratulations! You guessed the correct number {answer} in {len(guesses) + 1} guesses!'
        past_guesses.append({'guess': user_input, 'feedback': result})  # Append final guess before reset

        answer = generate_number()
        guesses = []  # Reset the game
        return jsonify({'message': result, 'win': True, 'guesses': past_guesses})

    for i in range(4):
        if user_input[i] == answer[i]:
            bulls += 1
        elif user_input[i] in answer:
            cows += 1

    result = f'{cows} cows, {bulls} bulls'
    guesses.append({'guess': user_input, 'feedback': result})
    return jsonify({'message': result, 'win': False, 'guesses': guesses})

if __name__ == '__main__':
    app.run(debug=True)
 