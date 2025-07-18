# XillenCreateTopicsTelegram

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Telethon](https://img.shields.io/badge/Library-Telethon-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Этот Python скрипт позволяет автоматически создавать темы (разделы форума) в ваших Telegram-группах. Он использует библиотеку `Telethon` для взаимодействия с Telegram API, значительно упрощая организацию больших сообществ.

## ✨ Возможности

*   *Автоматическое создание тем:* Создает заданный вами список тем.
*   *Обработка лимитов Telegram:* Скрипт умеет ждать при `FloodWaitError` и продолжать работу.
*   *Простая авторизация:* Подключение через номер телефона и 2FA.

## ⚠️ Важное примечание о смайликах тем (Emoji)

В этом скрипте для `icon_emoji_id` установлено значение `0`. Это означает, что Telegram *автоматически выберет случайный эмодзи* для каждой новой темы. Если вы хотите установить конкретный эмодзи, вам потребуется получить его `emoji_id` и заменить `0` на это значение.

## 📦 Установка и Запуск

Следуйте этим шагам, чтобы начать использовать скрипт.

### Шаг 1: Скачать код

Клонируйте репозиторий:
bash
git clone https://github.com/BengaminButton/XillenCreateTopicsTelegram.git
cd XillenCreateTopicsTelegram

### Шаг 2: Установить зависимости

Настоятельно рекомендуется использовать виртуальное окружение:

1. *Создайте виртуальное окружение:*
    
bash
    python3 -m venv venv
    
2. *Активируйте виртуальное окружение:*
    *   Для *Linux / macOS*:
        
bash
        source venv/bin/activate
        
    *   Для *Windows (в командной строке или PowerShell)*:
        
bash
        venv\Scripts\activate
        
3. *Установите `telethon`:*
    
bash
    pip install telethon
    

### Шаг 3: Настройка скрипта

Откройте файл `forum_creator.py` и заполните следующие переменные:

1. *`API_ID` и `API_HASH`*:
    *   Получите их на [my.telegram.org](https://my.telegram.org) (API development tools).
    
python
    API_ID = 12345678 # Ваш API_ID
    API_HASH = 'ВАШ_API_HASH' # Ваш API_HASH
    

2. *`GROUP_ID`*:
    *   ID вашей группы. Перешлите любое сообщение из группы боту `@userinfobot`, он покажет ID (будет отрицательным, например, `-1001234567890`).
    
python
    GROUP_ID = -1234567890 # ID вашей группы
    

3. *`phone`*:
    *   Ваш номер телефона в международном формате.
    
python
    phone = "+79XXXXXXXXX" # Ваш номер телефона (например, +79123456789)
    

4. *`TOPICS`*:
    *   Список тем, которые вы хотите создать. *ОБРАТИТЕ ВНИМАНИЕ на правильный синтаксис:*
    
python
    TOPICS = [
        {"title": "#ДоброПожаловать"},
        {"title": "#ВопросыИОтветы"},
        {"title": "#Обсуждения"},
        {"title": "#НовостиКанала"},
        {"title": "#Предложения"},
        {"title": "#Правила"}
        # Добавьте сколько угодно тем по аналогии:
        # {"title": "#ВашаНоваяТема"},
        # {"title": "#ЕщёОднаТема"}
    ]
    

### Шаг 4: Запустить скрипт

После настройки всех переменных, запустите скрипт:

bash
python forum_creator.py

При первом запуске вам потребуется ввести код авторизации из Telegram и, если включена, пароль 2FA. Скрипт начнет создавать темы, выводя прогресс в консоль.
