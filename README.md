
# 🌧 kaleidoscope
This is a powerful Telegram userbot built using the Pyrogram framework. Automatization, Management, Fun.


## Features

- Message automation: Send and reply to messages automatically.
- User interaction: React to specific keywords or commands.
- Custom plugins: Add your own plugins to extend the bot's functionality.

## Requirements
Before you can run userbot, ensure that you have the following:

- Python 3.7+ installed
- API ID and API Hash


## Installation
Clone the repository:

```bash
git clone https://github.com/hkamori/kaleidoscope.git
cd kaleidoscope
```
Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```


## Commands

```
Ping:  (ping | pong | alive | check)
Info:  (info | kaleidoscope | userbot | about)
Help:  (help | commands)
Settings:  (settings | setvalue)
Stop:  (stop | exit)
Restart:  (restart | reboot)
SetPrefix:  (setprefix)
ExecLine:  (exec)
Translate:  (tr)
ILoveYou:  (ily)
Weather:  (weather)
```

# Implementing new modules
#### Step 1: Create a New Module File
1. Create a new ```.py``` file in the modules folder. For example, name it ```modulename.py```.

2. Add the necessary imports to your module file. For example, if you need a timer function, you would add:

```python
import time
```

3. Define the main function of your module. If your module does not require any arguments, the function signature should be:

```python
async def handle(app: Client, client: Client, message):
```

If your command requires arguments, modify the function like this:

```python
async def handle(app: Client, client: Client, message, args):
```

4. Write your code inside this function. For example, if you want to send a message using Pyrogram, use the following:

```python
await app.send_message(message.chat.id, "Your message here")
```

5. Working with Pyrogram: To create useful modules, it's important to know how to work with Pyrogram’s methods. Refer to the Pyrogram documentation if needed.

#### Step 2: Using Configuration Options
If your module requires reading or writing to a configuration file, import the configuration functions like this:

```python
from utils import config
```

You can then use the following functions:

- ```config.add_to_config(key, value)``` – Add or update a key-value pair.
- ```config.read_from_config(key)``` – Read a specific key from the config.
- ```config.read_all_keys()``` – Get all configuration keys.

#### Step 3: Modify ```message_handler.py```
Open the ```message_handler.py``` file located in the ```utils``` folder.

Add your module to the import statement. You will find a line like this:

```python
from modules import ping, help, info, stop, exec, translate, setprefix, restart, ily, moonlove, weather, settings
```
You need to add your module name (without the ```.py``` extension) to the list. For example, if your module is named ```modulename.py```, the line should look like this:

```python
from modules import ping, help, info, stop, exec, translate, setprefix, restart, ily, moonlove, weather, settings, modulename
```

Add your command handling logic. Find the section where commands are handled and add a new block for your command. For example:

```python
elif command == 'yourcommand':
    await app.delete_messages(message.chat.id, message.id)
    await modulename.handle(app, client, message, args)  # Remove args if not needed
```

#### Step 4: Add Your Command to the Help Menu
To list your command in the help section, update the ```msgtosend``` variable in ```help.py``` by adding your new command to the list of available commands. For example:

```python
f"{e} **ILoveYou:**  (`ily`)\n"
f"{e} **Weather:**  (`weather`)"
f"{e} **YourModuleName:** (`yourmodulecommand`)")
```

#### Final Notes
- Testing: Once you’ve added the command, test your module by running the bot and executing the command in a chat.
- Expanding: You can continue adding more functionality to your module as needed by using Pyrogram’s extensive methods and utilities.
By following these steps, you will be able to create and integrate custom modules into your userbot.
## Contributing

Feel free to fork the repository, submit issues, or contribute new features via pull requests.

- Fork the repository.
- Create a new branch ```(git checkout -b feature-branch)```.
- Make your changes.
- Commit the changes ```(git commit -m 'Add new feature')```.
- Push to the branch ```(git push origin feature-branch)```.
- Open a pull request.


## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)


