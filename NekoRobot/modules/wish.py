import random
from PIL import Image
from NekoRobot import telethn as neko
from telethon import events
@neko.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):

 if e.is_reply:
         mm = random.randint(1,100)
         lol = await e.get_reply_message()
         fire = "https://telegra.ph/file/85f91175ae99287d54cc4.jpg"
         await neko.send_file(e.chat_id, fire,caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.💜**\n\n__Chance of success {mm}%__", reply_to=lol)
 if not e.is_reply:
         mm = random.randint(1,100)
         fire = "https://telegra.ph/file/85f91175ae99287d54cc4.jpg"
         await neko.send_file(e.chat_id, fire,caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.💜**\n\n__Chance of success {mm}%__", reply_to=e)
