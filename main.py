import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import scripts.outsiders as outsiders

load_dotenv()
token = os.getenv("CGMT2026Bot_DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_member_update(before, after):
    await outsiders.update_outsiders_role(before, after)

@bot.event
async def setup_hook():
    await bot.load_extension("scripts.outsiderCommands")
    await bot.tree.sync()

bot.run(token, log_handler=handler, log_level=logging.DEBUG)