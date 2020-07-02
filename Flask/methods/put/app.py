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

def result(error, error_description, data):
    value = {
        "error": error,
        "error_description": error_description,
        "data": data
    }
    return value


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/api/frameworks/", methods=["GET"])
def get_frameworks():
    return result(False, "", frameworks)


@app.route("/api/frameworks/<int:id>", methods=["GET"])
def get_frameworks_by_id(id):
    framework = []
    for item in frameworks:
        if item["id"] == id:
            framework.append(item)
    
    if len(framework)>0:
        return result(False, "", framework[0])
    else:
        return result(True, "Id '" + str(id) + "' not found.", "")


@app.route("/api/frameworks/<string:name>", methods=["GET"])
def get_frameworks_by_name(name):
    framework = []
    for item in frameworks:
        if item["name"] == name:
            framework.append(item)
    
    if len(framework)>0:
        return result(False, "", framework[0])
    else:
        return result(True, "Name '" + name + "' not found.", "")


@app.route("/api/frameworks/", methods=["POST"])
def add_framework():
    if 'id' in request.json and 'name' in request.json: #'id' and 'name' params are required
        
        id = int(request.json["id"])

        #check if id exists
        framework = [item for item in frameworks if item["id"]==id]
        if len(framework)==0:        
            framework = {
                "id": id,
                "name": request.json["name"]
            }
            frameworks.append(framework)
            return result(False, "", frameworks)
        else:
            return result(True, "Id '" + str(id) + "' duplicated.", "")


@app.route("/api/frameworks/<int:id>", methods=["PUT"])
def edit_framework(id):
    framework = [item for item in frameworks if item["id"]==id]

    if len(framework)>0: #if exists id
        if 'id' in request.json: #'id' param is optional
            id = int(request.json["id"])
        
        if 'name' in request.json: #'name' param is required
            framework[0]["id"] = id
            framework[0]["name"] = request.json["name"]
        
        return result(False, "", frameworks)
    else:
        return result(True, "Id '" + str(id) + "' not found.", "")


if __name__ == "__main__":
    app.run(debug=True) #update changes automatically