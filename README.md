## Конвертер валюты

![2023-07-10_22-01-35](https://github.com/ApT3rn/currency_converter_flask/assets/96689510/20e0d502-63c1-4580-a898-14c6dc81a704)
<p align=center>Домашняя страница</p>
<br>

Конвертер валюты, принимает количество выбранной валюты, 
и возвращает в ответе сколько получиться в другой валюте.<br>
Курс берётся с открытого API: https://api.exchangerate-api.com/v4/latest/USD

### Стек:

Python 3.11, Flask, requests, HTML, CSS.

### Инструкция для запуска:

1. Скачать проект: ``` git clone https://github.com/ApT3rn/currency_converter.git ```
2. Перейти в папку с проектом: ``` cd currency_converter ```
3. Создать виртуальной окружение: ``` python -m venv env ```
4. Перейти по пути: ``` cd env/Scripts ```
5. Запустить виртуальное окружение: ``` activate ```
6. Загрузить необходимые зависимости, тут два варианта:
   ``` pip install -r requirements.txt ```
   ``` pipenv install ```
7. Запустить приложение: ``` flask run ```
