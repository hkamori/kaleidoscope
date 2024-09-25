import time, threading, socket
from pyrogram import Client

commands = ["ping", "pong", "alive", "check"]
global_uptime = 0
stop_toggle = False

def uptime_thread():
    global global_uptime, stop_toggle
    while not stop_toggle:
        time.sleep(1)
        global_uptime += 1

def send_ping():
    start_time = time.time()
    try:
        socket.create_connection(("149.154.167.51", 80))
    except OSError:
        return "⚠️ Error connecting to Telegram."
    else:
        return f"{(time.time() - start_time) * 1000:.2f} ms"

def count_uptime(global_uptime):
    minutes, seconds = divmod(global_uptime, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    time_str = ""
    if days > 0:
        time_str += f"{days} days, "
    time_str += f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return time_str

uptimethr = threading.Thread(target=uptime_thread, daemon=True)
uptimethr.start()

async def handle(app: Client, client: Client, message, args):
    ping_time = send_ping()
    uptime = count_uptime(global_uptime)
    await app.send_message(message.chat.id, f"⚡ **Telegram ping:** `{ping_time}`\n🚀 **Uptime:** `{uptime}`")
