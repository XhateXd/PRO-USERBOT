import asyncio
import io
import re

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from userbot import bot
from userbot.plugins.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from userbot.plugins.sql_helper.bot_blacklists import check_is_black_list
from userbot.plugins.sql_helper.botusers import add_me_in_db, his_userid
from userbot.plugins.sql_helper.idadder import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)


@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    chat = await event.get_chat()
    await tgbot.get_me()
    if check_is_black_list(chat.id):
        return
    await reply_id(event)
    mention = f"[{chat.first_name}](tg://user?id={chat.id})"
    my_mention = f"[{user.first_name}](tg://user?id={user.id})"
    first = chat.first_name
    last = chat.last_name
    my_first = user.first_name
    my_last = user.last_name
    f"{my_first} {my_last}" if my_last else my_first
    f"@{user.username}" if user.username else my_mention
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    replied_user.user.first_name
    vent = event.chat_id
    starttext = f"Hey! 👤{mention},\nI am {my_mention}'s assistant bot.\nYou can contact to my master from here.\n\nPowered By [『Lêɠêɳ̃dẞø†』](https://t.me/Pro_LegendBots)"
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            vent,
            message=f"Hi Sir/Miss, It's Me {bot_id}, Your Assistant ! \nHow Can I help U?",
            buttons=[
                [
                    Button.url(" Support ", "https://t.me/LegendBot_Pros"),
                    Button.url(" Updates ", "https://t.me/Pro_LegendBots"),
                ],
                [
                    custom.Button.inline("Users", data="users"),
                    custom.Button.inline("Settings", data="osg"),
                ],
                [custom.Button.inline("Hack", data="hack")],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tgbot.send_message(
            event.chat_id,
            message=starttext,
            link_preview=False,
            buttons=[
                [
                    Button.url(" Repo ", "https://github.com/PROBOY-OP/PRO-LEGENDBOT"),
                    Button.url(" Support ", "https://t.me/LegendBot_Pros"),
                ],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        total_users = get_all_users()
        users_list = "⚜List Of Total Users In Bot.⚜ \n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Total Users In Your Bot.",
                allow_cache=False,
            )
    else:
        await event.answer(
            "Wait ... Sorry U are Not My Owmer So, U Cant Acesss It",
            cache_time=0,
            alert=True,
        )


# Bot Permit.


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.raw_text.startswith("/"):
        pass
    elif event.sender_id == bot.uid:
        return
    else:
        await event.get_sender()
        event.chat_id
        sed = await event.forward_to(bot.uid)
        # Add User To Database ,Later For Broadcast Purpose
        # (C) @SpecHide
        add_me_in_db(sed.id, event.sender_id, event.id)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    msg.id
    msg_s = event.raw_text
    user_id, reply_message_id = his_userid(msg.id)
    if event.sender_id == bot.uid:
        if event.raw_text.startswith("/"):
            pass
        else:
            await tgbot.send_message(user_id, msg_s)


# broadcast
@tgbot.on(
    events.NewMessage(
        pattern="^/broadcast ?(.*)", func=lambda e: e.sender_id == bot.uid
    )
)
async def sedlyfsir(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            sent_count += 1
            await tgbot.send_message(int(starkcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except Exception as e:
            try:
                logger.info(f"Error : {error_count}\nError : {e} \nUsers : {chat_id}")
            except:
                pass
    await tgbot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}",
    )


@tgbot.on(
    events.NewMessage(pattern="^/stats ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    starkisnoob = get_all_users()
    await event.reply(
        f"**Stats Of Your Bot** \nTotal Users In Bot => {len(starkisnoob)}"
    )


@tgbot.on(events.NewMessage(pattern="^/help", func=lambda e: e.sender_id == bot.uid))
async def starkislub(event):
    grabonx = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /hack- hack anyone through string session \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot"
    await event.reply(grabonx)


@tgbot.on(
    events.NewMessage(pattern="^/block ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("Already Blacklisted")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blacklisted This Dumb Person")
        await tgbot.send_message(
            user_id, "You Have Been Blacklisted And You Can't Message My Master Now."
        )


@tgbot.on(
    events.NewMessage(pattern="^/unblock ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("Not Even. Blacklisted 🤦🚶")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("DisBlacklisted This Dumb Person")
        await tgbot.send_message(
            user_id, "Congo! You Have Been Unblacklisted By My Master."
        )
