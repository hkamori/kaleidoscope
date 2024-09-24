# Dont touch this file.

#    __        __    _    __
#   / /_____ _/ /__ (_)__/ /__  ___ _______  ___  ___
#  /  '_/ _ `/ / -_) / _  / _ \(_-</ __/ _ \/ _ \/ -_)
# /_/\_\\_,_/_/\__/_/\_,_/\___/___/\__/\___/ .__/\__/
#                                         /_/

# ----------------------------------------------------------------------
import json, os, sys, time, threading
from pyrogram import Client, filters
from requests import api
from utils.command_parser import parse_command
from utils.message_handler import handle_message
# ----------------------------------------------------------------------
global_uptime = 0
stop_toggle = False
api_id = None
api_hash = None
# ----------------------------------------------------------------------
try:
    with open('credentials', "rb") as credentials:
        credentials_data = json.load(credentials)
except (FileNotFoundError, json.JSONDecodeError):
    credentials_data = {}

if not credentials_data:
    api_id = input("Enter API ID: ")
    api_hash = input("Enter API hash: ")
    credentials_data = {'api_id': api_id, 'api_hash': api_hash}

with open('credentials', "wb") as credentials:
    credentials.write(json.dumps(credentials_data).encode('utf-8'))

api_id = credentials_data['api_id']
api_hash = credentials_data['api_hash']
# ----------------------------------------------------------------------
def uptime_thread():
    global global_uptime, stop_toggle
    while not stop_toggle:
        time.sleep(1)
        global_uptime += 1
# ----------------------------------------------------------------------
def initialize():
    os.system('cls')
    print("\033[95m __           .__         .__    .___                                       ")
    print("|  | _______  |  |   ____ |__| __| _/____  ______ ____  ____ ______   ____  ")
    print("|  |/ /\__  \ |  | _/ __ \|  |/ __ |/  _ \/  ___// ___\/  _ \\____ \_/ __ \ ")
    print("|    <  / __ \|  |_\  ___/|  / /_/ (  <_> )___ \\  \__(  <_> )  |_> >  ___/ ")
    print("|__|_ \(____  /____/\___  >__\____ |\____/____  >\___  >____/|   __/ \___  >")
    print("     \/     \/          \/        \/          \/     \/      |__|        \/ \033[92m")
# ----------------------------------------------------------------------
initialize()
app = Client("kaleidoscope", api_id = api_id, api_hash = api_hash)
uptimethr = threading.Thread(target=uptime_thread, daemon=True)
uptimethr.start()
print("\n\n                            🌧 Launch was successful!\033[94m")
# ----------------------------------------------------------------------
@app.on_message(filters.text & filters.private)
async def send_message(client, message):
    await handle_message(client, message, app, global_uptime)

app.run()
