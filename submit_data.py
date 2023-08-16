import requests
import os


file_path = os.path.join(os.path.dirname(__file__), "image1.png")

data = {
    "beautyTitle": "перевал",
    "title": "Пхия",
    "add_time": "2023-08-10 12:00:00",
    "user": {
        "email": "qwerty@mail.ru",
        "fam": "Пупкин",
        "name": "Василий",
        "otc": "Иванович",
        "phone": "+7 555 55 55"
    },
    "coords": {
        "latitude": "45.3842",
        "longitude": "7.1525",
        "height": "1200"
    },
}

url = 'http://127.0.0.1:8000/myapp/submit-data/'

# Преобразование данных для изображений в кортежи
image_files = [('images', ('image1.png', open(file_path, 'rb'), 'image/png'))]

# Отправка POST запроса с данными в виде словаря и файлами для изображений
response = requests.post(url, data=data, files=image_files)
print(response.status_code)
print(response.text)