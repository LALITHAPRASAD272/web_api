from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/prasad')
def prasad():

    return jsonify({
        "message":"Welcome To Prasad API",
        "status":"Running",
        "time":str(datetime.now())
    })

@app.route('/prasad/health')
def health():

    return jsonify({
        "status":"Healthy"
    })

if __name__ == "__main__":
    app.run()