import discord
from discord.ext import commands

class Sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sync(self, ctx):
        await ctx.send("Syncing...")
        await self.bot.tree.sync()
        await ctx.send("Synced!")

async def setup(bot):
    await bot.add_cog(Sync(bot))