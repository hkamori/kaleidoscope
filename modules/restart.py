import os
import sys
from pyrogram import Client

async def handle(app: Client, client: Client, message):
    await app.send_message(message.chat.id, "🌧 `Kaleidoscope` **is restarting...**")
    os.execv(sys.executable, ['python'] + sys.argv)
