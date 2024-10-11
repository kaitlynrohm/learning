# Imports
import json
from flask import Flask, jsonify, request

# Create app
app = Flask(__name__)

@app.route("/", methods=["GET"]) #Define route and method
def root(): #Function for route
    return jsonify({"Message": "Root endpoint hit"})

# Run app
if __name__ == "__main__":
    app.run(port=5000)