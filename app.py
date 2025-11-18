from flask import Flask, request, jsonify

app = Flask(__name__)


users = {
    1: {"id": 1, "name": "Sandhya", "email": "sandhya@gmail.com"},
    2: {"id": 2, "name": "Kiran", "email": "kiran@gmail.com"}
}


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200



@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200



@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    
    if "name" not in data or "email" not in data:
        return jsonify({"error": "name and email are required"}), 400

    new_id = max(users.keys()) + 1 if users else 1
    user = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"]
    }

    users[new_id] = user
    return jsonify(user), 201



@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()

    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])

    return jsonify(users[user_id]), 200



@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted}), 200


if __name__ == "__main__":
    app.run(debug=True)
