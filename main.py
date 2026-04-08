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

@bot.event
async def on_member_update(before, after):
    await update_outsiders_role(before, after)

async def update_outsiders_role(before, after):
    TARGET_ROLE_IDS = {
        1484252666623164476,
        1484252688928608329,
        1484252718418759700,
        1484262102721101997,
        1484260182149300357
    }
    OUTSIDERS_ROLE_ID = 1484255527986004000

    before_ids = {role.id for role in before.roles}
    after_ids = {role.id for role in after.roles}

    if len(after_ids) > len(before_ids):
        added_ids = after_ids - before_ids
        if not (added_ids & TARGET_ROLE_IDS):
            return
        
        role_to_add = after.guild.get_role(OUTSIDERS_ROLE_ID)
        if role_to_add and role_to_add not in after.roles:
            try:
                await after.add_roles(role_to_add, reason="Auto role assignment")
            except discord.Forbidden:
                print("Missing permissions")
            except discord.HTTPException as e:
                print(f"HTTP error: {e}")
    else:
        removed_ids = before_ids - after_ids
        if not (removed_ids & TARGET_ROLE_IDS):
            return
        
        if (after_ids & TARGET_ROLE_IDS):
            return

        role_to_remove = after.guild.get_role(OUTSIDERS_ROLE_ID)
        if role_to_remove and role_to_remove in after.roles:
            try:
                await after.remove_roles(role_to_remove, reason="Auto role removal")
            except discord.Forbidden:
                print("Missing permissions")
            except discord.HTTPException as e:
                print(f"HTTP error: {e}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)