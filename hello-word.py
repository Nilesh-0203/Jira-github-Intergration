from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'])
def createJIRA():
    data = request.json  # Extract webhook payload

    # Safely extract the comment body
    comment_body = data.get("comment", {}).get("body", "").strip()
    print(f"Received GitHub comment: {comment_body}")

    if comment_body == "/jira":
        print("Trigger matched: Creating Jira ticket...")

        url = ""

        API_TOKEN = ""
        auth = HTTPBasicAuth("email@gmail.com", API_TOKEN)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps({
            "fields": {
                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "Automatically created from GitHub comment /jira",
                                    "type": "text"
                                }
                            ],
                            "type": "paragraph"
                        }
                    ],
                    "type": "doc",
                    "version": 1
                },
                "issuetype": {
                    "id": "10011"
                },
                "project": {
                    "key": "AB"
                },
                "summary": "Jira ticket created from GitHub comment"
            },
            "update": {}
        })

        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        return jsonify({"status": "Jira ticket created", "response": response.json()}), 201

    else:
        print("Comment did not match '/jira'. Ignoring.")
        return jsonify({"status": "No action taken"}), 200

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
