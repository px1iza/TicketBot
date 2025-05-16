from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN
from handlers.commands import start, button_handler, handle_message
from handlers.news_checker import check_tickets_update

application = Application.builder().token(TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button_handler))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# JobQueue для періодичної перевірки сайту
job_queue = application.job_queue
job_queue.run_repeating(check_tickets_update, interval=300, first=10)

if __name__ == "__main__":
    print("✅ Бот запущено! Щоб зупинити — Ctrl+C")
    application.run_polling()