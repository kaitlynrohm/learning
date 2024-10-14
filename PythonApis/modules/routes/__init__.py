from flask import Blueprint
from .test import test_bp

def init_api(app):
    app.register_blueprint(test_bp)