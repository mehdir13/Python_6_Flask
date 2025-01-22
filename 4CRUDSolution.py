### 4. CRUD Operations Simulation

# Simulate basic CRUD (Create, read, update and delete) operations for a collection of "users".
 
# - Create a list `users` to store user records in the format `{"id": int, "name": str, "favorite_color": str}`.
# For example users = [{"id": 1, "name": "Alice", "favorite_color": "Blue"}, {"id": 2, "name": "Bob", "favorite_color": "Red"}]
# - Implement the following routes:
# 1. `GET /users`: Return the full list of users.
# 2. `POST /users`: Accept JSON data with `name` and `favorite_color`, assign a unique `id` to each new user, and add them to the `users` list. Return the new user data.
# 3. `GET /users/<user_id>`: Return the user data for the specified `user_id`. If not found, return a `404` error.
# 4. `PUT /users/<user_id>`: Accept JSON data to update the name and/or age of the user with the given `user_id`. Return the updated user data.
# 5. `DELETE /users/<user_id>`: Remove the user with the specified `user_id` and return a confirmation message.

# - **Challenge**: Add validation to prevent duplicate names in the list and return a `409 Conflict` status if a user with the same name already exists.


from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "favorite_color": "Blue"},
    {"id": 2, "name": "Bob", "favorite_color": "Red"},
    {"id": 3, "name": "Alan", "favorite_color": "Green"},
    {"id": 4, "name": "Lawrence", "favorite_color": "White"},
    {"id": 5, "name": "Sean", "favorite_color": "Yellow"}
]

# unique ID generator for each new user added to the users list
# Will be used while creating new user in 2. POST/users
def get_next_id():
    if users:
        return max(user["id"] for user in users) + 1
    # IF the users list is not empty, the MAX function iterates through the list and finds the highest ID among the current USERS;
    # then the added user ID will be tha highest current ID + 1.
    # Else the list is empty and therefore the newly added ID will be 1:
    else:
        return 1

# 1. GET /users: Return the full list of users
# In JSON format &  HTTP status code indicating that the request was processed successfully.
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# 2. POST /users: Add a new user
# Accept JSON data assign a unique ID, add them to the `users` list. Return the new user data.
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Validate incoming data
    if not data or 'name' not in data or 'favorite_color' not in data:
        return jsonify({"error": "Name and favorite_color are required."}), 400
    
    # Validation to prevent duplication
    if any(user['name'] == data['name'] for user in users):
        return jsonify({"error": "A user with this name already exists."}), 409
    # The any() function evaluates each element in the iterable:
    # a quick and efficient way to check if at least one condition in a series of checks is met.

    # Create a new user and add to the users list.
    new_user = {
        "id": get_next_id(),
        "name": data['name'],
        "favorite_color": data['favorite_color']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# 3. GET /users/<user_id>: Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found."}), 404
    return jsonify(user), 200
# The next() function is used to get the first item from the generator expression.
# If a matching user is found, next() returns that user object. JESONIFYs it and data status 200 will be returend to shoe the process is completed.
# If no match is found (the generator doesn’t yield any results), next() returns the default value None,
# That is why we should specify the default None as the second argument.

# 4. PUT /users/<user_id>: Update user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    # GET user by ID (exactly like the above part)
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found."}), 404

    # Update user's info in case user is not None, it exits in the list 'users'.
    if 'name' in data:
        user['name'] = data['name']
    if 'favorite_color' in data:
        user['favorite_color'] = data['favorite_color']
    
    return jsonify(user), 200

# 5. DELETE /users/<user_id>: Delete user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    # The users list being defined at a global scope within the Flask application;
    # This means the users list is accessible throughout the whole application, including inside any route functions.
    # 'users' lit is defined outside of any functions or classes, henceforeis a global variable.
    # However, in order to modify the global variabel, we need to declare it as global within the function where we make changes.

    # firstly a quick check to see the user ID virtually exits in the users list:
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found."}), 404
    
    # Remove user from the list
    # Actually what is happening is a lit comrehension of the list 'uers' with all the users in it except the one whose ID is named to be deleted.
    # Technically we are not deleting a member of the list, but re-writing the list and meanwhile excluding the desired ID.
    # It is like filtering out a memeber and re-assigning the list globally.  
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": f"User with ID {user_id} deleted."}), 200
# The original list is perished and the new one which has already been filtered out of the "deleted" member will be over-written upon it.

if __name__ == '__main__':
    app.run(debug=True)
