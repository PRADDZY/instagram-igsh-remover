# Discord Instagram Link Cleaner Bot

## Installation

To use this bot, you'll need to have Python and the `discord.py` library installed. You can install the required dependencies using pip:

```
pip install discord.py
```

## Usage

1. Clone the repository or copy the `bot.py` file to your local machine.
2. Replace the bot token in the `bot.run()` function with your own bot token.
3. Run the `bot.py` file to start the bot:

```
python bot.py
```

Once the bot is running, it will listen for messages in the Discord server and automatically clean any Instagram links by removing the tracking parameters.

## API

The bot uses the following Discord API events:

- `on_ready()`: This event is triggered when the bot is logged in and ready to receive messages.
- `on_message(message)`: This event is triggered whenever a new message is sent in the Discord server. The bot checks the message content for Instagram links and cleans them.

The bot also uses the following regular expression to capture Instagram links with tracking parameters:

```python
instagram_regex = r"(https:\/\/www\.instagram\.com\/[^\s\?]+)(\?igsh=[^\s]+)?"
```

## Testing

To test the bot, you can send a message in the Discord server that contains an Instagram link. The bot should automatically delete the original message and repost the cleaned link.

You can also test the bot by running it locally and sending messages to it directly. Make sure to replace the bot token with your own token before running the bot.
