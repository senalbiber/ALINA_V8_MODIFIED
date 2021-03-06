"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "๐คฃ๐คฃDo not grieve because I am alive๐๐\n\n โ๐๐ฒ ๐๐ซ๐๐๐ญ๐จ๐ซ: @happyisapartofmylife\n\nโ๐๐ฒ ๐ฎ๐ฉ๐๐๐ญ๐๐ฌ: @cinmahubupdates\n\nโ๐๐ฒ ๐ฌ๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ๐๐ซ: @ImError_X"
HELP = "Don't send like this๐๐๐ /help  โญ๏ธpress Help button...."
REPO = "It's private..... so sorry"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
