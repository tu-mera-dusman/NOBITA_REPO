#
# Copyright (C) 2024 by IamDvis@Github, < https://github.com/IamDvis >.
#
# This file is part of < https://github.com/IamDvis/DV-VIBES > project,
# and is released under the MIT License.
# Please see < https://github.com/IamDvis/DV-VIBES/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ANWIVIBES import LOGGER, app, userbot
from ANWIVIBES.core.call import ANWI
from ANWIVIBES.misc import sudo
from ANWIVIBES.plugins import ALL_MODULES
from ANWIVIBES.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("✦ Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ANWIVIBES.plugins" + all_module)
    LOGGER("ANWIVIBES.plugins").info("✦ Successfully Imported Modules...💞")
    await userbot.start()
    await ANWI.start()
    try:
        await ANWI.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ANWIVIBES").error(
            "✦ Please turn on the videochat of your log group\channel.\n\n✦ Stopping Bot...💣"
        )
        exit()
    except:
        pass
    await ANWI.decorators()
    LOGGER("ANWIVIBES").info(
        "✦ Created By ➥ The Captain...🐝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ANWIVIBES").info("❖ Stopping ANWI VIBES Bot...💌")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
