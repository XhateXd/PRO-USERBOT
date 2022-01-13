import asyncio
import time
from telethon import version
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from userbot import ALIVE_NAME, LEGENDversion
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from . import *
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG
DEFAULTUSER = ALIVE_NAME 
LEGEND_IMG = "https://telegra.ph/file/153977a71b928874151a5.jpg"
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG 
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@LegendBot_Pro"
@bot.on(admin_cmd(outgoing=True, pattern="legend$"))
@bot.on(sudo_cmd(pattern="legend$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    if LEGEND_IMG:
        LEGEND_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        LEGEND_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        LEGEND_caption += f"        **✘𝕭𝖔† 𝕾𝖙𝖆𝖙𝖚𝖘✘** \n"
        LEGEND_caption += f"•🔥• **Oաղ̃ҽ̈ɾ**          ~ {ALIVE_NAME}\n\n"
        LEGEND_caption += f"•🌟• **𝖑𝖊ɠêɳ̃dẞø†**   ~ {LEGENDversion}\n"
        LEGEND_caption += f"•🌟• **†ҽ̀lҽ́thøղ̃**     ~ `{version.__version__}`\n"
        LEGEND_caption += f"•🌟• **𝚄ρtime**         ~ `{uptime}`\n"
        LEGEND_caption += f"•🌟• **𝙶𝚛𝚘𝚞𝚙**           ~ [𝙶𝚛𝚘𝚞𝚙](t.me/LegendBot_Pro)\n"
        LEGEND_caption += f"•🌟• **𝙼𝚢 𝙶𝚛𝚘𝚞𝚙**  ~ {CUSTOM_YOUR_GROUP}\n"
        await alive.client.send_file(
            alive.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         \n"
            f"•⚡• 𝕿єℓєτнοи    : `{version.__version__}`\n"
            f"🇮🇳 ℓєgєи∂ϐοτ  : `{LEGENDversion}`\n"
            f"🇮🇳 υρτιмє        : `{uptime}`\n"
            f"🔱 ɱαรƭεɾ        : {mention}\n"
            f"🔱 σωɳεɾ         : [ℓєgєи∂](t.me/Pro_LegendBoy)\n",
        )


msg = (
    gvarstatus("ALIVE_TEMPLATE")
    or f"""
**  ⚜️ Lêɠêɳ̃dẞø† ιѕ σиℓιиє ⚜️**

       {Config.ALIVE_MSG}
    **  Bø✞︎ ẞ✞︎α✞︎µѕ **
**•⚜️•Øաղ̃ҽ̈r     :** **{mention}**
**•🌹•𝖑𝖊ɠêɳ̃dẞø✞︎  :** {LEGENDversion}
**•🌹•✞︎ҽ̀lҽ́ƭhøղ  :** {version.__version__}
**•🌹•Ãbûßê     :**  {abuse_m}
**•🌹•ßudø      :**  {is_sudo}
**•🌹•Bøt.      :** {Config.BOY_OR_GIRL}
"""
)
botname = Config.BOT_USERNAME


@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def legend_a(event):
    try:
        legend = await bot.inline_query(botname, "alive")
        await legend[0].click(event.chat_id)
        if event.sender_id == Pro_LegendBoy:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


file1 = "https://te.legra.ph/file/2426eab17330c6e6310ea.mp4"
file2 = "https://te.legra.ph/file/11ec9dd576ee5536125b2.jpg"
file3 = "https://te.legra.ph/file/d2a5265abdc4e73af1f94.jpg"
file4 = "https://te.legra.ph/file/d17467283e73c884834a5.jpg"
file5 = "https://telegra.ph/file/af51de2749a4506d3eb43.jpg"
""" =======================CONSTANTS====================== """
pm_caption = f"** {CUSTOM_ALIVE_TEXT}**\n"
pm_caption += f"**╭────────────**\n"
pm_caption += f"┣»»»『{legend_mention}』«««\n"
pm_caption += f"┣Lêɠêɳ̃dẞø† ~ {LEGENDversion}\n"
pm_caption += f"┣Lêɠêɳ̃d  ~ [Owner](https://t.me/Pro_LegendBoy)\n"
pm_caption += f"┣Support ~ [G𝖗ουρ](https://t.me/LegendBot_Pro)\n"
pm_caption += f"┣Řepô    ~ [Rєρο](https://github.com/PROBOY-OP/PRO-LEGENDBOT)\n"
pm_caption += f"**╰────────────**\n"


@borg.on(admin_cmd(pattern=r"about"))
@borg.on(sudo_cmd(pattern="about$", allow_sudo=True))
async def amireallyalive(yes):
    edit_time = 12
    await yes.get_chat()
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)
    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)

    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)

    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)

    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await alive.delete()

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command("bot", None, "υѕє αи∂ ѕєє").add_command(
    "legend", None, "Its Same Like Alive"
).add_command("about", None, "BEST alive command").add_command(
    "alive", None, "Its Show ur Alive Template"
).add_warning(
    "Harmless Module✅"
).add_info(
    "Checking Alive"
).add_type(
    "Official"
).add()
