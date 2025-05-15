# api_final
api final
# api_final
### Описание проекта:

API для сервиса YATUBE. Позволяет получать:комментарии, список публикаций, групп сервиса, создавать комментарии и публикации к постам, подписываться на других пользователей посредством API запросов. Безопасные запросы можно выполнять анонимно, для других запросов нужно получать токен.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/maxim190404/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры использования:

Запрос на получение токена:

```
POST /api/v1/jwt/create/
{
  "username": "string",
  "password": "string"
}
```

Создание публикации:

```
POST /api/v1/posts/
{
  "text": "string",
  "image": "string",
  "group": None
}
```

Чтобы разобраться с другими примерами и изучить более подробное руководство после запуска проекта на локальной машине перейдите:

```
http://127.0.0.1:8000/redoc/
```
