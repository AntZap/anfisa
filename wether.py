import datetime as dt
import requests

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}
# Определение + ко времени в зависимости от города из базы и вывод под нужный формат
def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


# Определение погоды в зависимости от города
def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 4,
        'M': '',
        'lang': 'ru'
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return f'Погода в городе - {response.text}'

    else:
        return '<ошибка на сервере погоды>'


def query():
    city = input("Введите город: ")
    what_weather(city)
    what_time(city)
    return print(f"Время в городе {city} - {what_time(city)} *** {what_weather(city)}")

query()