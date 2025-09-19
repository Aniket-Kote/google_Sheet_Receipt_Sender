from flask import Flask, request, jsonify

from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for the /send_email endpoint only, adjust origins as needed
CORS(app)

def process_new_entry(entry):
    print("✅ New row detected:", entry)
    # 👉 Your logic here

@app.route('/new_entry', methods=['POST'])
def new_entry():
    data = request.json.get("new_entry")
    process_new_entry(data)
    return jsonify({"status": "received", "data": data}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
