# To start server: python app.py
# Imports
from flask import Flask, jsonify
# modules import
from PythonApis.Modules.controller import my_module

# Create app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"Message": "Root endpoint hit"})

@app.route("/module")
def module():
    greeting = my_module.greetings("Kay")
    return greeting


# Run app
if __name__ == "__main__":
    app.run(port=5000)