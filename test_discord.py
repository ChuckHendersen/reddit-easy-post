import discord
import threading
import time
import _thread
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
server_id = 00000000000000
channel_id = 00000000000000

class DiscordBot(commands.Bot):
    def __init__(self, command_prefix, message):
        super().__init__(command_prefix, intents=intents)
        self.__message__ = message

    async def on_ready(self):
        print(f'Bot connesso a Discord come {self.user.name}')
        server = self.get_guild(server_id)
        canale = discord.utils.get(server.text_channels, id=channel_id)
        await self.invia_messaggio(canale,self.__message__)
        await self.close()

    async def invia_messaggio(self, canale: discord.TextChannel, messaggio):
        await canale.send(messaggio)