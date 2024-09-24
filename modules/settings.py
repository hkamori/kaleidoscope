from ast import arg
from pyrogram import Client
from utils import config

async def handle(app: Client, client: Client, message):
    msg = "⚠  **Configuration**\n\n"
    p = config.read_from_config('prefix')
    cfgkeys = config.read_all_keys()
    def transform_dict_to_list():
        """
        Transforms the dictionary of config into a list of [key, value] pairs.

        :return: A list of lists, where each inner list contains a key and its corresponding value
        """
        config_dict = config.read_all_keys()
        return [[key, value] for key, value in config_dict.items()]
    config_list = transform_dict_to_list()

    for item in config_list:
        msg += f'❗ `{item[0]}` = "`{item[1]}`"\n'
    msg += f'\nℹ  To change or add new values, use `{p}setvalue (name) (value)`'
    await app.send_message(message.chat.id, msg)

async def setvalue(app: Client, client: Client, message, args):
    try:
        key = args[0]
        value = args[1]
        config.add_to_config(key, value)
        await app.send_message(message.chat.id, "💚  **Value set successfully**")
    except:
        await app.send_message(message.chat.id, "🛑  **The command is not used correctly**")
