import random
from PIL import Image
from NekoRobot import telethn as neko
from telethon import events
@neko.on(events.NewMessage(pattern="/guess ?(.*)"))
async def wish(e):

 if e.is_reply:
         mm = random.randint(1,100)
         lol = await e.get_reply_message()
         fire = "https://telegra.ph/file/9ff2283cd3aea55c49c5f.jpg"
         await neko.send_file(e.chat_id, fire,caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your Guess is {mm}%__**\n\n__Correct!!!", reply_to=lol)
 if not e.is_reply:
         mm = random.randint(1,100)
         fire = "https://telegra.ph/file/9ff2283cd3aea55c49c5f.jpg"
         await neko.send_file(e.chat_id, fire,caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your Guess is {mm}%__**\n\n__Correct!!!", reply_to=e)
