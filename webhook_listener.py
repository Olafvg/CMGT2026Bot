from flask import Flask, request
import hmac
import hashlib
import subprocess

app = Flask(__name__)

# Replace with your GitHub webhook secret
GITHUB_SECRET = b'your_webhook_secret'

def verify_signature(payload, signature):
    sha_name, signature = signature.split('=')
    mac = hmac.new(GITHUB_SECRET, payload, hashlib.sha1)
    return hmac.compare_digest(mac.hexdigest(), signature)

@app.route("/github-webhook", methods=["POST"])
def github_webhook():
    signature = request.headers.get('X-Hub-Signature')
    if signature is None:
        return "No signature", 400

    if not verify_signature(request.data, signature):
        return "Invalid signature", 400

    # Pull latest code and restart bot
    subprocess.run(["/home/pi/your-bot/update_bot.sh"])
    return "Success", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)