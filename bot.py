import discord
import re
import time
from discord.ext import commands


DISCORD_TOKEN = 'your-discord-bot-token'  
BOT_OWNER_ID = your-discord-user-id  
PREFIX = '<'


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix=PREFIX, intents=intents)

start_time = time.time()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
   
    activity = discord.Activity(type=discord.ActivityType.watching, name="your Instagram links")
    await bot.change_presence(activity=activity)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


    if "https://www.instagram.com/" in message.content:
        user = message.author
        link = message.content


        cleaned_link = re.sub(r'/\?.*', '', link)

        try:
            await message.delete()
            await message.channel.send(f'Instagram link posted by {user.name}: {cleaned_link}')
        except Exception as e:
            print(f'Error deleting or sending message: {e}')

    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    if ctx.author.id == BOT_OWNER_ID:
        await ctx.send('Pong!')
    else:
        await ctx.send('You are not allowed to use this command.')

@bot.command(name='uptime')
async def uptime(ctx):
    if ctx.author.id == BOT_OWNER_ID:
        current_time = time.time()
        uptime_seconds = int(current_time - start_time)
        
        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        uptime_str = f"Uptime: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
        await ctx.send(uptime_str)
    else:
        await ctx.send('You are not allowed to use this command.')


bot.run(DISCORD_TOKEN)
