# Polls - API сервис для создания и проведения опросов
## Описание

Для создания были использованы:

* Python
* Django
* Django Rest Framework
* JWT Token
* Redoc

Возможности:

* Создавать и редактировать опросы
* Создавать и редактировать вопросы к опросам
* Создавать варианты ответов к вопросам
* Проходить опросы

## Установка 
Клонируем репозиторий на локальную машину:

```$ git clone https://github.com/Rusich90/polls.git```

 Создаем виртуальное окружение:
 
 ```$ python -m venv venv```
 
 Активируем виртуальное окружение
 
 ```$ source venv/Scripts/activate```
 
 Переходм в папку polls
 
 ```$ cd polls/``` 
 
 Устанавливаем зависимости:

```$ pip install -r requirements.txt```

Создание и применение миграций:

```$ python manage.py makemigrations``` и ```$ python manage.py migrate```

Запускаем django сервер:

```$ python manage.py runserver```


Документация доступна по адресу http://127.0.0.1:8000/api/v1/redoc/
