import os
import importlib
from pyrogram import Client
from utils import config

commands = ["help", "commands"]

module_names = [
    name[:-3] for name in os.listdir("modules")
    if name.endswith(".py") and name != "__init__.py"
]
modules = {name: importlib.import_module(f"modules.{name}") for name in module_names}

commands_dict = {}
for module_name, module in modules.items():
    if hasattr(module, 'commands'):
        for command in module.commands:
            if module_name not in commands_dict:
                commands_dict[module_name] = []
            commands_dict[module_name].append(command)

async def handle(app: Client, client: Client, message, args):
    e = config.read_from_config('help_emoji')
    me = config.read_from_config('mainemoji')
    commands_count = sum(len(cmds) for cmds in commands_dict.values())
    modules_count = len(commands_dict)  # Count of unique modules
    msgtosend = f"{me} **{commands_count}** Commands available. **{modules_count}** modules.\n\n"
    # msgtosend = f"{me} **{len(commands_list)}** Commands available\n\n"
    # for command, module_name in commands_list:
    #     msgtosend += f"{e} **{module_name.capitalize()}**:  (`{command}`)\n"
    # msgtosend = (f"{me} **9** Commands available\n\n"
    #             f"{e} **Ping:**  (`ping` | `pong` | `alive` | `check`)\n"
    #             f"{e} **Info:**  (`info` | `kaleidoscope` | `userbot` | `about`)\n"
    #             f"{e} **Help:**  (`help` | `commands`)\n"
    #             f"{e} **Settings:**  (`settings` | `setvalue`)\n"
    #             f"{e} **Stop:**  (`stop` | `exit`)\n"
    #             f"{e} **Restart:**  (`restart` | `reboot`)\n"
    #             f"{e} **SetPrefix:**  (`setprefix`)\n"
    #             f"{e} **ExecLine:**  (`exec`)\n"
    #             f"{e} **Translate:**  (`tr`)\n"
    #             f"{e} **ILoveYou:**  (`ily`)\n"
    #             f"{e} **Weather:**  (`weather`)")

    for module_name, commands in commands_dict.items():
            commands_str = " | ".join(commands)  # Join commands with a pipe separator
            msgtosend += f"{e} **{module_name.capitalize()}**:  ({commands_str})\n"
    await app.send_message(message.chat.id, msgtosend)
