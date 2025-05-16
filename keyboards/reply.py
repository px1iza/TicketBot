from telegram import ReplyKeyboardMarkup

def main_menu():
    keyboard = [
        ["🎫 Перевірити квитки", "🌐 Перейти на сайт"],
        ["🎭 Обрати інший спектакль"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)