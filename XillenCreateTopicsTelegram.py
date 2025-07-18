from telethon.sync import TelegramClient
from telethon.tl.functions.channels import CreateForumTopicRequest
from telethon.errors import SessionPasswordNeededError, FloodWaitError
import asyncio
import time
import os

# Ваши данные
API_ID = ВАШ_API_ID #Получить тут -> my.telegram.org
API_HASH = 'ВАШ_API_HASH' #Получить тут -> my.telegram.org
SESSION_NAME = 'thm_session'
GROUP_ID = -1234567890  # ID вашей группы

# Темы с эмодзи
TOPICS = [
    {"title": "#Название темы", "": "эмодзи для темы"},
    {"title": "#Название темы", "emoji": "эмодзи для темы"},
    {"title": "#Название темы", "emoji": "эмодзи для темы"},
    {"title": "#Название темы", "emoji": "эмодзи для темы"},
    {"title": "#Название темы", "emoji": "эмодзи для темы"},
    {"title": "#Название темы", "emoji": "эмодзи для темы"}

#Если надо больше тем создать то просто добавляете строку "{"title": "#Название темы", "emoji": "эмодзи для темы"}" и потом закрываете квадратной скобкой ] ну крч просто добавляте сколько надо

]

async def create_topics(client):
    print(f"Создаю темы в группе {GROUP_ID}...")
    created_count = 0
    
    for topic in TOPICS:
        try:
            # Создаем тему
            result = await client(CreateForumTopicRequest(
                channel=GROUP_ID,
                title=topic["title"],
                icon_emoji_id=0  # 0 = случайный эмодзи
            ))
            created_count += 1
            print(f"✅ Создана тема: {topic['title']}")
            await asyncio.sleep(5)  # Увеличил паузу между созданиями
            
        except FloodWaitError as e:
            wait_time = e.seconds + 10
            print(f"🚫 Требуется подождать {wait_time} секунд из-за ограничений Telegram")
            time.sleep(wait_time)
            continue
            
        except Exception as e:
            print(f"❌ Ошибка при создании темы {topic['title']}: {str(e)}")
            continue
    
    return created_count

async def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    
    try:
        print("Подключаемся к Telegram...")
        await client.connect()
        
        if not await client.is_user_authorized():
            print("Авторизация...")
            phone = "+ваш_номер"
            
            try:
                await client.send_code_request(phone)
                code = input("Введите код из Telegram: ").strip()
                
                try:
                    await client.sign_in(phone=phone, code=code)
                except SessionPasswordNeededError:
                    password = input("Введите пароль 2FA: ")
                    await client.sign_in(password=password)
            
            except FloodWaitError as e:
                print(f"🚫 Telegram требует подождать {e.seconds} секунд перед повторной попыткой")
                return
        
        # Проверяем авторизацию
        me = await client.get_me()
        print(f"Авторизован как: {me.first_name} ({me.phone})")
        
        # Создаем темы
        created = await create_topics(client)
        print(f"\nСоздано тем: {created}/{len(TOPICS)}")
        
        if created < len(TOPICS):
            print("⚠ Некоторые темы не созданы. Запустите скрипт через 10-15 минут")
    
    except Exception as e:
        print(f"🔥 Критическая ошибка: {str(e)}")
    finally:
        await client.disconnect()
        print("Сессия закрыта")

if __name__ == '__main__':
    print("Запуск создания тем...")
    asyncio.run(main())
    print("Работа завершена. Можно спать 😴")
