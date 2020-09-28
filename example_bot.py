import discord
from discord.ext import tasks
import bme680tph
from datetime import datetime
import subprocess

import os
from os.path import join, dirname
from dotenv import load_dotenv

client = discord.Client()

load_dotenv(verbose=True)
sandbox_channel_id = int(os.environ.get("SANDBOX_CHANNEL_ID"))
bot_token = os.environ.get("BOT_TOKEN")

@client.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(client))
    await client.get_channel(sandbox_channel_id).send('こんにちは')

@client.event
async def on_message(message):
    print('on_message:{0}'.format(message.content));
    if message.author.bot:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('よぅ!')

    if message.content.startswith('$ojichat'):
        try:
            res = subprocess.check_output('ojichat')
        except:
            print('ojichat : error')
        await message.channel.send(res.decode())

    if message.content.startswith('$室温'):
        await message.channel.send(bme680tph.get_sensor())

@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻 : 00分のときのみセンサの値を送信
    print(datetime.now().strftime('%H:%M'))
    if datetime.now().strftime('%M') == '00':
        await client.get_channel(sandbox_channel_id).send('定期送信\n'+bme680tph.get_sensor())

loop.start()
client.run(bot_token)

