import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import webserver

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

TARGET_ROLE_IDS = {
    1406759995751661709,
    987654321098765432,
    555555555555555555
}
GIVE_ROLE_ID = 1484223681910673408

@bot.event
async def on_member_update(before, after):
    before_roles = set(before.roles)
    after_roles = set(after.roles)

    # Roles that were added
    added_roles = after_roles - before_roles
    role_to_add = after.guild.get_role(GIVE_ROLE_ID)

    if any(role.id in TARGET_ROLE_IDS for role in added_roles):
        if role_to_add and role_to_add not in after.roles:
            await after.add_roles(role_to_add, reason="Auto role assignment")

webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)