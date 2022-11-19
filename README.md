# api_yamdb

api_yamdb

## Авторы:
**Команда 22** в составе:
* Павел Дровнин
* Даниил Фёдоров
* Игорь К

### О чем проект:

Yamdb, с помощью API позволяет собирать отзывы на произведения искусства, такие как картины, музыкальные композиции, фильмы и другие.

У каждого произведения искусства есть название, год создания, категория и жанр. Всем пользователям доступен просмотр списка всех хранящихся в базе произведений, сведения определенного произведения, отзывов и комментариев к нему, а также просмотр всех хранящихся в базе категорий и жанров.

* Для авторизованных пользователей доступно написание отзывов и комментариев к произведениям. 

* Для администраторов доступно добавление произведений, категорий, жанров, а также написание отзывов и комментариев.

Проект также направлен на обучение и развитие совместной работы в команде у каждого из участников. 

### Как развернуть:

```
git clone git@github.com:pashpiter/api_yatube.git
```

```
Открыть папку с проектом
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры команд для API доступные всем пользователям:
Получение кода подтверждения на почту для нового пользователя

```
POST http://127.0.0.1:8000/api/v1/auth/signup/
```

Получение токена для зарегестрированного пользователя

```
POST http://127.0.0.1:8000/api/v1/auth/token/
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

Получение списка всех комментариев к отзыву на произведение

```
GET http://127.0.0.1:8000/api/v1/titles/<title_id>/reviews/comments/
```

### Примеры команд для API доступные для администраторов:

Создание нового произведения в базе

```
POST http://127.0.0.1:8000/api/v1/titles/
```

Изменение произведеия в базе

```
PATCH http://127.0.0.1:8000/api/v1/titles/<title_id>/
```

Удаление произведеия

```
DELETE http://127.0.0.1:8000/api/v1/titles/<title_id>/
```

Создание новой категории

```
POST http://127.0.0.1:8000/api/v1/categories/
```

Удаление категории

```
DELETE http://127.0.0.1:8000/api/v1/categories/<slug>
```

Создание нового жанра

```
POST http://127.0.0.1:8000/api/v1/genres/
```

Удаление жанра

```
DELETE http://127.0.0.1:8000/api/v1/genres/<slug>
```
