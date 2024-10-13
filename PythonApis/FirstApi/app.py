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

@app.route("/employee/<int:id>", methods=["GET"])
def getEmployee_by_id(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({"Error": "Employee does not exist"}), 400
    return jsonify(employee)

def get_employee(id):
    return next((e for e in employees if e['id'] == id), None)

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

@app.route("/employee/<int:id>", methods=["PUT"])
def update_employee(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404
    updated_employee = json.loads(request.data)
    if not employee_is_valid(updated_employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400
    employee.update(updated_employee)
    return jsonify(employee)

@app.route("/employee/<int:id>", methods=["DELETE"])
def delete_employee(id: int):
    global employees
    employee = get_employee(id)
    if employee is None:
        return({"Error": "Employee does not exist"}), 404
    employees = [e for e in employees if e["id"] != id]
    return jsonify(employee), 200

# Run app
if __name__ == "__main__":
    app.run(port=5000)