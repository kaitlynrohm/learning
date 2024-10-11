# To start server: python app.py
# Imports
import json
from flask import Flask, jsonify, request

# Create app
app = Flask(__name__)

# dummy data
employees = [ { 'id': 1, 'name': 'Ashley' }, { 'id': 2, 'name': 'Kate' }, { 'id': 3, 'name': 'Joe' }]

@app.route("/", methods=["GET"]) #Define route and method
def root(): #Function for route
    return jsonify({"Message": "Root endpoint hit"})

@app.route("/employees", methods=['GET'])
def get_employees():
    return jsonify(employees)

def employee_is_valid(employee):
    for key in employee.keys():
        if key != 'name':
            return False
        return True

@app.route("/employees", methods=["POST"])
def create_employee():
    global nextEmployeeId
    nextEmployeeId = len(employees) + 1
    employee = json.loads(request.data)
    if not employee_is_valid(employee):
        return jsonify({"Error": "Invalid properties."}), 400
    employee['id'] = nextEmployeeId
    # nextEmployeeId += 1
    employees.append(employee)
    return { 'location': f'/employees/{employee["id"]}' }, 201

# Run app
if __name__ == "__main__":
    app.run(port=5000)