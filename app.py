from flask import Flask, request

app = Flask(__name__)

def process_new_entry(entry):
    print("✅ New row detected:", entry)
    # 👉 Your logic here

@app.route('/new_entry', methods=['POST'])
def new_entry():
    data = request.json.get("new_entry")
    process_new_entry(data)
    return {"status": "received"}, 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
