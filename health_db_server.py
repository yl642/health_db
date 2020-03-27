from flask import Flask, jsonify, request

db = []  # global section

app = Flask(__name__)


if __name__ == '__main__':
    app.run()