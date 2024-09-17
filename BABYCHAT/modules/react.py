import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from BABYCHAT import dev

# List of reactions
reactions = ["👍", "👎", "❤️", "😂", "🤯", "😮", "🤔", "😢"]

@dev.on_message(filters.group & filters.text)
async def react_to_message(client: Client, message: Message):
    emoji = random.choice(reactions)
    await message.reply(emoji)
