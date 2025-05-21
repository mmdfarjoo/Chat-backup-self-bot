from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetHistoryRequest

#get https://my.telegram.org/
api_id = 1234567 
api_hash = 'paste your api hash from telegram here'
backup_channel = -1002513229943  #Backup channel numeric ID

client = TelegramClient('self_backup_session', api_id, api_hash)

#Read message backup function using GetHistoryRequest
async def backup_unread_messages():
    async for dialog in client.iter_dialogs():
        if dialog.is_user and dialog.unread_count > 0:
            offset_id = 0
            total = dialog.unread_count
            while total > 0:
                history = await client(GetHistoryRequest(
                    peer=dialog.id,
                    offset_id=offset_id,
                    offset_date=None,
                    add_offset=0,
                    limit=100,
                    max_id=0,
                    min_id=0,
                    hash=0
                ))
                messages = history.messages
                if not messages:
                    break
                
                for message in reversed(messages):
                    if not message.out and not message.read:
                        sender = await message.get_sender()
                        user_id = sender.id
                        username = f"@{sender.username}" if sender.username else "none"
                        msg_text = message.message or ""

                        caption = f"{msg_text}\n\n— User ID: {user_id}\n— Username: {username}"

                        if message.media:
                            await client.send_file(backup_channel, file=message.media, caption=caption)
                        else:
                            await client.send_message(backup_channel, caption)

                        await message.mark_read()
                        total -= 1

                offset_id = messages[-1].id

#Listen to new messages and back them up

@client.on(events.NewMessage(incoming=True))
async def backup_private_message(event):
    sender = await event.get_sender()
    if event.is_private and not sender.bot:
        user_id = sender.id
        username = f"@{sender.username}" if sender.username else "none"
        msg_text = event.text or ""

        caption = f"{msg_text}\n\n— User ID: {user_id}\n— Username: {username}"

        if event.media:
            await client.send_file(backup_channel, file=event.media, caption=caption)
        else:
            await client.send_message(backup_channel, caption)

#running
async def main():
    await backup_unread_messages()
    print(" bot running")
    await client.run_until_disconnected()

client.start()
client.loop.run_until_complete(main())
