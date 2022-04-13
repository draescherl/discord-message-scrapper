import json
import os
import discord
from termcolor import colored


async def get_all_messages():
    try:
        channel = client.get_channel(int(os.environ.get('CHANNEL_ID')))
        messages = {}
        count = 0
        print(f'Reading messages of channel {colored(channel.name, "cyan")} in server {colored(channel.guild.name, "cyan")} ... ', end='')
        async for message in channel.history(limit=None, oldest_first=True):
            messages[count] = {
                'contents':  message.content,
                'author':    message.author.name,
                'timestamp': message.created_at
            }
            count += 1
        print(colored('Done.', 'green'))
        filename = './message_dump.json'
        print(f'Writing {colored(str(count + 1), "cyan")} messages to {colored(filename, "cyan")} ... ', end='')
        with open(filename, 'w') as outfile:
            json.dump(messages, outfile, default=str, ensure_ascii=False, indent=2)
        print(colored('Done.', 'green'))
    except AttributeError:
        print(colored('The provided channel ID is either invalid or your bot does not have access to it.', 'red'))


class Bot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {colored(self.user, "cyan")}.')
        await get_all_messages()
        await self.close()


intents = discord.Intents.all()
client = Bot(intents=intents)
try:
    client.run(os.environ.get('BOT_TOKEN'))
except discord.errors.LoginFailure:
    print(colored('The provided token is invalid.', 'red'))
