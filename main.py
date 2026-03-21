import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("CGMT2026Bot_DISCORD_TOKEN")

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
    before_ids = {role.id for role in before.roles}
    after_ids = {role.id for role in after.roles}

    added_ids = after_ids - before_ids

    if not (added_ids & TARGET_ROLE_IDS):
        return

    if GIVE_ROLE_ID in added_ids:
        return

    role_to_add = after.guild.get_role(GIVE_ROLE_ID)

    if role_to_add and role_to_add not in after.roles:
        try:
            await after.add_roles(role_to_add, reason="Auto role assignment")
        except discord.Forbidden:
            print("Missing permissions")
        except discord.HTTPException as e:
            print(f"HTTP error: {e}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
