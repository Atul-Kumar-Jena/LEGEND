from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"wis ?(.*)"))
async def ues(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        chat = await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(str(event.chat_id), str(r_msg.from_id), bot_api_file_id))
        else:
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`".format(str(event.chat_id), str(r_msg.from_id))) 

        try:
            new_update = await borg.get_entity(int("{}".format(str(r_msg.from_id))))
        except ValueError:
            new_update = await borg.get_entity('me')
        await event.edit(new_update.stringify())
@borg.on(admin_cmd(pattern=r"uis ?(userid)"))
async def ues(event):
    giveVar = event.text
    a = giveVar[5:]
    try:
        new_update = await borg.get_entity(int(a))
    except ValueError:
        new_update = await borg.get_entity('me')
    await event.edit(new_update.stringify())
@borg.on(admin_cmd(pattern=r"mes ?(.*)"))
async def mes(event):
    new_update = await borg.get_entity('me')
    await event.edit(new_update.stringify())
