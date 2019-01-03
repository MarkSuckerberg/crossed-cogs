#Standard Imports
import asyncio
import time

#Discord Imports
import discord

#Redbot Imports
from redbot.core import commands, checks, Config, utils

__version__ = "0.0.1"
__author__ = "Crossedfall"

BaseCog = getattr(commands, "Cog", object)

class SS13RoundManager(BaseCog):

    def __init__(self, bot):
        self.bot = bot

        try:
            loop = asyncio.get_event_loop()
            loop.create_task(self.get_db_conf())
        except:
            self.config = Config.get_conf(self, 3257193195, force_registration=True)

            default_guild = {
                "mysql_host": "127.0.0.1",
                "mysql_port": 3306,
                "mysql_user": "ss13",
                "mysql_password": "password",
                "mysql_db": "feedback",
                "admin_ckey": {}
            }

            self.config.register_global(**default_guild)

    async def get_db_conf(self):
        await self.bot.wait_until_ready() 
        try:
            getnotes = self.bot.get_cog('GetNotes')
            self.config = getnotes.config
        except:
            raise