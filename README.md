# discord-message-scrapper
A quick and dirty discord bot to save all messages from a channel into a JSON file.

## Requirements
- A bot you control in the server you want to scrape
- The bot token
- The channel ID

## Install dependencies
```shell
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Configuration
```shell
export BOT_TOKEN=<your-bot-token>
export CHANNEL_ID=<id-of-channel-to-scrape>
```
