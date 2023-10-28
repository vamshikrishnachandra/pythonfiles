# Import necessary libraries
from flask import Flask, request, render_template, jsonify
import random

# Create a Flask application
app = Flask(__name__)

# Sample questions and answers
qa_pairs = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Which gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"}
]

# Function to generate a random question
def generate_random_question():
    return random.choice(qa_pairs)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to get a random question
@app.route('/get_question', methods=['GET'])
def get_question():
    random_qa = generate_random_question()
    return jsonify(random_qa)

if __name__ == '__main__':
    app.run(debug=True)
