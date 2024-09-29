from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

restaurants = [
    "McDonald's",
    "Burger King",
    "Subway",
    "KFC",
    "Starbucks",
    "Pizza Hut",
    "Taco Bell",
    "Wendy's",
    "Dunkin' Donuts",
    "Domino's Pizza"
]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_restaurant', methods=['POST'])
def get_restaurant():
    random_restaurant = random.choice(restaurants)
    return jsonify({'restaurant': random_restaurant})

if __name__ == '__main__':
    app.run(debug=False)
