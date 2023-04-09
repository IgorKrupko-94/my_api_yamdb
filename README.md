# API_YAMDB


## Авторы:
**Команда 22** в составе:
* Даниил Фёдоров
* Игорь Крупко
* Павел Дровнин

### О чём проект:

Yamdb, с помощью API позволяет собирать отзывы на произведения искусства, 
такие как картины, музыкальные композиции, фильмы и другие.

У каждого произведения искусства есть название, год создания, категория и жанр.
Всем пользователям доступен просмотр списка всех хранящихся в базе 
произведений, сведения определенного произведения, 
отзывов и комментариев к нему, 
а также просмотр всех хранящихся в базе категорий и жанров.

* Для авторизованных пользователей доступно написание отзывов 
и комментариев к произведениям. 

* Для модераторов доступно написание отзывов и комментариев, 
а также удаление отзывов и комментариев, которые оставили другие пользователи.

* Для администраторов доступно добавление произведений, категорий, 
жанров, а также написание отзывов и комментариев, 
удаление отзывов и комментариев, которые оставили другие пользователи.

Проект также направлен на обучение и развитие совместной работы в команде у каждого из участников. 


### Запуск проекта на dev-сервере:

Клонировать репозиторий и перейти в него в командной строке:
``` 
git clone git@github.com:IgorKrupko-94/my_api_yamdb.git
```
```
cd my_api_yamdb
```
Установите и активируйте виртуальное окружение c учётом версии Python 3.7 (выбираем python не ниже 3.7):
``` 
py -3.7 -m venv venv 
```
Для пользователей Windows:
``` 
source venv/Scripts/activate 
```
Для пользователей Linux и macOS:
``` 
source venv/bin/activate 
```
Обновляем до последней версии пакетный менеджер pip:
``` 
python -m pip install --upgrade pip 
```
Затем нужно установить все зависимости из файла requirements.txt:
``` 
pip install -r requirements.txt 
```
Заходим в папку с manage.py:
```
cd api_yamdb
```
Выполняем миграции:
``` 
python manage.py migrate 
```
Запускаем проект:
``` 
python manage.py runserver 
```


### Примеры команд для API доступные всем пользователям:
Получение кода подтверждения на почту для нового пользователя

```
POST http://127.0.0.1:8000/api/v1/auth/signup/
    {
    "email": "string",
    "username": "string"
    }
```

Получение токена для зарегестрированного пользователя

```
POST http://127.0.0.1:8000/api/v1/auth/token/
    {
    "username": "string",
    "confirmation_code": "string"
    }
```

Получение списка всех произведений

```
GET http://127.0.0.1:8000/api/v1/titles/
```

Получение списка всех категорий

```
GET http://127.0.0.1:8000/api/v1/categories/
```

Получение списка всех жанров

```
GET http://127.0.0.1:8000/api/v1/genres/
```

Получение списка всех отзывов к произведению

```
GET http://127.0.0.1:8000/api/v1/titles/<title_id>/reviews/
```

Добавление отзыва к произведению

```
POST http://127.0.0.1:8000/api/v1/titles/<title_id>/reviews/
    {
    "text": "string",
    "score": 10
    }
```

Получение списка всех комментариев к отзыву на произведение

```
GET http://127.0.0.1:8000/api/v1/titles/<title_id>/reviews/<reviews_id>/comments/
```

Добавление комментария к отзыву

```
POST http://127.0.0.1:8000/api/v1/titles/<title_id>/reviews/<reviews_id>/comments/
    {
    "text": "string"
    }
```

### Примеры команд для API доступные для модераторов 
(также доступны команды из категории "Все пользователи"):

Изменение отзыва к произведению

```
POST http://127.0.0.1:8000/api/v1/titles/<title_id>/reviews/<review_id>
    {
    "text": "string",
    "score": 10
    }
```

Изменение комментария к отзыву

```
POST http://127.0.0.1:8000/api/v1/titles/<title_id>/reviews/comments/<comment_id>
    {
    "text": "string"
    }
```

### Примеры команд для API доступные для администраторов 
(также доступны команды из категории "Все пользователи" и "модераторы"):

#### Произведения

Создание нового произведения в базе

```
POST http://127.0.0.1:8000/api/v1/titles/
    {
    "name": "string",
    "year": 0,
    "description": "string",
    "genre": [
        "string"
    ],
    "category": "string"
    }
```

Изменение произведения в базе

```
PATCH http://127.0.0.1:8000/api/v1/titles/<title_id>/
```

Удаление произведения

```
DELETE http://127.0.0.1:8000/api/v1/titles/<title_id>/
```

#### Категории

Создание новой категории

```
POST http://127.0.0.1:8000/api/v1/categories/
    {
    "name": "string",
    "slug": "string"
    }
```

Удаление категории

```
DELETE http://127.0.0.1:8000/api/v1/categories/<slug>
```

### Жанры

Создание нового жанра

```
POST http://127.0.0.1:8000/api/v1/genres/
    {
    "name": "string",
    "slug": "string"
    }
```

Удаление жанра

```
DELETE http://127.0.0.1:8000/api/v1/genres/<slug>
```
