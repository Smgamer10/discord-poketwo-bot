import os
import discord
from discord.ext import commands, tasks

TOKEN = os.getenv('MTI2NDMwNDM5NzQwNDM0MDI4Nw.GTkb3b.vhnU--_Kq6RPfYPCneROOBMCnPd3svoN6fb4R4')
CHANNEL_ID = int(os.getenv('1264738443661938780'))
POKETWO_ID = os.getenv('716390085896962058')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')

@tasks.loop(seconds=3600)
async def spawn_pokemon():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        poketwo_mention = f'<@{POKETWO_ID}>'
        await channel.send(f'{poketwo_mention} catch <nome do pokemon>')
    else:
        print(f'Canal com ID {CHANNEL_ID} não encontrado')

@bot.command(name='start')
async def start_spawn(ctx):
    spawn_pokemon.start()
    await ctx.send('Spawn automático de Pokémon iniciado!')

@bot.command(name='stop')
async def stop_spawn(ctx):
    spawn_pokemon.stop()
    await ctx.send('Spawn automático de Pokémon parado!')

@bot.command(name='spawn')
async def manual_spawn(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        poketwo_mention = f'<@{POKETWO_ID}>'
        await channel.send(f'{poketwo_mention} catch <nome do pokemon>')
        await ctx.send('Pokémon spawnado manualmente!')
    else:
        await ctx.send(f'Canal com ID {CHANNEL_ID} não encontrado')

bot.run(TOKEN)
