import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types

from userbot import *
from userbot import ALIVE_NAME
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.helpers.tools import media_type
from userbot.helpers.utils import _format
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓєgєи∂"

LEGEND = bot.uid


class AFK:
    def __init__(self):
        self.USERAFK_ON = {}
        self.afk_time = None
        self.last_afk_message = {}
        self.afk_star = {}
        self.afk_end = {}
        self.reason = None
        self.msg_link = False
        self.afk_type = None
        self.media_afk = None
        self.afk_on = False


AFK_ = AFK()


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    if AFK_.afk_on is False:
        return
    back_alive = datetime.now()
    AFK_.afk_end = back_alive.replace(microsecond=0)
    if AFK_.afk_star != {}:
        total_afk_time = AFK_.afk_end - AFK_.afk_star
        time = int(total_afk_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        elif h > 0:
            endtime += f"{h}h {m}m {s}s"
        else:
            endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message = event.message.message
    if (("afk" not in current_message) or ("#afk" not in current_message)) and (
        "on" in AFK_.USERAFK_ON
    ):
        shite = await event.client.send_message(
            event.chat_id,
            "`My Gf Says enough for today! So No Longer afk.\nWas afk for " + endtime + "`",
        )
        AFK_.USERAFK_ON = {}
        AFK_.afk_time = None
        await asyncio.sleep(5)
        await shite.delete()
        AFK_.afk_on = False
        if LOGGER:
            await event.client.send_message(
                LOGGER_ID,
                "#AFKFALSE \n`Set AFK mode to False\n"
                + "Back alive! No Longer afk.\nWas afk for "
                + endtime
                + "`",
            )


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_afk(event):  # sourcery no-metrics
    if AFK_.afk_on is False:
        return
    back_alivee = datetime.now()
    AFK_.afk_end = back_alivee.replace(microsecond=0)
    if AFK_.afk_star != {}:
        total_afk_time = AFK_.afk_end - AFK_.afk_star
        time = int(total_afk_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        elif h > 0:
            endtime += f"{h}h {m}m {s}s"
        else:
            endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text or "#afk" in current_message_text:
        return False
    if not await event.get_sender():
        return
    if AFK_.USERAFK_ON and not (await event.get_sender()).bot:
        msg = None
        if AFK_.afk_type == "media":
            if AFK_.reason:
                message_to_reply = (
                    f"`I am AFK .\n\n📍AFK Since {endtime}\n📍Reason : {AFK_.reason}`"
                )
            else:
                message_to_reply = f"`I am AFK .\n\nAFK Since {endtime}\nReason : Not Mentioned ( ಠ ʖ̯ ಠ)`"
            if event.chat_id:
                msg = await event.reply(message_to_reply, file=AFK_.media_afk)
        elif AFK_.afk_type == "text":
            if AFK_.msg_link and AFK_.reason:
                message_to_reply = (
                    f"**I am Busy with my Gf So I'm AFK .\n\nAFK Since {endtime}\nReason : **{AFK_.reason}"
                )
            elif AFK_.reason:
                message_to_reply = (
                    f"`I am Busy with my gf So I'm AFK .\n\nAFK Since {endtime}\nReason : {AFK_.reason}`"
                )
            else:
                message_to_reply = f"`I am Busy with my Gf So I'm AFK .\n\nAFK Since {endtime}\nReason : Not Mentioned ( ಠ ʖ̯ ಠ)`"
            if event.chat_id:
                msg = await event.reply(message_to_reply)
        if event.chat_id in AFK_.last_afk_message:
            await AFK_.last_afk_message[event.chat_id].delete()
        AFK_.last_afk_message[event.chat_id] = msg
        if event.is_private:
            return
        hmm = await event.get_chat()
        if Config.LOGGER_ID == -100:
            return
        full = None
        try:
            full = await event.client.get_entity(event.message.from_id)
        except Exception as e:
            LOGS.info(str(e))
        messaget = media_type(event)
        resalt = f"#AFK_TAGS \n<b>Group : </b><code>{hmm.title}</code>"
        if full is not None:
            resalt += f"\n<b>From : </b> 👤{_format.htmlmentionuser(full.first_name , full.id)}"
        if messaget is not None:
            resalt += f"\n<b>Message type : </b><code>{messaget}</code>"
        else:
            resalt += f"\n<b>Message : </b>{event.message.message}"
        resalt += f"\n<b>Message link: </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> link</a>"
        if not event.is_private:
            await event.client.send_message(
                Config.LOGGER_ID,
                resalt,
                parse_mode="html",
                link_preview=False,
            )


@borg.on(admin_cmd(pattern=r"afk (.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    "To mark yourself as afk i.e. Away from keyboard"
    AFK_.USERAFK_ON = {}
    AFK_.afk_time = None
    AFK_.last_afk_message = {}
    AFK_.afk_end = {}
    AFK_.afk_type = "text"
    start_1 = datetime.now()
    AFK_.afk_on = True
    AFK_.afk_star = start_1.replace(microsecond=0)
    if not AFK_.USERAFK_ON:
        input_str = event.pattern_match.group(1)
        if ";" in input_str:
            msg, mlink = input_str.split(";", 1)
            AFK_.reason = f"[{msg.strip()}]({mlink.strip()})"
            AFK_.msg_link = True
        else:
            AFK_.reason = input_str
            AFK_.msg_link = False
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            AFK_.afk_time = datetime.now()
        AFK_.USERAFK_ON = f"on: {AFK_.reason}"
        if AFK_.reason:
            await eod(event, f"`I shall be Going afk! because ~` {AFK_.reason}", 5)
        else:
            await eod(event, "`I shall be Going afk! `", 5)
        if LOGGER:
            if AFK_.reason:
                await event.client.send_message(
                    LOGGER_ID,
                    f"#AFKTRUE \nSet AFK mode to True, and Reason is {AFK_.reason}",
                )
            else:
                await event.client.send_message(
                    LOGGER_ID,
                    "#AFKTRUE \nSet AFK mode to True, and Reason is Not Mentioned",
                )


@borg.on(admin_cmd(pattern=r"mafk (.*)", outgoing=True))
async def _(event):
    "To mark yourself as afk i.e. Away from keyboard (supports media)"
    reply = await event.get_reply_message()
    media_t = media_type(reply)
    if media_t == "Sticker" or not media_t:
        return await edit_or_reply(
            event, "`You haven't replied to any media to activate media afk`"
        )
    if not LOGGER_ID:
        return await edit_or_reply(
            event, "`To use media afk you need to set PRIVATE_GROUP_BOT_API_ID config`"
        )
    AFK_.USERAFK_ON = {}
    AFK_.afk_time = None
    AFK_.last_afk_message = {}
    AFK_.afk_end = {}
    AFK_.media_afk = None
    AFK_.afk_type = "media"
    start_1 = datetime.now()
    AFK_.afk_on = True
    AFK_.afk_star = start_1.replace(microsecond=0)
    if not AFK_.USERAFK_ON:
        input_str = event.pattern_match.group(1)
        AFK_.reason = input_str
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            AFK_.afk_time = datetime.now()
        AFK_.USERAFK_ON = f"on: {AFK_.reason}"
        if AFK_.reason:
            await eod(event, f"`I shall be Going afk! because ~` {AFK_.reason}", 5)
        else:
            await eod(event, "`I shall be Going afk! `", 5)
        AFK_.media_afk = await reply.forward_to(LOGGER_ID)
        if AFK_.reason:
            await event.client.send_message(
                LOGGER_ID,
                f"#AFKTRUE \nSet AFK mode to True, and Reason is {AFK_.reason}",
            )
        else:
            await event.client.send_message(
                LOGGER_ID,
                "#AFKTRUE \nSet AFK mode to True, and Reason is Not Mentioned",
            )


CmdHelp("afk").add_command(
    "afk",
    "<reply to media>/<or type a reson>",
    "Marks you AFK(Away from Keyboard) with reason(if given) also shows afk time. Media also supported.",
).add_info("When U Go Offline Use this Command").add_warning(
    "Harmless Module✅"
).add_type(
    "Official"
).add()
