import asyncio
import logging
import os
import sys
import yaml
import random

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot
'''
inputs = None
with open('MyPack.yaml', 'r') as stream:
    inputs = yaml.safe_load(stream)

packs = inputs['Packages']
keyphrase = inputs['KeyPhrase'].lower()'''

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )

listen_options = {
    "local": True,
    "wallet": True,
    "dev": True,
    "hide-exploding": False,
    "convs": True,
    "filter_channel": None,
    "filter_channels": None,
}


def makeString(kp_str):
    pack_str = 'Here\'s your meet link: \npraja.sytes.net/'
    temp=kp_str.split()
    print(temp)
    if(len(temp)==1):
        random_str=['hailPJ','Satoshi','ProductiveMeet','ItsMeetTime','jitsibot']
        link=random.randint(0,len(random_str)-1)
        return pack_str+random_str[link]+ '\n'
    else:
        return pack_str+temp[1]+ '\n'

async def handler(bot, event):
    if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
        return
    msg = str(event.msg.content.text.body).lower()
    kp="!jitsipj"
    if kp in msg:
        channel = event.msg.channel
        sender = event.msg.sender.username
        # print(sender)
        if sender == bot.username:
            # print(msg)
            return
        pack_str = makeString(msg)
        # print(pack_str)
        await bot.chat.send(channel, pack_str)

paperkey = "PAPER_KEY"
username = 'USERNAME'

bot = Bot(
    username=username, paperkey=paperkey, handler=handler
)

asyncio.run(bot.start(listen_options))

