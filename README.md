# Тестовое задание backend разработчик

## Содержание
- [Задание](#задание)
- [Начало работы](#начало-работы)

## Задание

Стек Django\DRF

Даны модели "Категория Блюд" и "Блюдо" для ресторана.

Даны сериализаторы.

В выборку попадают только Блюда у которых `is_publish=True`.

Если в категории нет блюд (или все блюда данной категории имеют `is_publish=False`) - не включаем ее в выборку.

Запрос в БД сделать любым удобным способом:

Django ORM (предпочтительно), Raw SQL, Sqlalchemy…

Написать View который вернет для API `127.0.0.1/api/v1/foods/`

JSON следующего формата:

```commandline
[
      {
         "id":1,
         "name_ru":"Напитки",
         "name_en":null,
         "name_ch":null,
         "order_id":10,
         "foods":[
            {
               "internal_code":100,
               "code":1,
               "name_ru":"Чай",
               "description_ru":"Чай 100 гр",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  200
               ]
            },
            {
               "internal_code":200,
               "code":2,
               "name_ru":"Кола",
               "description_ru":"Кола",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            },
            {
               "internal_code":300,
               "code":3,
               "name_ru":"Спрайт",
               "description_ru":"Спрайт",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            },
            {
               "internal_code":400,
               "code":4,
               "name_ru":"Байкал",
               "description_ru":"Байкал",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            }
         ]
      },
      {
         "id":2,
         "name_ru":"Выпечка",
         "name_en":null,
         "name_ch":null,
         "order_id":20,
         "foods":[...]
      },
      {...},
      {...}
   ]
```

## Начало работы

1. **Клонирование приложения**<br>
   `git clone git@github.com:a-krstn/utf_test.git`
2. **Создание виртуального окружения и его активация**<br>
   В командной строке из директории проекта<br>
   `python -m venv .venv`<br>
   - Windows: `.venv\Scripts\activate`<br>
   - Linux/MacOS: `source .venv/bin/activate`
3. **Установка зависимостей**<br>
   `pip install -r requirements.txt`
4. **Определение переменных среды**<br>
   Создайте файл .env в корневой папке проекта и определите в нем переменные среды.
   Перечень требуемых переменных перечислен в файле .env.example.<br>
5. **Выполнение миграций**<br>
   В командной строке выполните команду `python manage.py migrate`
6. **Создание суперпользователя**<br>
   В командной строке выполните команду `python manage.py createsuperuser`.
   Заполните требуемые данные.
7. **Загрузка данных**<br>
   В командной строке выполните команду `python manage.py loaddata db.json`<br>
8. **Запуск**<br>
   Выполнить команду `python manage.py runserver`.<br>
   Перейти по адресу http://127.0.0.1:8000/api/v1/foods/
