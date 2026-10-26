import discord

async def ping_stas(message):
    TARGET_ID = 840157927503691817
    messageContent = message.content
    messageAuthor = message.author
    messageChannel = message.channel
    if messageAuthor.id != 1484623372351570090:
        if "67" in messageContent:
            await messageChannel.send(f"I am dissapointed in you.")

