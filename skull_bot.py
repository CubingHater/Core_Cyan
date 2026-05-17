from email.mime import message

import discord
import os
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
SKULL_CHANNEL_ID = 1505313262860894308

@client.event
async def on_ready():
    print(f"☠ Skull Bot is online als {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    await message.add_reaction("💀")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if random.random() < 0.001:
        await message.channel.send("I JUST HIT THE JACK POT!@everyone 💀" * 100)
    if random.random() <0.01:
        await message.channel.send("@core_cyan 💀" * 100)
    if message.channel.id != SKULL_CHANNEL_ID:
        return
    
    await message.add_reaction("💀")
    
token = os.getenv("DISCORD_TOKEN")
client.run(token)
