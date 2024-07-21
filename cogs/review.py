import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()

REVIEW_CHANNEL_ID = int(os.getenv('REVIEW_CHANNEL_ID'))


class Review(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="review", description="Submit a review with a star rating and additional info.")
    @app_commands.describe(stars="Rating out of 5 stars", info="Additional information or comments")
    async def review(self, interaction: discord.Interaction, stars: int, info: str):
        # Ensure stars is between 1 and 5
        if stars < 1 or stars > 5:
            await interaction.response.send_message("Please provide a rating between 1 and 5 stars.", ephemeral=True)
            return
        
        # Create the review embed
        embed = discord.Embed(
            title="New Review Submitted",
            description=f"**Rating:** ``{stars} {'⭐' * stars}``\n**Additional Info:** ``{info}``",
            color=0000000
        )
        embed.set_footer(text=f"Reviewed by: {interaction.user}", icon_url=interaction.user.avatar.url)
        
        # Get the review channel and send the embed
        channel = self.bot.get_channel(REVIEW_CHANNEL_ID)
        if channel is None:
            await interaction.response.send_message("Review channel not found.", ephemeral=True)
            return
                
        review_message = await channel.send(embed=embed)
        review_message_url = review_message.jump_url  # Get the URL to the review message
        
        # Response message with a link to the review message
        thank_you_message = (
            f"Thank you for your review! You can [view your review here]({review_message_url})."
        )
        await interaction.response.send_message(thank_you_message, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Review(bot))
