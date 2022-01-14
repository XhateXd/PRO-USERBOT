from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CmdHelp
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd("gencc$"))
@bot.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(LEGENDevent):
    if LEGENDevent.fwd_from:
        return
    LEGENDcc = Faker()
    LEGENDname = LEGENDcc.name()
    LEGENDadre = LEGENDcc.address()
    LEGENDcard = LEGENDcc.credit_card_full()

    await edit_or_reply(
        LEGENDevent,
        f"__**👤 NAME :- **__\n`{LEGENDname}`\n\n__**🏡 ADDRESS :- **__\n`{LEGENDadre}`\n\n__**💸 CARD :- **__\n`{LEGENDcard}`",
    )


@bot.on(admin_cmd(pattern="bin ?(.*)"))
@bot.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    LEGEND_input = event.pattern_match.group(1)
    chat = "@szbinscheckerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2143004427)
            )
            await event.client.send_message(chat, f"/bin {LEGEND_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @szbinscheckerbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@bot.on(admin_cmd(pattern="register ?(.*)"))
@bot.on(sudo_cmd(pattern="register ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    LEGEND_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/register {LEGEND_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@bot.on(admin_cmd(pattern="password ?(.*)"))
@bot.on(sudo_cmd(pattern="password ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    LEGEND_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/password {LEGEND_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CmdHelp("carder").add_command("gencc", None, "Generates fake cc...").add_command(
    "register", None, "Register Ur Account Here"
).add_command("password", "<enter>", "Set ur Account Password On CXM.CARDS").add()
