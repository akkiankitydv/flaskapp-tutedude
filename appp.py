from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.items

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()
    item_name = data.get('itemName')
    item_description = data.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({'message': 'Missing data'}), 400

    collection.insert_one({
        'itemName': item_name,
        'itemDescription': item_description
    })

    return jsonify({'message': 'Item saved successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
