#
# Copyright (C) 2024 by IamDvis@Github, < https://github.com/IamDvis >.
#
# This file is part of < https://github.com/IamDvis/DV-VIBES > project,
# and is released under the MIT License.
# Please see < https://github.com/IamDvis/DV-VIBES/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from ANWIVIBES import app
from ANWIVIBES.core.call import ANWI 
from ANWIVIBES.utils.database import is_music_playing, music_off
from ANWIVIBES.utils.decorators import AdminRightsCheck
from ANWIVIBES.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await ANWI.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
