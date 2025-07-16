import discord
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await send_spotify_links_loop()

async def send_spotify_links_loop():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        while not client.is_closed():
            # Пример: просто отправим тестовую ссылку
            await channel.send("🖤 New music\nhttps://open.spotify.com/track/example")
            await asyncio.sleep(3600)  # ждет 1 час

client.run(DISCORD_TOKEN)
