# Интерактивная карта Москвы

Данный [ресурс](http://cosmicorder.pythonanywhere.com/) представляет собой интерактивную карту Москвы, на которой
отмечены все виды активного отдыха с подробными описаниями, комментариями и
фотографиями.

## Как установить

Скачайте код проекта.

Создайте виртуальное окружение:

```
python3 -m venv venv
```

Активируйте виртуальное окружение:

- для Windows:
    ```
    venv\Scripts\activate 
    ```
- для Linux:
    ```
    source venv/bin/activate 
    ```

Установите зависимости командой:

```
pip install -r requirements.txt
```
## Запуск

Чтобы запустить сервер на локальном компьютере, введите в терминале:

- для Windows:
    ```
    python manage.py runserver 
    ```
- для Linux:
    ```
    ./manage.py runserver 
    ```

После этого переходите по ссылке 127.0.0.1:8000. Там вы увидите главную страницу.
## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта эти настройки не требуются**, значения уже проставлены по-умолчанию.

Доступны следущие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_NAME` — имя базы данных. По-умолчанию `'db.sqlite3'`.
- `STATIC_URL` — по-умолчанию это `'/static/'`. [Что такое STATIC_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATIC_URL).
- `STATIC_ROOT` — по-умолчанию это `'None'`, т.е. текущая папка. [Что такое STATIC_ROOT](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATIC_ROOT).
- `MEDIA_URL` — по-умолчанию это `'/media/'`. [Что такое MEDIA_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_URL).
- `MEDIA_ROOT` — по-умолчанию это `'None'`, т.е. текущая папка. [Что такое MEDIA_ROOT](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_ROOT).

## Цели проекта

Код написан в образовательных целях на онлайн-курсе для
веб-разработчиков [dvmn.org](https://dvmn.org/).