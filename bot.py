import discord
from discord.ext import commands
from discord import app_commands
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
bot = commands.Bot(command_prefix='/',intents=intents)
token = "MTE5ODI0MjM5OTQwMzY1NTI0OA.GK7tVA.GJNhTRb5ayWmnRDSY0PRriA2lsmIKPf4Pt5XYM"

@bot.event
async def on_ready():
    print('ready')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name='hello')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey, {interaction.user.mention}!")

@bot.tree.command(name='say')
@app_commands.describe(thingtosay = "What should I say?")
async def say(interaction: discord.Interaction, thingtosay: str):
    await interaction.response.send_message(f"{interaction.user.name} said: {thingtosay}")

bot.run(token)
