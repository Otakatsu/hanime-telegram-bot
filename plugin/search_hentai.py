from pyrogram import *
from pyrogram.types import *
import requests
import json
from pyrogram.errors.exceptions.bad_request_400 import ButtonDataInvalid
import sys

def hentaisearch(client, message):
    msg = message.text
    msgSplit = msg.split(" ")
    msgSplit.remove(msgSplit[0])
    query = " "
    query = query.join(msgSplit)
    if query == "":
        client.send_animation(chat_id=message.chat.id,
                              animation="https://telegra.ph/file/cdeae50a8a23041b01935.mp4",
                              caption=f"""**/search <space> hentai name**""", parse_mode="markdown")
    else:
        url = f"https://apikatsu.otakatsu.studio/api/hanime/search?query={query}&page=0"
        result = requests.get(url) 
        result = result.json()
        K = result["response"]
        keyb = []
        for x in K:
            id = x["slug"]
            name = x["name"]
            keyb.append([InlineKeyboardButton(f"{name}", callback_data=f"info_{id}")])
        if keyb == []:
            message.reply_text("No results found, Please check the Spelling and try again")
        else:
            repl = InlineKeyboardMarkup(keyb)
            message.reply_text(f"Your Search Results for **{query}**", reply_markup=repl, parse_mode="markdown")
