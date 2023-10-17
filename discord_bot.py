import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
server_id = 
J6_channel_id = 
general_channel_id = 

class DiscordBot(commands.Bot):
    def __init__(self, command_prefix, message):
        super().__init__(command_prefix, intents=intents)
        self.__message__ = message

    async def on_ready(self):
        print(f'Bot connesso a Discord come {self.user.name}')
        server = self.get_guild(server_id)
        J6_channel = discord.utils.get(server.text_channels, id=J6_channel_id)
        general_channel = discord.utils.get(server.text_channels, id=general_channel_id)
        try:
            await self.invia_messaggio(J6_channel, self.__message__)
            await self.invia_messaggio(general_channel, self.__message__)
        except Exception as err:
            print(err)
        await self.close()

    async def invia_messaggio(self, canale: discord.TextChannel, messaggio):
        await canale.send(messaggio)
