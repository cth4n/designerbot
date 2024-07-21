import discord
from discord.ext import commands
from discord import app_commands

# Function to calculate the after-tax amount
def calculate_after_tax(amount: float) -> float:
    tax_rate = 42.8 / 100  # Convert 42.8% to a decimal
    return amount * (1 + tax_rate)

class Tax(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="tax", description="Calculate the after-tax amount.")
    async def tax(self, interaction: discord.Interaction, amount: float):       
        after_tax_amount = calculate_after_tax(amount)
        after_tax_amount_rounded = round(after_tax_amount)  # Round to the nearest whole number
        
        # Remove .0 from the amount if it's a whole number
        original_amount_str = f"{amount:.0f}" if amount.is_integer() else f"{amount:.2f}"
        after_tax_amount_str = f"{after_tax_amount_rounded:.0f}"
        
        embed = discord.Embed(
            title="📊 Tax Calculation",
            description=f"**Original Amount:** ``{original_amount_str}``\n**After Tax Amount:** ``{after_tax_amount_str}``",
            color=00000
        )        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Tax(bot))
