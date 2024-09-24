import psutil
import platform
from pyrogram import Client

async def handle(app: Client, client: Client, message):
    ram_usage = psutil.virtual_memory().used / (1024 ** 3)
    total_ram = psutil.virtual_memory().total / (1024 ** 3)
    cpu_usage = psutil.cpu_percent()
    os_info = f"{platform.system()} {platform.release()}"

    await app.send_video(message.chat.id, "assets/info.mp4", caption=f"🌧 `Kaleidoscope`\n🔹 Version: `0.1.0` #1\n\n🌠 **Ram usage**:  `{ram_usage:.0f}GB/{total_ram:.0f}GB`\n♻ **CPU Usage**:  `{cpu_usage}%`\n💻 **OS:**  `{os_info}`")
