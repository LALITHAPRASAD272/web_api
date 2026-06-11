from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():

    return jsonify({
        "message":"Welcome To Prasad API",
        "status":"Running",
        "time":str(datetime.now())
    })

@app.route('/health')
def health():

    return jsonify({
        "status":"Healthy"
    })

if __name__ == "__main__":
    app.run()