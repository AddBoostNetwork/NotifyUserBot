from telethon import TelegramClient, events

# Замените эти значения на свои
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'
notify_user_id = 'TARGET_USER_ID'  # ID пользователя, которому будут отправляться уведомления

# Создаем клиент
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # Получаем информацию о пользователе, отправившем сообщение
    sender = await event.get_sender()
    user = sender.first_name if sender.first_name else sender.username

    # Формируем текст сообщения
    message_text = f"Сообщение от {user}.\n\n{event.message.message}"

    # Отправляем уведомление на указанный аккаунт
    await client.send_message(notify_user_id, message_text)

async def main():
    await client.start()
    print("Client is running...")
    await client.run_until_disconnected()

# Запускаем клиент
with client:
    client.loop.run_until_complete(main())