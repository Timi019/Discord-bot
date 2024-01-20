import discord
from discord.ext import commands
from discord import app_commands
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
bot = commands.Bot(command_prefix='/',intents=intents)
token = "YOUR TOKEN HERE"

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

@bot.tree.command(name='heh')
@app_commands.describe(number = "How many times?")
async def heh(interaction: discord.Interaction, num: int):
    await interaction.response.send_message(f'he' * num)

@bot.tree.command(name='bye')
async def bye(interaction: discord.Interaction):
    await interaction.response.send_message(f"Bye, {interaction.user.mention}!")

@bot.tree.command(name='gen_pass')
@app_commands.describe(length = "How long password?")
async def passgen(interaction: discord.Interaction, length: int):
    await interaction.response.send_message(gen_pass(length))

@bot.tree.command(name='smile')
async def smile(interaction: discord.Interaction):
    await interaction.response.send_message(gen_emoji())

@bot.tree.command(name='coinflip')
async def coinflip(interaction: discord.Interaction):
    await interaction.response.send_message(flip_coin())

bot.run(token)
