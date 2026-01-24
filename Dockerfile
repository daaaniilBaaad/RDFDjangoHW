# Указываем базовый образ
FROM python:3.13

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt ./

# Обновляем pip и устанавливаем зависимости из requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем остальной код приложения
COPY . .

# Указываем порт, на котором будет работать Django (по умолчанию 8000)
EXPOSE 8000

# Команда для запуска Django-сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
