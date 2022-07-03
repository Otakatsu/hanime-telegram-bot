from pyrogram import *
from pyrogram.types import *
import requests
import os
import subprocess
import json

def hentailink(client, callback_query):
    click = callback_query.data
    clickSplit = click.split("_")
    link = clickSplit[1]
    chatid = callback_query.from_user.id
    messageid = callback_query.message.message_id
    url = f"https://hanime.metavoid.info/link?id={link}" 
    result = requests.get(url) 
    result = result.json()  
    url = result["data"][0]["url"]
    if not url == "":
        url1 = result["data"][0]["url"]
        url2 = result["data"][1]["url"]
        url3 = result["data"][2]["url"]        
        keyb = [
            [InlineKeyboardButton("360p", url=f"{url3}")],
            [InlineKeyboardButton("480p", url=f"{url2}")],
            [InlineKeyboardButton("720p", url=f"{url1}")],
            [InlineKeyboardButton("Back", callback_data=f"info_{link}")]
        
        ]
        repl = InlineKeyboardMarkup(keyb)
        client.edit_message_text(chat_id=chatid, message_id=messageid, text=f"""You are now watching **Episode https://hanime.tv/videos/hentai/{link}** :-\nPlease share the bot if you like it ☺️.""", reply_markup=repl, parse_mode="markdown")
        
    if url == "":
        url1 = result["data"][1]["url"]
        url2 = result["data"][2]["url"]
        url3 = result["data"][3]["url"]
        keyb = [
            [InlineKeyboardButton("360p", url=f"{url3}")],
            [InlineKeyboardButton("480p", url=f"{url2}")],
            [InlineKeyboardButton("720p", url=f"{url1}")],
            [InlineKeyboardButton("Back", callback_data=f"info_{link}")]
        
        ]
        repl = InlineKeyboardMarkup(keyb)
        client.edit_message_text(chat_id=chatid, message_id=messageid, text=f"""You are now watching **Episode https://hanime.tv/videos/hentai/{link}** :-\nPlease share the bot if you like it ☺️.""", reply_markup=repl, parse_mode="markdown")
        
def hentaidl(client, callback_query):
    click = callback_query.data
    clickSplit = click.split("_")
    link = clickSplit[1]
    chatid = callback_query.from_user.id
    messageid = callback_query.message.message_id
    url = f"https://hanime.metavoid.info/link?id={link}" 
    result = requests.get(url) 
    result = result.json()  
    url = result["data"][0]["url"]
    callback_query.edit_message_text("""Wait till we fetch hentai for you...\nStatus: **DOWNLOADING**""", parse_mode="markdown")
    if not url == "":        
        url3 = result["data"][2]["url"]
        file1 = f"{link}.mp4"        
        subprocess.run("ffmpeg -i {} -acodec copy -vcodec copy {}".format(url3, file1), shell=True)
        callback_query.edit_message_text("""Uploading Now""", parse_mode="markdown")              
        client.send_document(chat_id=chatid, document=f'{link}.mp4', caption=f"""Download By @hanime_dl_bot""", parse_mode="markdown")   
        os.remove(file1)
    if url == "":     
        url3 = result["data"][3]["url"]
        file1 = f"{link}.mp4"        
        subprocess.run("ffmpeg -i {} -acodec copy -vcodec copy {}".format(url3, file1), shell=True)
        callback_query.edit_message_text("""Uploading Now""", parse_mode="markdown")       
        client.send_document(chat_id=chatid, document=f'{link}.mp4', caption=f"""Download By @hanime_dl_bot""", parse_mode="markdown")   
        os.remove(file1)
 
