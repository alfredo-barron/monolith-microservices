from flask import Flask, jsonify, make_response
from flask_api import status
from flask_cors import CORS
import simplejson as json

app = Flask(__name__)
app.debug = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

with open("db.json", "r") as f:
    db = json.load(f)

@app.route("/api/posts", methods=['GET'])
def get_posts():
    return jsonify(db.get("posts")), status.HTTP_200_OK

@app.route("/api/posts/<int:id>", methods=['GET'])
def get_post(id):
    data = list(filter(lambda x:x.get("id") == id, db.get("posts")))
    return jsonify(data), status.HTTP_200_OK

@app.route("/api/posts/by-user/<int:user_id>", methods=['GET'])
def get_post_by_user(user_id):
    data = list(filter(lambda x:x.get("createdBy") == user_id, db.get("posts")))
    return jsonify(data), status.HTTP_200_OK

@app.route("/api/", methods=['GET'])
def api():
    return "API ready to receive requests"

@app.route("/", methods=['GET'])
def index():
    return "Ready to receive requests"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')