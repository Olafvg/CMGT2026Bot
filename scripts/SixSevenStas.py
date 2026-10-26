import discord
import re
import random

# thank you claude by giving me regex for this
DISCORD_TOKENS = re.compile(r"<(?:@[!&]?|#|a?:\w+:|/[\w -]+:|t:)\d+(?::\w)?>")
LINKS = re.compile(r"https?://\S+")

def contains_67(content: str) -> bool:
    cleaned = DISCORD_TOKENS.sub("", content)
    cleaned = LINKS.sub("", cleaned)
    return "67" in cleaned


async def ping_stas(message):
    STAS_ID = 840157927503691817
    BOT_ID = 1484623372351570090
    messageContent = message.content
    messageAuthor = message.author
    messageChannel = message.channel
    if messageAuthor.id == BOT_ID:
        return

    if contains_67(message.content):
        if random.randint(0, 1):
             await message.channel.send("I am disappointed in you.")
             return
        await message.channel.send(f"I am disappointed in you.\n I'm pinging Stas anyways. Hello <@{STAS_ID}>.")
       

