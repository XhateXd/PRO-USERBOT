import datetime

from telethon import version

from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.plugins.sql_helper.globals import addgvar, delgvar, gvarstatus
from userbot.utils import *

LEGEND_USER = bot.me.first_name
Pro_LegendBoy = bot.uid
legend_mention = f"[{LEGEND_USER}](tg://user?id={Pro_LegendBoy})"

gban_pic = "./userbot/resources/pics/gban.mp4"
main_pic = "./userbot/resources/pics/main.jpg"
core_pic = "./userbot/resources/pics/core.jpg"
chup_pic = "./userbot/resources/pics/chup.mp4"
bsdk_pic = "./userbot/resources/pics/bsdk.jpg"
bsdkwale_pic = "./userbot/resources/pics/bsdk_wale.jpg"
chutiya_pic = "./userbot/resources/pics/chutiya.jpg"

perf = "[ Přô-Lêɠêɳ̃dẞø† ]"


DEVLIST = ["5061095379"]


async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid


l1 = Config.HANDLER
l2 = Config.SUDO_HANDLER
sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m = "Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.YOUR_CHANNEL or "Pro_LegendBot"
my_group = Config.YOUR_GROUP or "LegendBot_Pro"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")


mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

chnl_link = "https://t.me/Pro_LegendBot"
Legend_channel = f"[✞︎t͛ẞ̸ 𝖑𝖊ɠêɳ̃dẞø✞︎]({chnl_link})"
grp_link = "https://t.me/LegendBot_Pro"
Legend_grp = f"[𝖑𝖊ɠêɳ̃dẞø✞︎ Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
