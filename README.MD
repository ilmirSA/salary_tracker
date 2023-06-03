
## Тестовое задание

Данный код представляет собой простой API-сервер на базе фреймворка FastAPI, который обрабатывает запросы на получение информации о зарплате и дате следующего повышения для сотрудников. Для авторизации пользователей используется токен, который генерируется при успешной аутентификации на сервере.

## Используемые библиотеки

-   FastAPI
-   Pydantic
-   datetime
-   JWT
-   uvicorn

## Как запустить

1.  Установите все необходимые зависимости, используя команду  `pip install -r requirements.txt`
2.  Запустите сервер используя команду  `uvicorn main:app --reload`
3.  После этого вы можете отправлять запросы на сервер, используя любой инструмент для отправки HTTP-запросов например Curl.

## Обработка запросов

1.  `/login`  - POST-метод для получения токена доступа. Принимает параметры  `username`  и  `password`  в формате JSON. Если пользователь существует и пароль верный, то будет сгенерирован JWT-токен, который будет возвращен в ответе.
    
2.  `/salary`  - GET-метод для получения информации о зарплате и дате следующего повышения для сотрудника. Принимает заголовок  `Authorization`  с JWT-токеном в формате  `Bearer <token>`. В ответ на запрос возвращается информация о зарплате и дате следующего повышения для сотрудника, указанного в токене.
    

## Примеры запросов

1.  Получение токена доступа:

Copy

```
curl -X POST "http://localhost:8000/login?username=john&password=password" 
```

Ответ:



```
{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImlsbWlyIiwiZXhwIjoxNjg1Nzg5NTcyfQ.Hmvz_sxaPaYkIohRkY27QT41BFmiQTc0Zwavckg2SHI","token_type":"bearer"}

```

2.  Получение информации о зарплате и дате следующего повышения:

Copy

```
curl -X GET "http://localhost:8000/salary" -H "Authorization: Bearer <token>"
```

Ответ:

```
{"name":"Ilmir","salary":60000,"next_raise":"2023-07-08T00:00:00"}
```