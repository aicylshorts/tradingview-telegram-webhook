# TradingView → Telegram Webhook

Clean, lightweight webhook receiver that forwards TradingView alerts to Telegram.

Designed to work perfectly with the **Apex Multi-Confluence Scalper v3** indicator (and any other Pine Script alerts).

## Features
- Simple Flask app
- Secure webhook endpoint
- Clean Telegram formatting
- Easy deployment on Render (free tier)
- Ready for your existing Telegram bot

## Quick Start

1. Clone or fork this repo
2. Set environment variables on Render:
   - `TELEGRAM_TOKEN` = your bot token
   - `TELEGRAM_CHAT_ID` = your chat ID
   - `WEBHOOK_SECRET` = any random string (for security)
3. Deploy on Render as Web Service
4. Use the webhook URL in TradingView alerts

## Webhook URL Format

```
https://your-app.onrender.com/webhook?secret=YOUR_WEBHOOK_SECRET
```

## How to Use with TradingView

1. Add an alert on your chart (using the Apex v3 indicator)
2. In the alert settings:
   - Condition: `long_entry` or `short_entry` is true
   - Webhook URL: paste your Render URL above
   - Message: Use placeholders like `{{ticker}} | Score: {{plot("CONFLUENCE SCORE")}}%`

## Security
Always use the `secret` query parameter so only you can trigger the webhook.

## Files
- `app.py` – Main Flask application
- `requirements.txt` – Python dependencies
- `render.yaml` – One-click Render deployment config

Created for the SMC Powerhouse trading system.