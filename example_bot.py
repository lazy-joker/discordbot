import discord
from discord.ext import tasks
import bme680tph
from datetime import datetime
import subprocess
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

import os
from os.path import join, dirname
from dotenv import load_dotenv

def get_sensor_post_discord():
    sensor_data = bme680tph.get_sensor()
    return """温度 : {0:.2f} [°C],
気圧 : {1:.2f} [hPa],
湿度 : {2:.3f} [%RH]""".format(
            sensor_data[0],
            sensor_data[1],
            sensor_data[2])

client = discord.Client()
myMQTTClient = AWSIoTMQTTClient("raspi-home")

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
        await message.channel.send(get_sensor_post_discord())


@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻 : 00分のときのみセンサの値を送信
    print(datetime.now().strftime('%H:%M'))
    if datetime.now().strftime('%M') == '00':
        await client.get_channel(sandbox_channel_id).send('定期送信\n'+get_sensor_post_discord())

    sensor_data = bme680tph.get_sensor()
    json_data = json.dumps({"temp": sensor_data[0], "pres": sensor_data[1], "moist": sensor_data[2], "datetime": datetime.now().strftime("%Y/%m/%d %H:%M:%S")})
    myMQTTClient.publish("test", json_data, 0)
    print(json_data)

if __name__ == '__main__':
    # init for discordbot.

    load_dotenv(verbose=True)
    sandbox_channel_id = int(os.environ.get("SANDBOX_CHANNEL_ID"))
    bot_token = os.environ.get("BOT_TOKEN")
    
    #init for AWS IoT.

    myMQTTClient.configureEndpoint("a252n8vsuty40h-ats.iot.ap-northeast-1.amazonaws.com", 443)
    myMQTTClient.configureCredentials("./cert/root.pem", "./cert/f0e00cdc2f-private.pem.key", "./cert/f0e00cdc2f-certificate.pem.crt")
    myMQTTClient.configureOfflinePublishQueueing(-1)
    myMQTTClient.configureDrainingFrequency(2)
    myMQTTClient.configureConnectDisconnectTimeout(10)
    myMQTTClient.configureMQTTOperationTimeout(5)

    # Connect to AWS IoT endpoint and publish a message
    myMQTTClient.connect()

    loop.start()
    client.run(bot_token)

