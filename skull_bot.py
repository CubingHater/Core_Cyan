from flask import Flask
from threading import Thread

import discord
import os
import random

# ---------------- DISCORD ----------------

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

SKULL_CHANNEL_ID = 1505313262860894308
TOKEN = os.getenv("DISCORD_TOKEN")

# ---------------- FLASK ----------------

app = Flask(__name__)

@app.route("/")
def home():
    return "Skull Bot is online 💀"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ---------------- EVENTS ----------------

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
    
# ---------------- START ----------------

Thread(target=run_web).start()

client.run(TOKEN)
