import discord
from discord.ext import commands
from discord import app_commands

class outsiderCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="update_outsiders", description="Updates outsider role")
    @commands.has_permissions(administrator=True)
    async def update_outsiders(self, interaction: discord.Interaction):
        await interaction.response.send_message("Starting role assignment...", ephemeral=True)

        guild = interaction.guild
        added_count = 0
        removed_count = 0

        TARGET_ROLE_IDS = {
            1484252666623164476,
            1484252688928608329,
            1484252718418759700,
            1484262102721101997,
            1484260182149300357
        }
        OUTSIDERS_ROLE_ID = 1484255527986004000

        role = guild.get_role(OUTSIDERS_ROLE_ID)
        for member in guild.members:
            if role not in member.roles and any(r.id in TARGET_ROLE_IDS for r in member.roles):
                try:
                    await member.add_roles(role)
                    added_count += 1
                except discord.Forbidden:
                    print(f"Missing permissions for {member}")
                except discord.HTTPException as e:
                    print(f"Error: {e}")
            if role in member.roles and not any(r.id in TARGET_ROLE_IDS for r in member.roles):
                try:
                    await member.add_roles(role)
                    added_count += 1
                except discord.Forbidden:
                    print(f"Missing permissions for {member}")
                except discord.HTTPException as e:
                    print(f"Error: {e}")

        await interaction.followup.send(f"Done! Gave the role to {added_count} users and removed it from {removed_count} users.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(outsiderCommands(bot))