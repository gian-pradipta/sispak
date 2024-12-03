from flask import Flask, request, jsonify
import main
from naive_bayes import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

dataset : list = main.get_dataset()
data = main.seperate_based_on_class(dataset, "dengue")

# Kode di bawah ini digunakan untuk melakukan
# penghapusan data dengan target yes, karena
# data dengan target yes terlalu banyak
for i in range(43):
    data["yes"].pop()

# Route for GET requests
@app.route('/get_example', methods=['GET'])
def get_example():
    # Access query parameters, e.g., /get_example?name=John
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

# Route for POST requests
@app.route('/', methods=['POST'])
def post_example():
    # Access JSON data sent in the request
    new_case = request.get_json()

    result = do_naive_bayes(data, new_case)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
