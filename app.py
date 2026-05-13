from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8764471009:AAE5kTp_zNTAAvMwlseOTqs8KvNrjGrutrI"
CHAT_ID = "-1003800263291"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("text", "TradingView Alert")  # ← FIXED: "message" changed to "text"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)
    return "ok"

@app.route('/')
def home():
    return "TrendStrike Bot Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
