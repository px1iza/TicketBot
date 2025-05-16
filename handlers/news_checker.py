from telegram import Bot
from parser.tickets_parser import get_tickets_info
from handlers.user_service import load_users
import asyncio

last_info = None  

async def check_tickets_update(context):
    global last_info
    bot: Bot = context.bot

    current_info = get_tickets_info()

    if current_info != last_info:
        print("🔔 Змінилось розміщення квитків!")

        users = load_users()
        for user in users:
            try:
                await bot.send_message(
                    chat_id=user["id"],
                    text=f"🔔 Оновлення на сайті!\n\n{current_info}"
                )
            except Exception as e:
                print(f"❌ Не вдалося відправити користувачу {user['id']}: {e}")

        last_info = current_info
    else:
        print("✅ Змін немає.")