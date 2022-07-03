from pyrogram import *
from pyrogram.types import *

def start(client, message):
    message.reply_text("""**/search <hentai name> to search**\n Powered By @MetaVoid""", parse_mode="markdown")
