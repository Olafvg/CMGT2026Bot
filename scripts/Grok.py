import discord
import random

async def grok(message):
    answers = [
        "yeah I dont know this one",
        "buddy look it up yourself",
        "man im busy",
        "just use your buas claude account for this, i cant be bothered",
        "get a job damn",
        "192.166.255.1, Breda, Netherlands\nThis you?"
    ]
    messageContent = message.content
    messageAuthor = message.author
    messageChannel = message.channel
    if messageAuthor.id != 1484623372351570090:
        if "@grok" in messageContent:
            await messageChannel.send(answers[random.randint(0, len(answers))])
