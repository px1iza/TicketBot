from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from parser.tickets_parser import get_tickets_info
from config import URL
from handlers.user_service import add_user
from datetime import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = {
        "id": update.effective_user.id,
        "first_name": update.effective_user.first_name,
        "username": update.effective_user.username,
        "joined_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    added = add_user(user_data)

    if added:
        print(f"➕ Новий користувач: {user_data}")
    else:
        print(f"👤 Користувач уже був: {user_data}")

    keyboard = [
        ["🎟 Перевірити квитки"],
        ["🌐 Перейти на сайт"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        f"Вітаю, {update.effective_user.first_name}! 👋\nЦей бот допомагає перевірити наявність квитків на виставу «Конотопська відьма».\n\nОберіть дію нижче:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'check_tickets':
        tickets_info = get_tickets_info()
        await query.edit_message_text(
            text=f"🔍 Ось що вдалося знайти:\n\n{tickets_info}"
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🎟 Перевірити квитки":
        tickets_info = get_tickets_info()
        await update.message.reply_text(f"🔍 Ось що вдалося знайти:\n\n{tickets_info}")

    elif text == "🌐 Перейти на сайт":
        await update.message.reply_text(f"Ось лінк на сайт: {URL}")

    else:
        await update.message.reply_text("Я вас не зрозумів. Будь ласка, оберіть дію з меню нижче.")