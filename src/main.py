
from discord import Intents
from discord.ext import commands   
from discord import app_commands
from dotenv import load_dotenv
from os import getenv
from datetime import date
from time import time
import json
from os import chdir
from wotdDate import wotdDate
from WotdClient import WotdClient

chdir("src")

intent = Intents.default()
intent.message_content = True

# class WotdClient(commands.Bot):

#     # def __init__(self, command_prefix, intents):
#     #     self.currentDate = wotdDate()
#     #     self.datefile = "date.json"
#     #     super().__init__(command_prefix=command_prefix, intents=intents)

#     def __init__(self, intents):
#         self.currentDate = wotdDate()
#         self.datefile = "../date.json"
#         super().__init__(command_prefix="wotd$:", intents=intents)

#     async def setup_hook(self):
#         await self.load_extension('WotdCommands')

#     async def on_ready(self):
#         print(f"Successfully logged in as {self.user}")
#         try:
#             synced = await self.tree.sync()
#             print(f"Synced {len(synced)} commands")
#         except Exception as e:
#             print("Failed to sync commands")

#     async def on_message(self, message):
#         if message.author == self.user:
#             return
#             # print(f"User message recieved: \'{message.content}\'")
#         elif message.content == "~!hello":
#             await message.channel.send("Hello!")
#         elif message.content.startswith(self.command_prefix):
#             await message.channel.send("Input Recognized")
   
# client = WotdClient(command_prefix='wotd$:',intents=intent)
client = WotdClient(intents=intent)

load_dotenv()
my_token = getenv('DISCORD_TOKEN') # located in ".env"

client.load_extension('WotdCommands')
client.run(token=my_token)


