import discord
import re
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
ACTIVITY_NAME = os.getenv('ACTIVITY_NAME')

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
instagram_regex = r"(https:\/\/www\.instagram\.com\/[^\s\?]+)(\?igsh=[^\s]+)?"

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=ACTIVITY_NAME))
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    matches = re.finditer(instagram_regex, message.content)
    if matches:
        for match in matches:
            base_url = match.group(1)
            cleaned_url = base_url.replace("instagram.com", "instagramez.com")
            repost_message = f"Instagram link posted by {message.author}: {cleaned_url}"
            await message.delete()
            await message.channel.send(repost_message)

bot.run(DISCORD_TOKEN)
