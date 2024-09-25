import os
import importlib
import subprocess
from pyrogram import Client
from pyrogram.types.messages_and_media import message
from utils import config

module_names = [
    name[:-3] for name in os.listdir("modules")
    if name.endswith(".py") and name != "__init__.py"
]
modules = {name: importlib.import_module(f"modules.{name}") for name in module_names}

def parse_command(text):
    prefix = config.read_from_config('prefix')
    if text.startswith(prefix):
        command_parts = text.split(prefix)[1].strip().split()
        command = command_parts[0]
        args = command_parts[1:]
        return command, args
    return None, None

async def loadmodule(app, message):
    file = await message.download()
    try:
        importlib.import_module(f'downloads.{message.document.file_name[:-3]}')
        subprocess.run(f'rm downloads/{message.document.file_name}')
        download_folder = "modules"
        await message.download(file_name=os.path.join(download_folder, message.document.file_name))
        await app.send_message(message.chat.id, "✅  Module **loaded** successfully, restart your userbot.\n\n⚠  **Note: **If your module does not answer to messages, this means that your module is not implemented according to the instructions")
    except Exception as error:
        await app.send_message(message.chat.id, f"📛  **Error loading module**")


async def handle_message(client: Client, message, app: Client):
    if message.document:
        if message.caption:
            if message.caption == ".lm" or message.caption == ".loadmodule":
                await loadmodule(app, message)
    elif message.text:
        command, args = parse_command(message.text)
        if command:
            # await app.delete_messages(message.chat.id, message.id)
            command_handled = False
            for module_name, module in modules.items():
                if hasattr(module, 'commands') and command in module.commands:
                    await module.handle(app, client, message, args)
                    command_handled = True
                    break

            if not command_handled:
                pass
    else:
        pass
