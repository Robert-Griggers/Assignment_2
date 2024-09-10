from flask import Flask, g


def create_app():
    app = Flask(__name__)
    return app