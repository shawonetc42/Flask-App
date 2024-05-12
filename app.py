from flask import Flask, jsonify, request
from students import students  # Import students from data.py
from data import data  # Import data from data.py
app = Flask(__name__)

# Define a route for the root endpoint
@app.route('/')
def index():
    return "Welcome to the data API!"

# Define a route for returning the sample data
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

# Define a route for returning the sample data

# Define a route for returning the sample data
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Define a route for returning a specific student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    # Check if the student ID is valid
    if student_id >= 0 and student_id < len(students):
        return jsonify(students[student_id])
    else:
        return jsonify({"error": "Student not found"}), 404

# Define a route for receiving data via POST
@app.route('/students', methods=['POST'])
def receive_student_data():
    # Get the JSON data from the request
    request_data = request.json

    # Process the received data as needed
    # For demonstration purposes, let's just return the received data
    return jsonify(request_data)

if __name__ == '__main__':
    app.run(debug=True)
