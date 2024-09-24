from pyrogram import Client

async def handle(app: Client, client: Client, message):
    global stop_toggle
    stop_toggle = True
    await app.send_message(message.chat.id, "🌧 `kaleidoscope` is now closed.`")
    exit()
