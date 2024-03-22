# Мой проект URL Shortener

Этот проект представляет собой простую систему сокращения URL, разработанную с использованием Django.

## Установка и настройка

1. Создано и активировано виртуальное окружение:
    python3 -m venv myvenv
    source venv/bin/activate
    

2. Установите Django:
    pip install django
    

3. Создаy Django проект и приложение:
    
    django-admin startproject urlshortner .
    python manage.py startapp shortner
4. Установлена база данных PostgreSQL. командой sudo apt install pgadmin4
5. с помощью sudo -u postgres psql создана база, командой:
CREATE DATABASE mybaseshortner
6. создан пользователь командой: CREATE USER zhumagul WITH PASSWORD 'post'
7. назначена права доступа к созданной базе: GRANT ALL PRIVILEGES ON DATABASE mybaseshortner TO zhumagul
8. Настроена база данных PostgreSQL в файле settings.py:
    python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mybaseshortner',
            'USER': 'zhumagul',
            'PASSWORD': 'post',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    

9. Создайте необходимые модели Django в приложении shortner.
10. Чтобы добавлять, редактировать и удалять записи, для которых мы только что создали модель, мы используем панель управления администратора Django. необходимо настроить admin.py
11. Настроены urls файлы
12. добавлены функции во views файл
13. создание файла шаблона. Шаблоны сохраняются в корневой директории 

14. Применены миграции:
    
    python manage.py makemigrations
    python manage.py migrate
    

## Запуск проекта

1. Запустите сервер Django:
    
    python manage.py runserver
    

2. Откройте ваш браузер и перейдите по адресу http://127.0.0.1:8000/

## Вклад в проект

Если вы хотите внести свой вклад в проект, пожалуйста, создайте pull request. Мы рады любым предложениям и улучшениям!

