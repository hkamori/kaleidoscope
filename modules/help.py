from pyrogram import Client
from utils import config

async def handle(app: Client, client: Client, message):
    e = config.read_from_config('help_emoji')
    msgtosend = (f"🌧 **9** Commands available\n\n"
                f"{e} **Ping:**  (`ping` | `pong` | `alive` | `check`)\n"
                f"{e} **Info:**  (`info` | `kaleidoscope` | `userbot` | `about`)\n"
                f"{e} **Help:**  (`help` | `commands`)\n"
                f"{e} **Settings:**  (`settings` | `setvalue`)\n"
                f"{e} **Stop:**  (`stop` | `exit`)\n"
                f"{e} **Restart:**  (`restart` | `reboot`)\n"
                f"{e} **SetPrefix:**  (`setprefix`)\n"
                f"{e} **ExecLine:**  (`exec`)\n"
                f"{e} **Translate:**  (`tr`)\n"
                f"{e} **ILoveYou:**  (`ily`)\n"
                f"{e} **Weather:**  (`weather`)")
    await app.send_message(message.chat.id, msgtosend)
