import os
import requests
import base64
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

REPO = "Yaroslav-0000/commands"
DATA_FILE = "data.json"

@app.route("/commands", methods=["GET"])
def get_data():
    url = f"https://api.github.com/repos/{REPO}/contents/{DATA_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    return jsonify(json.loads(content))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
