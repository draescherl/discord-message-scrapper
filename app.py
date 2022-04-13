import json
import os
import discord


async def get_all_messages():
    channel = client.get_channel(466696591399714822)
    messages = {}
    count = 0
    print(f"Reading messages of channel \"{channel.name}\" in server \"{channel.guild.name}\" ... ", end='')
    async for message in channel.history(limit=None, oldest_first=True):
        messages[count] = {
            "contents":  message.content,
            "author":    message.author.name,
            "timestamp": message.created_at
        }
        count += 1
    print("Done.")
    filename = "./message_dump.json"
    print(f"Writing {count + 1} messages to \"{filename}\" ... ", end='')
    with open(filename, 'w') as outfile:
        json.dump(messages, outfile, default=str, ensure_ascii=False, indent=2)
    print("Done.")


class Bot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await get_all_messages()
        await self.close()


intents = discord.Intents.all()
client = Bot(intents=intents)
client.run(os.environ.get("BOT_TOKEN"))
