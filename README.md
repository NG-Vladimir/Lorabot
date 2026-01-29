# Telegram-бот «Привет»

При нажатии кнопки **Старт** (или команды `/start`) бот отвечает: **Привет!**

---

## Запуск 24/7 в облаке (без своего компьютера)

Чтобы бот работал круглосуточно, залей проект на один из сервисов ниже и задай там токен. Локально ничего держать не нужно.

### Вариант 1: Railway — [railway.app](https://railway.app)

**Деплой из репозитория [Lorabot](https://github.com/NG-Vladimir/Lorabot):**

1. Залий код в **GitHub** (репозиторий [NG-Vladimir/Lorabot](https://github.com/NG-Vladimir/Lorabot)):
   ```bash
   cd "/Users/vladimir/Desktop/Новая папка 2"
   git init
   git add .
   git commit -m "Telegram bot: /start → Привет"
   git branch -M main
   git remote add origin https://github.com/NG-Vladimir/Lorabot.git
   git push -u origin main
   ```
2. Зайди на **[railway.app](https://railway.app)** и войди через GitHub.
3. **New Project** → **Deploy from GitHub repo** → выбери репозиторий **NG-Vladimir/Lorabot**.
4. В проекте открой свой сервис → вкладка **Variables** → **Add Variable**:
   - **Name:** `TELEGRAM_BOT_TOKEN`
   - **Value:** твой токен от @BotFather
5. В **Settings** сервиса проверь **Start Command:** должно быть `python bot.py` (Railway может подставить это из Procfile).
6. Деплой запустится автоматически. Бот будет работать 24/7.

У Railway есть бесплатный кредит ($5 в месяц).

---

### Вариант 2: Render.com

1. Зарегистрируйся на **[render.com](https://render.com)** (через GitHub).
2. Залей проект на **GitHub** (те же файлы, что и выше).
3. В Render: **New** → **Background Worker**.
4. Подключи свой репозиторий.
5. Укажи:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
6. В разделе **Environment** добавь переменную:
   - **Key:** `TELEGRAM_BOT_TOKEN`
   - **Value:** твой токен от @BotFather
7. Нажми **Create Background Worker**. Бот будет работать 24/7.

На бесплатном плане Render может ограничивать время работы воркера — для стабильного 24/7 смотри их тарифы.

---

### Вариант 3: Fly.io

1. Установи [flyctl](https://fly.io/docs/hands-on/install-flyctl/) и войди: `fly auth login`.
2. В папке с ботом выполни: `fly launch` (создай приложение, на вопросы можно отвечать по умолчанию).
3. Задай секрет с токеном:  
   `fly secrets set TELEGRAM_BOT_TOKEN=твой_токен`
4. Запусти: `fly deploy`.  
Бот будет крутиться на Fly.io 24/7 (есть бесплатный лимит).

---

## Локальный запуск (для проверки)

### 1. Создай бота в Telegram

1. Напиши **@BotFather** в Telegram.
2. Команда `/newbot` → имя → username (оканчивается на `bot`).
3. Сохрани выданный **токен**.

### 2. Установи зависимости и запусти

```bash
pip install -r requirements.txt
# или: pip3 install -r requirements.txt

export TELEGRAM_BOT_TOKEN="ТВОЙ_ТОКЕН"
python bot.py
# или: python3 bot.py
```

Найди бота в Telegram, нажми **Старт** — он ответит «Привет!». Остановка: `Ctrl+C`.
