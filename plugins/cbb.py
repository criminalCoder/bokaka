
from pyrogram import Client, __version__
# from bot import Bot
from config import STREAM_LOGS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio
from urllib.parse import quote_plus
from util.file_properties import get_name, get_hash
from plugins.send_file import media_forward
from config import *

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    data = query.data
    cb_data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"○ Dev : <a href='https://t.me/LazyDeveloperr'>❤LazyDeveloperr❤</a>\n○  Updates Channel: <a href='https://t.me/LazyDeveloper'> LazyDeveloper</a> </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/LazyDeveloperr')
                    ]
                ]
            )
        )
    elif cb_data.startswith("generate_stream_link"):
        _, file_id = cb_data.split(":")
        try:
            user_id = query.from_user.id
            username =  query.from_user.mention

            lazy_file = await media_forward(client, user_id=STREAM_LOGS, file_id=file_id)
            
            fileName = {quote_plus(get_name(lazy_file))}
            lazy_stream = f"{URL}watch/{str(lazy_file.id)}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
            lazy_download = f"{URL}{str(lazy_file.id)}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"

            xo = await query.message.reply_text(f'🔐')
            await asyncio.sleep(1)
            await xo.delete()

            await lazy_file.reply_text(
                text=f"•• ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ꜰᴏʀ ɪᴅ #{user_id} \n•• ᴜꜱᴇʀɴᴀᴍᴇ : {username} \n\n•• File Name: {fileName}",
                quote=True,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("web Download", url=lazy_download),  # we download Link
                                                    InlineKeyboardButton('▶Stream online', url=lazy_stream)]])  # web stream Link
            )
            await query.message.edit(
                text="•• ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ☠︎⚔",
                quote=True,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("web Download", url=lazy_download),  # we download Link
                                                    InlineKeyboardButton('▶Stream online', url=lazy_stream)]])  # web stream Link
            )
        except Exception as e:
            print(e)  # print the error message
            await query.answer(f"☣something went wrong sweetheart\n\n{e}", show_alert=True)
            return
        
    elif data.startswith("get_embed_code"):
        _, log_id, file_name = data.split(":")
        try:
            # Generate the embed URL
            lazy_embed = f"{URL}/embed/{log_id}/{file_name}?hash={get_hash(log_id)}"

            # Create the HTML embed code
            embed_code = f"""
            <div style="position: relative; padding-bottom: 56.25%; height: 0">
                <iframe
                    src="{lazy_embed}"
                    scrolling="no"
                    frameborder="0"
                    webkitallowfullscreen
                    mozallowfullscreen
                    allowfullscreen
                    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%">
                </iframe>
            </div>
            """

            # Send the embed code to the user
            await query.message.reply_text(
                text=f"Here is your embed code:\n\n<code>{embed_code}</code>",
                quote=True,
                disable_web_page_preview=True,
                parse_mode="HTML"
            )
        except Exception as e:
            print(e)
            await query.answer(f"☣ Unable to generate embed code\n\n{e}", show_alert=True)

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
