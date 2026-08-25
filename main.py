from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Success", "message": "My Mobile API is Working!"})

@app.route('/user/<name>', methods=['GET'])
def get_user(name):
    return jsonify({"user": name, "role": "Developer"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
