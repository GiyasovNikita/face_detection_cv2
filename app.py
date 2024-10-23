import cv2

# Загружаем изображение
image_path = 'image.jpg'
image = cv2.imread(image_path)

# Загрузка каскада Хаара для обнаружения лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Преобразуем изображение в оттенки серого
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Обнаруживаем лица
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Выводим результат
if len(faces) == 0:
    print("Лиц не найдено.")
else:
    print(f"Найдено {len(faces)} лиц(о/а):")
    for (x, y, w, h) in faces:
        print(f"Лицо на координатах X:{x}, Y:{y}, ширина:{w}, высота:{h}.")
