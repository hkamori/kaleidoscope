from pyrogram import Client
from utils import config

commands = ["setprefix"]

async def handle(app: Client, client: Client, message, args):
    me = config.read_from_config('mainemoji')
    new_prefix = " ".join(args)  # Assuming args is a list of words for the new prefix
    # Update the global prefix variable (this might need to be passed differently)
    config.add_to_config('prefix', new_prefix)
    await app.send_message(message.chat.id, f"{me} **Prefix changed.** \n💫 New prefix: `({new_prefix})`")
