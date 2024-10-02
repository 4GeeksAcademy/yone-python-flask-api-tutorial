from flask import Flask, jsonify, request
#jsonify convierte un diccionario en un string de formato json
app = Flask(__name__)

#Lista
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

#Post
@app.route('/todos', methods=['POST'])
def add_new_todo():

    body = request.json
    print("Incoming request with the following body", body)
    
    if isinstance(body, list):
        todos.extend(body)
    else:
        todos.append(body)
    
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)