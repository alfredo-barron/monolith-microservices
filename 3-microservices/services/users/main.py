from flask import Flask, jsonify, make_response
from flask_api import status
from flask_cors import CORS
import simplejson as json

app = Flask(__name__)
app.debug = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

with open("db.json", "r") as f:
    db = json.load(f)

@app.route("/api/users", methods=['GET'])
def get_users():
    return jsonify(db.get("users")), status.HTTP_200_OK

@app.route("/api/users/<int:id>", methods=['GET'])
def get_user(id):
    data = list(filter(lambda x:x.get("id") == id, db.get("users")))
    return jsonify(data), status.HTTP_200_OK

@app.route("/api/", methods=['GET'])
def api():
    return "API ready to receive requests"

@app.route("/", methods=['GET'])
def index():
    return "Ready to receive requests"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')