from flask import Flask, jsonify
from flask_api import status
from flask_cors import CORS
import simplejson as json

app = Flask(__name__)
app.debug = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

with open("db.json", "r") as f:
    db = json.load(f)

@app.route("/api/comments/posts/<int:id>", methods=['GET'])
def get_comments_post(id):
    data = list(filter(lambda x:x.get("post") == id, db.get("comments")))
    return jsonify(data), status.HTTP_200_OK

@app.route("/api/comments/by-user/<int:user_id>", methods=['GET'])
def get_comments_by_user(user_id):
    data = list(filter(lambda x:x.get("user") == user_id, db.get("comments")))
    return jsonify(data), status.HTTP_200_OK

@app.route("/api/", methods=['GET'])
def api():
    return "API ready to receive requests"

@app.route("/", methods=['GET'])
def index():
    return "Ready to receive requests"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')