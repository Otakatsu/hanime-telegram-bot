from pyrogram import *
from pyrogram.types import *
import requests
import os
import json




def infohentai(client, callback_query):
    click = callback_query.data
    clickSplit = click.split("_")
    query = clickSplit[1]
    chatid = callback_query.from_user.id
    messageid = callback_query.message.message_id
    url = f"https://apikatsu.otakatsu.studio/api/hanime/details?id={query}" 
    result = requests.get(url) 
    result = result.json()   
    description = result["description"]
    name = result["name"]
    img = result["poster"]
    view = result["views"]     
    released_date = result["released_date"]
    keyb = [
        [InlineKeyboardButton("Download Now", callback_data=f"dlt_{query}")],
        [InlineKeyboardButton("Link", callback_data=f"link_{query}")]
    ]
    repl = InlineKeyboardMarkup(keyb)
    client.edit_message_text(chat_id=chatid, message_id=messageid, text=f"""**Name:** [{name}]({img})\n**View:** {view}\n**Release Date:** {released_date}""", reply_markup=repl, parse_mode="markdown")
