# API для работы с импортируемыми данными

## Загрузка файла

**URL:** `/upload`
**Метод:** `POST`

Эндпоинт для загрузки файла в формате CSV.

**Пример запроса:**
POST /upload
Content-Type: multipart/form-data
Body: <файл в формате CSV>


**Пример успешного ответа:**
{
"message": "Файл загружен успешно!"
}


## Получение списка файлов

**URL:** `/files`
**Метод:** `GET`

Получение списка файлов с информацией о колонках.

**Пример запроса:**
GET /files


**Пример успешного ответа:**
{
"files": ["file1.csv", "file2.csv"]
}


## Получение данных из файла

**URL:** `/data/<filename>`
**Метод:** `GET`

Получение данных из конкретного файла с опциональной фильтрацией и сортировкой.

**Пример запроса:**
GET /data/file1.csv?filters=column1:value1,column2:value2&sort_by=column1


**Пример успешного ответа:**
[
{"column1": "value1", "column2": "value2"},
{"column1": "value3", "column2": "value4"}
]


## Удаление файла

**URL:** `/files/<filename>`
**Метод:** `DELETE`

Удаление ранее загруженного файла.

**Пример запроса:**
DELETE /files/file1.csv


**Пример успешного ответа:**
{
"message": "File deleted successfully"
}


## Развертывание приложения

1. Установите зависимости:
pip install -r requirements.txt

2. Запустите миграции базы данных:
python manage.py migrate

3. Запустите сервер Django:
python manage.py runserver


