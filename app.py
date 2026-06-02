from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Environment variables (set these in Render dashboard)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")  # Add this for security


def send_to_telegram(message: str):
    """Send a message to your Telegram chat."""
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("Missing Telegram credentials")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")


@app.route("/webhook", methods=["POST", "GET"])
def tradingview_webhook():
    """Receive webhook from TradingView and forward to Telegram."""
    # Security check using secret
    secret = request.args.get("secret")
    if WEBHOOK_SECRET and secret != WEBHOOK_SECRET:
        return jsonify({"status": "unauthorized"}), 401

    try:
        # Get the raw data TradingView sends
        data = request.get_data(as_text=True)

        # You can also do: data = request.get_json() if you send JSON from TV

        # Format a clean message
        message = f"🚨 <b>TradingView Alert</b>\n\n{data}"

        send_to_telegram(message)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({"status": "error"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
