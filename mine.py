import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容を取得するために必要

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ログイン完了: {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() in ['ping', '/ping']:
        await message.channel.send('ポン！')

client.run(TOKEN)
￼
