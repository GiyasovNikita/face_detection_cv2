# Используем базовый образ с Python
FROM python:3.9-slim

# Устанавливаем зависимости для OpenCV
RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev libopencv-dev

# Устанавливаем Python-зависимости
RUN pip install opencv-python-headless

# Копируем файлы проекта в контейнер
WORKDIR /app
COPY app.py .
COPY image.jpg .

# Указываем команду для запуска скрипта
CMD ["python", "app.py"]
