### 1. Basic Route Creation

# Create a Flask route that displays a welcome message.
# - Create a new route `/welcome` that returns the message `"Welcome to the API!"`.
# - Ensure this route only responds to `GET` requests.
# - Add another route `/goodbye` that returns `"Goodbye from the API!"`.

from flask import Flask, request 

app = Flask(__name__)

@app.route("/welcome", methods = ['GET'])
def welcome():
    return "Welcome to the API !"

@app.route("/goodbye", methods = ['GET'])
def godbye():
    return "GOODBYE from the beautiful API !"


if __name__ == '__main__':
    app.run(debug=True)


# How to test in Postman:
# - Set the request method to GET.
# - Enter the Route URL: `localhost:5000/welecome` or "http://127.0.0.1:5000/welcome" in the URL field.
# - Enter the Route URL:`localhost:5000/goodbye` or "http://127.0.0.1:5000/goodbye" in the URL field.
# - Press Send.


# (__name__) : When you create a Flask app with Flask(__name__), 
# it tells Flask to use the current module (or file) as the source of the app’s configurations and resources.

# (__name__) helps Flask locate static files, templates, and allows it to set up error handling properly for the module.
# How __name__ Works:
# When a Python file is run directly (e.g., python myfile.py), Python sets __name__ to "__main__".
# When the same file is imported as a module in another script, __name__ is set to the module’s name instead (like "myfile").