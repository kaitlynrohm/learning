# To start server: python app.py
# Imports
from flask import Flask, jsonify
from routes import init_api

# Create app
app = Flask(__name__)

# Initialise app
init_api(app)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"Message": "Root endpoint hit"})

# Run app
if __name__ == "__main__":
    app.run(port=5000)