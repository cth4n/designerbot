import sys
import os
import discord
import asyncio
from cogwatch import watch
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
intents.guilds = True
intents.members = True

class Bot(commands.Bot):
    def __init__(self, command_prefix="-", intents=None):
        super().__init__(command_prefix=command_prefix, intents=intents)

    @watch(path='cogs', preload=True, default_logger=True)
    async def on_ready(self):
        print(f"Bot is online as {self.user} (ID: {self.user.id}).")
        await self.tree.sync()

if __name__ == '__main__':
    bot = Bot(intents=intents)
    bot.remove_command("help")
    bot.run(TOKEN)
