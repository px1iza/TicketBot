import requests
from bs4 import BeautifulSoup
from config import URL

def get_tickets_info():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    tickets_section = soup.find('section', class_='selectTickets')

    if tickets_section:
        return tickets_section.text.strip()
    else:
        return "Квитків не знайдено."

# Функція для регулярного запиту (наприклад для тесту можна зробити log)
async def check_news_update(context):
    info = get_tickets_info()
    print("🔄 Автоматична перевірка квитків:", info)