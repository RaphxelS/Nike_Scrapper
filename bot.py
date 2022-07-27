import os
import discord

from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

from nike_scrap import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix='!',
    intents = discord.Intents(messages=True)
)


@bot.command(name='nk', help='SCRAP NIKE STOCK')
async def nk(ctx, taille, lien):
    time.sleep(2)
    await ctx.send("SCRAPING EN COURS...")
    response = main(taille, lien)
    await ctx.send(response)
    await ctx.send(file=discord.File('screenshot.png'))
    

bot.run(TOKEN)
