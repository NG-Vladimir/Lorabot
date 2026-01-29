"""
Простой Telegram-бот: при команде /start отвечает "Привет"
"""
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start — отвечает приветствием."""
    await update.message.reply_text("Привет! Господин Владимир! ")


def main() -> None:
    # Получаем токен из переменной окружения
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Ошибка: задай переменную окружения TELEGRAM_BOT_TOKEN")
        print("Как получить токен: напиши @BotFather в Telegram, создай бота, скопируй токен")
        return

    # Создаём приложение и добавляем обработчик /start
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    # Запускаем бота
    print("Бот запущен. Нажми Ctrl+C для остановки.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
