from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)

# Create routes
@app.route('/latest', methods=['GET'])
def getCurrencies():
    return jsonify({"rates":{"CHF":"1.087","PLN":"4.2609","TRY":"6.5834","USD":"1.1075","GBP":"0.85708"},"base":"EUR","date":"2019-12-23"})

# Run server
if __name__ == '__main__':
    app.debug = True
    app.run()
