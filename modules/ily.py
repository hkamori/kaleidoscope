import asyncio
import requests
from pyrogram import Client

async def fetch_hearts_animation():
    response = await asyncio.get_event_loop().run_in_executor(
        None,
        lambda: requests.get("https://gist.githubusercontent.com/hikariatama/89d0246c72e5882e12af43be63f5bca5/raw/08a5df7255d5e925ab2ede1efc892d9dc93af8e1/ily_classic.json")
    )
    return response.json()

async def handle(app: Client, client: Client, message):
    hearts_animation = await fetch_hearts_animation()
    for frame in hearts_animation:
        await app.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=frame)
        await asyncio.sleep(0.5)  # Adjust the speed of the animation as needed
