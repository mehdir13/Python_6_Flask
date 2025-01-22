### 2. GET and POST Requests

# Implement two separate routes to handle `GET` and `POST` requests.
# - Create a route `/info` that only responds to `GET` requests. It should return the message `"Send a POST request with your name and age."`
# - Create another route `/submit` that only accepts `POST` requests. This route should:
# - Parse JSON data from the request body.
# - Expect keys `title` and `year` in the JSON data.
# - Return a message confirming the received information, like `The book is, [title]! And was published in [year]"
# - If `title` or `year` is missing, return a 400 status with a message like `{"error": "Title and year are required."}`


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    return "Send a POST request with your name and age."

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    if not data or 'title' not in data or 'year' not in data:
        return jsonify({"error": "Title and year are required."}), 400
    # case 1: data is empty or unreadable: nor data is TRUE
    # case 2: title is not in data
    # case 3: year is not in data

    title = data['title']
    year = data['year']

    return jsonify({"message": f"The book is '{title}' and was published in {year}."}), 200

if __name__ == '__main__':
    app.run(debug=True)