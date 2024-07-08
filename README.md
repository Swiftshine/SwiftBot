# SwiftBot

## Requirements
* Python 3.8+
* Your own Discord developer application (and token)
* `discord.py`
* `colorama`
* `dotenv`
## Setup
Create a file called `.env` and write the following:
```env
DISCORD_TOKEN=YOUR_TOKEN_HERE
```
This is where your bot's token will go.

Create a folder called `files`. This is where any requested files from your machine will be searched for.

## Starting

To run the bot, run `start.py`.

## Commands

Commands are prefixed with a lowercase (reply, no ping) or uppercase (reply, with ping) letter 's'.

```
-s ping
```

Here is a full table of commands:

| Command | Description | Example/Notes |
|---|---|---|
| ping    | If the bot is up, it replies with "pong!" | - |
| get-file | The bot will send the file specified. | ;get-file; sample.txt |
| github | Links this page. | -|