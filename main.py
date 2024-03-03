import discord
from bot_logic import *

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)
token = "MTE5NTczMDQ4MDAwODUzMjA3OQ.GqZ6NV.slDXJ2KOLbl7M-PE3ISG0D9LgTuxLp971KrrHg"
prefix = '/'
@client.event
async def on_ready():
    print(f'Zalogowano się jako {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:   
        return
    if message.content.startswith(prefix+'hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith(prefix+'bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith(prefix+'generate_password'):
        await message.channel.send(gen_pass(10) + " Twoje haslo ma 10 znaków")
    elif message.content.startswith(prefix+'smile'):
        await message.channel.send(gen_emoji())
    elif message.content.startswith(prefix+'flip_coin'):
        await message.channel.send(flip_coin())
    
client.run(token)