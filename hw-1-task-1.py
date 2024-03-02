from datetime import datetime
from collections import defaultdict

# Cписок словників users (тестові користувачі).
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)},
    {"name": "Elon Musk", "birthday": datetime(1971, 6, 28)},
    {"name": "Oprah Winfrey", "birthday": datetime(1954, 1, 29)},
    {"name": "Marie Curie", "birthday": datetime(1867, 11, 7)},
    {"name": "Di Dan", "birthday": datetime(1964, 3, 3)},
    {"name": "Albert Einstein", "birthday": datetime(1879, 3, 14)},
    {"name": "Jane Austen", "birthday": datetime(1775, 12, 16)},
    {"name": "Malala Yo", "birthday": datetime(1947, 3, 4)},
    {"name": "Doro Do", "birthday": datetime(1986, 3, 5)},
    {"name": "Frida Ka", "birthday": datetime(1999, 3, 8)},
]

def get_birthdays_per_week(users):
    birthdays = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]

        # Аналіз дати народження:
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Оцінка дати на цей рік.
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days

        # Визначення дня тижня.
        if delta_days < 7:
            day_of_week = birthday_this_year.strftime('%A')
            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"
            
            # Зберігаємо ім'я користувача у відповідний день тижня.
            birthdays[day_of_week].append(name)
    
    # Виводимо зібрані імена по днях тижня (з понеділка по п'ятницю) у відповідному форматі.
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        if birthdays[day]:
            print(f"{day}: {', '.join(birthdays[day])}")

get_birthdays_per_week(users)