import discord
from discord import Intents
from discord.ext import commands   
from discord import app_commands
from dotenv import load_dotenv
from os import getenv
from datetime import date
from time import time
from wotdDate import wotdDate
from WotdHandler import WordHandler
from menuView import menuView
from math import ceil
import json

dayUnix = 86400 

class WotdCommands(commands.Cog):

    def __init__(self, bot):
    
        self.bot = bot
        self._setCurrentDate()
        self.wotdHandler = WordHandler()

        with open("../date.json",'r') as file:
            dateIn = json.load(file)
            self.lastUnix = dateIn["lastunix"]
            self.lastYear, self.lastMonth, self.lastDay = dateIn["lastdate"].split('-')
        # super().__init__()
            
    def _setCurrentDate(self):
        self.currentDate = wotdDate()

    def _daysSinceLast(self):
        
        if self.currentDate.day != self.lastDay:
            daydiff = ceil((self.currentDate.unix-self.lastUnix)/dayUnix)
        else:
            daydiff = 0
        
        return daydiff
            
    # @app_commands.command(description="Fetch the current date.")
    # async def fetch_date(self, interaction):
    #     # word = message.content
    #     # if isinstance(word,str) and word.isalpha():
    #     #     await message.channel.send(f"Current Date: {date}")
    #     # else:
    #     #     await message.channel.send("Invalid Word Input")
    #     print(f"Fetch command executed by {interaction.user}")
    #     await interaction.response.send_message(f"Current Date: {self.currentDate}")

    # @app_commands.command(description="Test for wotd.")
    # async def wotd_test(self, interaction:discord.Interaction, msg:str):
    #     '''
    #     *args:str is used to take any number of string inputs from the slash command message.
    #     When using a command, everything separated by a space is taken as its own input.
    #     However, if something is within quotes (e.g. "hello there"), the whole string will be taken.

    #     Note: you can only respond (interaction.response) once per interaction
    #     '''
    #     print(type(interaction.message))
    #     try:
    #         if isinstance(msg,str) and msg.isalpha():
    #             await interaction.response.send_message(f"Message Recieved: {msg}")
    #         else:
    #             await interaction.response.send_message("Invalid Word Input")
    #         print(f"Fetch command executed by {interaction.user}")
    #         # await interaction.response.send_message(f"Current Date: {self.currentDate}")
    #     except:
    #         await interaction.response.send_message(f"Message Error")

    @app_commands.command(description="test for menu")
    async def option_menu(self, interaction:discord.Interaction):
        view = menuView(self.wotdHandler)
        await interaction.response.send_message("Choose an option", view=view, ephemeral=True)


async def setup(bot):
    await bot.add_cog(WotdCommands(bot))