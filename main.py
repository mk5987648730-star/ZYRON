
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "success": True,
        "app": "ZYRON API",
        "brand": "ZYRON",
        "developer": "@zyrondev",
        "message": "Welcome to ZYRON"
    })

@app.route("/api/search")
def search():
    number = request.args.get("number", "")

    if not number.isdigit() or len(number) != 10:
        return jsonify({
            "success": False,
            "error": "Enter a valid 10-digit demo number"
        }), 400

    return jsonify({
        "success": True,
        "app": "ZYRON API",
        "brand": "ZYRON",
        "developer": "@zyrondev",
        "query": number,
        "count": 1,
        "results": [{
            "name": "XYZ User",
            "phoneNumber": "XXXXXX" + number[-4:],
            "address": "Dummy Testing Address",
            "source": "test_data"
        }]
    })
