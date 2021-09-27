# Regen & Mod by @shamilhabeebnelli
# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
from utils import USERNAME, FFMPEG_PROCESSES
from config import Config
import os
import sys
U=USERNAME
CHAT=Config.CHAT


HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\n• Iam Baws FM Streamer by HARP Production\n• I Can Manage Group VC's\n\n• Hit /help to know about available commands.</b>"
HELP = """
🎧 <b>I Can Play Musics On VoiceChats 🤪</b>

🎶 **Common Commands**:
• `/song` __Download Song from youtube__
• `/c`  __Show current playing song__
• `/help` __Show help for commands__
• `/whotto` __Shows the playlist__
• `/stickerid` __To Get Id Of Replied Sticker__

🎶 **Admin Commands**:
• `/p`  __Reply to an audio file or YouTube link to play it or use /p <song name>__
• `/d` __Play music from Deezer, Use /d <song name>__
• `/sk [n]` __...Skip current or n where n >= 2__
• `/j`  __Join voice chat__
• `/l`  __Leave current voice chat__
• `/whotto`  __Check which VC is joined__
• `/sp`  __Stop playing__
• `/r` __Start Radio__
• `/sr` __Stops Radio Stream__
• `/rp`  __Play from the beginning__
• `/cl`  __Remove unused RAW PCM files__
• `/ps` __Pause playing__
• `/rs` __Resume playing__
• `/m`  __Mute in VC__
• `/um`  __Unmute in VC__
• `/update` __Update Current Settings n Restarts the Bot__

🎶 **Currently Playing**
• Baws FM English Station
• @HARP_Chat Voice Chat


© Powered By 
[ __@HARP_Productions__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("❔ How To Use Me ❔", callback_data="help"),
                ],[
                InlineKeyboardButton('📢 Channel', url='https://t.me/harp_tech'),
                InlineKeyboardButton('💬 Support', url='https://t.me/Harp_chat')
                ],[
                InlineKeyboardButton('🤖 Bawwa Official', url='https://bawwaofficial.pages.dev'),
                InlineKeyboardButton('🎧 Listen To the FM', url='https://bawsfm.com')
                ],[
                InlineKeyboardButton('Bawwa Official', url='https://t.me/bawwaofficial'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/3330043776a2146b5e2dd.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
          [

                InlineKeyboardButton('📢 Channel', url='https://t.me/harp_tech'),

                InlineKeyboardButton('💬 Support', url='https://t.me/Harp_chat')

                ],[

                InlineKeyboardButton('🤖 Bawwa Official', url='https://bawwaofficial.pages.dev'),

                InlineKeyboardButton('🎧 Listen To the FM', url='https://bawsfm.com')
                ],[

                InlineKeyboardButton('Bawwa Official', url='https://t.me/bawwaofficial'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/3330043776a2146b5e2dd.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
