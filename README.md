
## Автор

- [@TemaKut](https://github.com/TemaKut)


## Локальный запуск проекта:

* Спуститься в e_com
```bash
  cd e_com
```

Создать .env файл со следующим наполнением:
SECRET_KEY=qwerty1234Q

* Создать образ контейненра при помощи Dockerfile
```bash
docker build -t e_com .
```
* Запустить соответствующий контейнер 
```bash
docker run --name e_com -it -p 8000:8000 e_com
```
Получить доступ к проекту можно на http://localhost:8000

* Для дальнейшего тестирования проекта следует выполнить следующие команды:

```bash
docker exec e_com python manage.py migrate
docker exec e_com python manage.py test
```

* Загрузить CSV файл (Находится в директории с manage.py) можно следующей командой:
```bash
docker exec e_com python manage.py load_data
```

* В тех-задании посоветовали использовать tinyDB. Посмотрев видео увидел что разница между этой БД и sqlite только в расширении. Файл БД остаётся в проекте. Принял решение оставить sqlite.

* Для меня важно получить обратную связь по проекту. Именно поэтому, пожалуйста, напишите мне в telegtam: @TemaCu
