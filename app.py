from flask import Flask,jsonify,request, render_template
import json
app = Flask(__name__)

def getAllTodos():
 with open("db.json") as file:
    return json.load(file)

    
def addTodo(data):
     with open("db.json", "w") as file:
         json.dump( data, file, indent=4)
         

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def createTodo():
    body = request.json
    data = getAllTodos()
    test ={
        "id": len(data)+ 1,                                       #len      = lenth    id change hote 1, 2 .....
        "task": body["task"]
    }
    data.append(test)
    addTodo(data)
    return "todo create Success"

@app.route("/read", methods=["GET"])
def readTodo():
    data= getAllTodos()
    return jsonify(data)

@app.route("/update/<int:tid>", methods=["PUT"])
def updateTodo(tid): 
    data = request.json
    allTodos = getAllTodos()
    todos = []
    for item in allTodos:
        if item["id"] == tid:
            item["task"] = data["task"]
        todos.append(item)
    addTodo(todos)
    # print(tid)
    # print(data)
    return "todo update success"


@app.route("/remove/<int:tid>", methods=["DELETE"])                      #<int: tid>      dinamik id              kiti number cha = tid use kartat
def reamoveTodo(tid):
    data = getAllTodos()
    todos = []
    for item in data :
        if item["id"] != tid:
            todos.append(item)
    
    addTodo(todos)
    return "todo remove success"


if __name__ == "__main__":
    app.run(debug=True)