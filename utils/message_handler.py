#add your modules here

from pyrogram import Client, filters
from pyrogram.methods.messages import delete_messages
from modules import ping, help, info, stop, exec, translate, setprefix, restart, ily, moonlove, weather, settings
from utils.command_parser import parse_command

async def handle_message(client, message, app, global_uptime):
    command, args = parse_command(message.text)
    if command:
        if command == "ping" or command == "pong" or command == "alive" or command == "check":
            await app.delete_messages(message.chat.id, message.id)
            await ping.handle(app, client, message, global_uptime)
        elif command == "help" or command == "commands":
            await app.delete_messages(message.chat.id, message.id)
            await help.handle(app, client, message)
        elif command == "info" or command == "kaleidoscope" or command == "userbot" or command == "about":
            await app.delete_messages(message.chat.id, message.id)
            await info.handle(app, client, message)
        elif command == "stop" or command == "exit":
            await app.delete_messages(message.chat.id, message.id)
            stop_toggle = await stop.handle(app, client, message)
        elif command == "exec":
            await app.delete_messages(message.chat.id, message.id)
            await exec.handle(app, client, message, args)
        elif command == "tr":
            await app.delete_messages(message.chat.id, message.id)
            await translate.handle(app, client, message, args)
        elif command == "setprefix":
            await app.delete_messages(message.chat.id, message.id)
            await setprefix.handle(app, client, message, args)
        elif command in ["restart", "reboot"]:
            await app.delete_messages(message.chat.id, message.id)
            await restart.handle(app, client, message)
        elif command == "ily":
            await ily.handle(app, client, message)
        elif command == "moonlove":
            await moonlove.handle(app, client, message)
        elif command == "weather":
            await app.delete_messages(message.chat.id, message.id)
            await weather.handle(app, client, message, args)
        elif command == "settings":
            await app.delete_messages(message.chat.id, message.id)
            await settings.handle(app, client, message)
        elif command == 'setvalue':
            await app.delete_messages(message.chat.id, message.id)
            await settings.setvalue(app, client, message, args)
        #here is your module
