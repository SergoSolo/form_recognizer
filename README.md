# О проекте

Проект получения шаблона формы по запросу от пользователя.

Функционал:
* получение шаблона формы, если она была найдена. 
* если подходящей формы не нашлось, то вернет имя и тип введенных полей.


# Оглавление

[Requirements](#Requirements) <br>
[Запуск проекта](#Запуск-проекта) <br>
[Создание среды разработки](#Создание-сред-разработки) <br>
[Используемые технологии](#Используемые-технологии) <br>

# Requirements

* Python 3.10
* Docker 20.10+ [(инструкция по установке)](https://docs.docker.com/get-docker/).

# Клонирование репозитория
Склонируйте репозиторий git clone git@github.com:SergoSolo/form_recognizer.git

# Запуск проекта

Все команды выполняются из корневой директории проекта.

<details>
<summary>Проверка docker</summary>
<br>
По умолчанию проект запускается в докере. Для начала нужно убедиться, что докер
установлен. Открой любой терминал и выполни следующую команду:

```shell
docker --version
```
Должна быть выведена версия докера, это выглядит примерно так:
```
Docker version 20.10.21, build baeda1f
```
Если докер не установлен, то установите его, следуя [инструкции](https://docs.docker.com/get-docker/).
</details>

<details>
<summary>Запуск сервисов</summary>
<br>
<hr>

Для запуска проекта выполни следующую команду:
```
docker-compose up --build -d
```

Убедимся, что все контейнеры запущены:
```
docker-compose ps
```

Результат должен быть примерно такой (список сервисов может отличаться, но статус всех сервисов
должен быть `running`):
```
NAME                            COMMAND                  SERVICE             STATUS              PORTS
form_recognizer-mongo-1         "docker-entrypoint…"     mongo               running             0.0.0.0:27017->27017/tcp
form_recognizer-web-1           "python main.py"         web                 running             0.0.0.0:5000->5000/tcp
```

Проект доступен по ссылке http://localhost:5000

Остановить и удалить запущенные контейнеры:
```
docker-compose down
```

</details>

<details>
<summary>Примеры запросов</summary>
<br>

POST запрос к /get_form.
Запрос на http://localhost:5000/get_form?email=serg@mail.ru&username=serg&password=12345&phone=+79998883344:

При наличии формы в db ответом на запрос, вы получите:

```
{
  "form_name": "form_first"
}
```

Если подходящей формы нет, вы получите:

```
{
    "email": "EMAIL",
    "password": "TEXT",
    "username": "TEXT",
    "phone": "PHONE"
}

```
Так же в контейнере form_recognizer-web есть файл script.py, который делает тестовые POST запросы http://localhost:5000/get_form.

Скрипт можно запустить командой:

```
docker exec -ti <container_id> python script.py
```

Container_id можно посмотреть командой:

```
docker container ls
```

Результат такого запроса:

```
CONTAINER ID   IMAGE                 COMMAND                  CREATED             STATUS             PORTS                      NAMES
75dd54a26d49   form_recognizer-web   "python main.py"         9 minutes ago       Up 9 minutes       0.0.0.0:5000->5000/tcp     form_recognizer-web-1
ddba8d54ac22   mongo:latest          "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:27017->27017/tcp   form_recognizer-mongo-1
```

</details>

##  Используемые технологии:
- Python version 3.10
- Flask


## Автор:
> [Sergey](https://github.com/SergoSolo)