from flask import Flask, jsonify

app = Flask(__name__)

list_of_objects = [
	{"id": 1, "name": "Object 1"},
	{"id": 2, "name": "Object 2"},
	{"id": 3, "name": "Object 3"}
]

@app.route("/api/v1/objects")
def index():
    return jsonify(list_of_objects)

if __name__ == "__main__":
    app.run()