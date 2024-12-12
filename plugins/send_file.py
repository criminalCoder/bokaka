# (c) @LazyDeveloperr

import asyncio
from config import *
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from urllib.parse import quote_plus
from util.file_properties import get_name, get_hash, get_media_file_size


async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if FORWARD_AS_COPY is True:
                lazy_file = await bot.copy_message(chat_id=STREAM_LOGS, from_chat_id=CHANNEL_ID,
                                          message_id=file_id)


                lazy_stream = f"{URL}watch/{str(lazy_file.id)}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
                lazy_download = f"{URL}{str(lazy_file.id)}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
                
                fileName = quote_plus(get_name(lazy_file))

                await lazy_file.reply_text(
                    text=f"•• ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ꜰᴏʀ ɪᴅ #{user_id} \n\n• File Name : {fileName}",
                    quote=True,
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Direct Download", url=lazy_download),  # we download Link
                                                        InlineKeyboardButton('▶Stream online', url=lazy_stream)]])  # web stream Link
                )
                return await bot.copy_message(chat_id=user_id, from_chat_id=CHANNEL_ID,
                                          message_id=file_id, 
                                          reply_markup=InlineKeyboardMarkup(
                                            [
                                                [
                                                  InlineKeyboardButton("Fast Download", url=lazy_download),
                                                  InlineKeyboardButton("▶Stream online", url=lazy_stream),
                                                ],
                                            ]),
                                            )
        elif FORWARD_AS_COPY is False:
            lazy_file = await bot.copy_message(chat_id=user_id, from_chat_id=CHANNEL_ID,
                                              message_ids=file_id)
            lazy_stream = f"{URL}watch/{str(lazy_file.id)}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
            lazy_download = f"{URL}{str(lazy_file.id)}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
            fileName = quote_plus(get_name(lazy_file))
            await lazy_file.reply_text(
                text=f"•• ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ꜰᴏʀ ɪᴅ #{user_id} \n\n•• ᖴᎥᒪᗴ Nᗩᗰᗴ : {fileName}",
                quote=True,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("web Download", url=lazy_download),  # we download Link
                                                    InlineKeyboardButton('▶Stream online', url=lazy_stream)]])  # web stream Link
            )
            return await bot.forward_messages(chat_id=user_id, from_chat_id=CHANNEL_ID,
                                              message_ids=file_id,
                                              reply_markup=InlineKeyboardMarkup(
                                            [
                                                [
                                                  InlineKeyboardButton("Fast Download", url=lazy_download),
                                                  InlineKeyboardButton("▶Stream online", url=lazy_stream),
                                                ],
                                            ]),
                                            )

    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)

