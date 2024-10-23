# Приложение для распознавания лиц с использованием OpenCV

Это приложение написано на Python и использует библиотеку OpenCV для обнаружения лиц на изображении. Приложение загружает изображение `image.jpg` из директории, обнаруживает лица и выводит координаты лиц в терминал.

## Как запустить приложение локально

Запуск приложения локально
Для локального запуска приложения без Docker выполните следующие шаги:

### Склонируйте репозиторий:

```bash
git clone https://github.com/GiyasovNikita/face_detection_cv2.git
cd face_detection_cv2
```

### Установите необходимые зависимости:

```bash
pip install opencv-python-headless
```

### Запустите приложение:

```bash
python app.py
```

Приложение выведет в консоль количество обнаруженных лиц и их координаты на изображении.

## Сборка и запуск Docker-образа

### Чтобы собрать образ локально, выполните следующую команду:

```bash
docker build -t opencv_face_detection .
```

### Чтобы запустить контейнер с приложением, используйте следующую команду:

```bash
docker run --rm -v "%cd%:/app" opencv_face_detection
```

### Вы можете скачать и запустить образ напрямую с DockerHub, используя следующие команды:
```bash
docker pull redalertpanic/opencv_face_detection:latest
docker run --rm redalertpanic/opencv_face_detection:latest
```