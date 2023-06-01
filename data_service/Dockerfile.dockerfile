# Используйте базовый образ Python
FROM python:3.9

# Установите зависимости
RUN pip install django pandas

# Копируйте код приложения в контейнер
WORKDIR /app
COPY . /app

# Выполните миграции базы данных
RUN python manage.py migrate

# Указываете порт, который будет слушать ваше приложение
EXPOSE 8000

# Команда для запуска сервера Django
CMD python manage.py runserver 0.0.0.0:8000
