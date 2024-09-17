# Don't remove This Line From Here.
# SUPPORT :- (https://t.me/+OL6jdTL7JAJjYzVl)
# UPDATE ON TELEGRAM :- (https://t.me/BABY09_WORLD)
# POWERD BY :- UTTAM470

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import IMG, OWNER_USERNAME, STICKER
from BABYCHAT import BOT_NAME, dev
from BABYCHAT.database.chats import add_served_chat
from BABYCHAT.database.users import add_served_user
from BABYCHAT.modules.helpers import PNG_BTN


@dev.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="❍ ᴘɪɴɢ ᴘᴏɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"❍ ʜᴇʏ ʙᴀʙʏ\n{BOT_NAME} ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ʀᴜɴɴɪɴɢ ғɪɴᴇ wɪтн ᴀ ᴘɪɴɢ oғ\n➥ `{ms}` ms\n\n<b>❍ᴘᴏᴡᴇʀᴇᴅ ʙʏ➛[ʙᴧʙʏ-ᴍᴜsɪᴄ™](https://t.me/BABY09_WORLD) </b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
