from flask import Flask, jsonify, request

app = Flask(__name__)

frameworks = [
    {
        "id": 1,
        "name": "Flask"
    },
    {
        "id": 2,
        "name": "ExpressJS"
    },
    {
        "id": 3,
        "name": "Laravel"
    }
]

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/api/frameworks/", methods=["GET"]) #GET method by default. It isn't necessary.
def get_frameworks():
    return jsonify(frameworks)

@app.route("/api/frameworks/<int:id>") #recommended specify type of variable
def get_frameworks_by_id(id):
    framework = []
    for item in frameworks:
        if item["id"] == id:
            framework.append(item)
    
    if len(framework)>0:
        return jsonify(framework[0])
    else:
        return jsonify("")

@app.route("/api/frameworks/<string:name>") #recommended specify type of variable
def get_frameworks_by_name(name):
    framework = []
    for item in frameworks:
        if item["name"] == name:
            framework.append(item)
    
    if len(framework)>0:
        return jsonify(framework[0])
    else:
        return jsonify("")

@app.route("/api/frameworks/", methods=["POST"])
def add_framework():
    if 'id' in request.json and 'name' in request.json:    
        framework = {
            "id": request.json["id"],
            "name": request.json["name"]
        }
        if framework:
            frameworks.append(framework)

    return jsonify(frameworks)

if __name__ == "__main__":
    app.run(debug=True) #update changes automatically