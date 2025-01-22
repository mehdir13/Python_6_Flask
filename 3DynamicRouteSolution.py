### 3. Dynamic Route with Parameter Parsing

# Implement a dynamic route that takes a parameter from the URL.
# - Create a route `/greet/<username>`, where `<username>` is a dynamic segment.
# - When a user visits `/greet/jane`, the response should be `"Hello, Jane!"` (replace "Jane" with any `username` given).
# - Add basic validation: if `username` is empty or contains non-alphabet characters, return a `400` status with `{"error": "Invalid username."}`
# 
# Next, modify the route to accept an optional age query parameter (e.g., `/greet/jane?age=25`) and respond with `"Hello, Jane! You are 25 years old."` _if_ the age parameter is provided.

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/greet/<username>', methods=['GET'])
def greet(username: str):
    if not username.isalpha():
        return jsonify({"error": "Invalid username."}), 400

    age = request.args.get('age')

    # Construct the greeting message: AGE is optional, althoug acceptable: positive integer. 
    if age:
        if not age.isdigit():
            return jsonify({"error": "Age must be a number."}), 400
        return jsonify({"message": f"Hello, {username.capitalize()}! You are {age} years old."})
    else:
        return jsonify({"message": f"Hello, {username.capitalize()}!You are AGE is not revealed to the Matrix !!! "})

if __name__ == '__main__':
    app.run(debug=True)