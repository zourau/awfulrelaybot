import discord
from discord.ext import commands

bot = discord.Client()

@bot.event
async def on_ready():
        print (f'working maybe')

@bot.event
async def on_message(message):
    if message.channel.id == ListeningChannelID:
        channel = bot.get_channel(RelayChannelID)
        await channel.send(f"@everyone```Username: {message.author} \nChannel: {message.channel} \nPing: {message.content}```")


TOKEN = 'Insert Token Here'
bot.run(TOKEN)
