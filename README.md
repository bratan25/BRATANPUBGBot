# BRATAN PUBG Telegram Bot

A simple multilingual Telegram bot for BRATAN’s PUBG MOBILE settings\.

## Included

- English / Bulgarian / Russian language selector
- Sensitivity
- Controls
- Advanced Sensitivity
- Device
- PUBG UID
- TikTok
- Instagram
- Slash commands

## Security

Never put your Telegram bot token inside the code or GitHub repository\.
Set it as the `BOT_TOKEN` environment variable on your hosting provider\.

## Render

Create a Python Web Service\.

Build Command:
`pip install -r requirements.txt`

Start Command:
`python main.py`

Environment variables:

- `BOT_TOKEN` = your new BotFather token
- `WEBHOOK_URL` = your Render service URL \+ `/telegram-webhook`

Example:
`https://your-service-name.onrender.com/telegram-webhook`

After the service is deployed, open the bot in Telegram and send `/start`\.
