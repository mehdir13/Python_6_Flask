# python -m venv venv
# venv/scripts/activate (source ./venv/bin/activate for mac)
# pip install flask
# flask run



from flask import Flask, request

app = Flask(__name__)


# 1. Basic Route Decorator
# Use Case: This is a simple route that displays a welcome message at the root URL.
# It can serve as the homepage of a website or the main endpoint of an API.
@app.route("/")
def home():
    return "Welcome to our API!"  # 200 OK - Standard response for successful requests.


# More commonly you want to return the data in JSON-format.
# A dictionary will be converted into JSON by Flask.
@app.route("/home2")  # You can map multiple routes to one function.
@app.route("/json")
def json_home():
    return {"msg": "Welcome to our API!"}


# How to test in Postman:
# - Set the request method to GET.
# - Enter `localhost:5000/` in the URL field.
# - Press Send. You should see the response "Welcome to our API!".


# 2. Handling Different HTTP Methods
# Use Case: This route demonstrates handling both GET and POST requests on the same endpoint.
# GET can retrieve information, while POST can be used to send new data to the server.
@app.route("/data", methods=["POST"])
def handle_data():
    data = request.json
    # Example for creating a new entry or submitting data
    return {
        "message": "Data received successfully",
        "data": data,
    }

# - For POST: Set the method to POST, enter the same URL, go to the Body tab, select raw and JSON format,
#             enter JSON data like `{"name": "Alice", "age": 25}`, and press Send.
#             You should see a response with "Data received successfully" and the provided data.


# 3. Dynamic Routes
# Use Case: This route takes a dynamic parameter <username> from the URL.
# It could be used to greet a user or retrieve user-specific data.
@app.route("/user/<username>")
def greet_user(username):
    return {"msg": f"Hello, {username}!"}


# How to test in Postman:
# - Set the method to GET.
# - Enter `localhost:5000/user/YourName` in the URL field (replace YourName with any username).
# - Press Send. You should see a response like "Hello, YourName!".


# 4. Parsing the Request Body (essentially the same as 2 but more validation)
# Use Case: This route accepts JSON data in a POST request.
# It could be used to add a new user or handle submitted form data.
@app.route("/user", methods=["POST"])
def add_user():
    # Parse JSON data from the request body
    data = request.json
    name = data.get("name")
    age = data.get("age")
    if not name or not age:
        # 400 Bad Request - Missing required data.
        return {"error": "Name and age are required"}, 400
    # Example for saving user data or processing registration
    return {
        "message": f"User {name}, age {age}, added successfully!"
    }

# How to test in Postman:
# - Set the method to POST.
# - Enter `localhost:5000/user` in the URL field.
# - In the Body tab, select raw and JSON format.
# - Enter JSON data like: {"name": "Alice", "age": 25}
# - Press Send. You should see a response like `{"message": "User Alice, age 25, added successfully!"}`.
# - To test an error, omit the name or age in the JSON data and check for a 400 error.

# 5. Faulty route. This will raise a 500 error, indicating that the server broke.
@app.route("/error")
def error():
    return a

# How to test in Postman:
# - Set the method to GET.
# - Enter `localhost:5000/error` in the URL field.


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
