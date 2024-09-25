import subprocess
from pyrogram import Client

commands = ["exec"]

async def handle(app: Client, client: Client, message, args):
    command = " ".join(args)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    output = result.stdout if result.stdout else result.stderr
    await app.send_message(message.chat.id,
                            f"🔰 **Command:** `{command}`\n\n🔅 **Output:** ```{output}```")
