#
# Copyright (C) 2024 by IamDvis@Github, < https://github.com/IamDvis >.
#
# This file is part of < https://github.com/IamDvis/DV-VIBES > project,
# and is released under the MIT License.
# Please see < https://github.com/IamDvis/DV-VIBES/blob/master/LICENSE >
#
# All rights reserved.

import logging
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from ANWIVIBES import app
from pyrogram import filters
from config import BOT_USERNAME


@app.on_message(filters.command("yt"))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("✦ /yt needs an argument!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("✦ searching....")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"❖ ᴠɪᴅᴇᴏ ɴᴀᴍᴇ ➥ {results[i]['title']}\n\n"
            text += f"● ᴠɪᴅᴇᴏ ᴅᴜʀᴀᴛɪᴏɴ ➥ {results[i]['duration']}\n"
            text += f"● ᴠɪᴅᴇᴏ ᴠɪᴇᴡs ➥ {results[i]['views']}\n"
            text += f"● ᴠɪᴅᴇᴏ ᴄʜᴀɴɴᴇʟ ➥ {results[i]['channel']}\n"
            text += f"● ᴠɪᴅᴇᴏ ᴜʀʟ ➥ https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))

